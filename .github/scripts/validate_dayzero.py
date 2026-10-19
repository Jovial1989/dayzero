#!/usr/bin/env python3
"""Check .dayzero/ content against the rules used during development.

Usage: python .github/scripts/validate_dayzero.py [repo_root]
Exits 1 and prints one line per problem when any check fails.
"""
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

STACK_SECTIONS = list(range(1, 13))
STACK_MAX_LINES = 150
EM_DASH = "—"

errors = []


def fail(path, msg):
    errors.append(f"{path}: {msg}")


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fail(path, f"cannot parse JSON: {e}")
        return None


def check_schema(doc_path, schema_path, root):
    schema = load_json(schema_path)
    doc = load_json(doc_path)
    if schema is None or doc is None:
        return None
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "(root)"
        fail(doc_path.relative_to(root), f"{loc}: {err.message}")
    return doc


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]).resolve()
    dz = root / ".dayzero"

    measurements = check_schema(dz / "measurements.json", dz / "measurements.schema.json", root)
    check_schema(dz / "kano_answers.json", dz / "kano_answers.schema.json", root)
    measurement_ids = {m.get("id") for m in (measurements or {}).get("measurements", []) if isinstance(m, dict)}

    persona_schema = dz / "personas" / "persona.schema.json"
    for path in sorted((dz / "personas").glob("*.json")):
        if path.name == persona_schema.name:
            continue
        persona = check_schema(path, persona_schema, root)
        if not isinstance(persona, dict):
            continue
        rel = path.relative_to(root)
        seen = set()
        for i, rule in enumerate(persona.get("rules") or []):
            if not isinstance(rule, dict):
                continue
            rid = rule.get("id")
            if rid in seen:
                fail(rel, f"rules/{i}: duplicate rule id '{rid}'")
            seen.add(rid)
            mid = rule.get("measurement")
            if measurements is not None and mid not in measurement_ids:
                fail(rel, f"rules/{i}: measurement '{mid}' is not in .dayzero/measurements.json")

    for path in sorted((dz / "stacks").glob("*.md")):
        rel = path.relative_to(root)
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) > STACK_MAX_LINES:
            fail(rel, f"{len(lines)} lines, limit is {STACK_MAX_LINES}")
        if not any(re.match(r"^Checked: \d{4}-\d{2}-\d{2}", l) for l in lines):
            fail(rel, "missing 'Checked: YYYY-MM-DD' line")
        found = [int(m.group(1)) for l in lines if (m := re.match(r"^## (\d+)\. \S", l))]
        if found != STACK_SECTIONS:
            fail(rel, f"sections must be '## 1.' to '## 12.' in order, found {found}")

    stacks_dir = dz / "stacks"
    detect = check_schema(stacks_dir / "detect.json", stacks_dir / "detect.schema.json", root)
    if isinstance(detect, dict):
        rel = (stacks_dir / "detect.json").relative_to(root)
        entries = [s for s in detect.get("stacks", []) if isinstance(s, dict)]
        ids = [s.get("id") for s in entries]
        orders = [s.get("order") for s in entries]
        for dup in sorted({o for o in orders if orders.count(o) > 1}, key=str):
            fail(rel, f"duplicate order {dup}")
        for dup in sorted({i for i in ids if ids.count(i) > 1}, key=str):
            fail(rel, f"duplicate id '{dup}'")
        for s in entries:
            for ref in list(s.get("beats") or []) + ([s["falls_through_to"]] if s.get("falls_through_to") else []):
                if ref not in ids:
                    fail(rel, f"'{s.get('id')}' references unknown stack id '{ref}'")
            sid = s.get("id")
            if sid and sid != "unknown" and not (stacks_dir / f"{sid}.md").exists():
                fail(rel, f"stack id '{sid}' has no guide .dayzero/stacks/{sid}.md")
        for path in sorted(stacks_dir.glob("*.md")):
            if path.name != "_generic.md" and path.stem not in ids:
                fail(path.relative_to(root), "guide has no entry in .dayzero/stacks/detect.json")

    md_files = sorted(dz.rglob("*.md")) + [root / "README.md"]
    for path in md_files:
        if not path.exists():
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if EM_DASH in line:
                fail(path.relative_to(root), f"line {n}: em dash")

    if errors:
        print(f"DayZero validation failed ({len(errors)} problems):")
        for e in errors:
            print(f"  {e}")
        return 1
    print("DayZero validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
