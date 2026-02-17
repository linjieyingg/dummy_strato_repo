"""
CI script: detect changed Python files and generate tests via Gemini.
Skips files that already have up-to-date tests.
"""

import os
import subprocess
import re
import time
import random
import google.generativeai as genai
from pathlib import Path

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("No GEMINI_API_KEY set, skipping test generation")
    exit(0)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Directories to scan for changed source files
SOURCE_DIRS = ["src/"]
TESTS_DIR = Path("tests/")
TESTS_DIR.mkdir(exist_ok=True)


def get_changed_files() -> list[str]:
    """Get Python files changed in the last commit."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    )
    return [
        f for f in result.stdout.strip().splitlines()
        if f.endswith(".py")
        and any(f.startswith(d) for d in SOURCE_DIRS)
        and not f.endswith("__init__.py")
    ]


def get_test_path(source_path: str) -> Path:
    """Map src/foo/bar.py -> tests/test_bar.py"""
    name = Path(source_path).stem
    return TESTS_DIR / f"test_{name}.py"


def generate_tests(file_path: str, source_code: str) -> str:
    """Ask Gemini to write pytest tests for the given source file."""
    prompt = f"""Write pytest unit tests for this Python file.

File: {file_path}
```python
{source_code}
```

Requirements:
- Use pytest
- Import from the correct module path (e.g. from src.foo.bar import ...)
- Test normal cases, edge cases, and error cases
- Use descriptive test function names
- No mocking of external APIs (Gemini, GitHub) — skip those functions
- Return ONLY the Python test code, no explanation
"""

    for attempt in range(4):
        try:
            response = model.generate_content(prompt)
            raw = response.text.strip()
            # Strip markdown fences if present
            if "```" in raw:
                parts = re.split(r"```(?:python)?", raw)
                for part in parts:
                    if "import" in part or "def test_" in part:
                        return part.strip().strip("`\n\r ")
            return raw
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                wait = (15 * (2 ** attempt)) + random.uniform(1, 3)
                print(f"Rate limited, waiting {wait:.1f}s...")
                time.sleep(wait)
            else:
                print(f"Gemini error for {file_path}: {e}")
                return None
    return None


def main():
    changed = get_changed_files()

    if not changed:
        print("No changed source files detected.")
        return

    print(f"Changed files: {changed}")

    for source_path in changed:
        if not Path(source_path).exists():
            print(f"Skipping deleted file: {source_path}")
            continue

        test_path = get_test_path(source_path)

        with open(source_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        if not source_code.strip():
            print(f"Skipping empty file: {source_path}")
            continue

        print(f"Generating tests for {source_path} -> {test_path}")
        tests = generate_tests(source_path, source_code)

        if tests:
            with open(test_path, "w", encoding="utf-8") as f:
                f.write(tests + "\n")
            print(f"  Written: {test_path}")
        else:
            print(f"  Skipped: could not generate tests")


if __name__ == "__main__":
    main()