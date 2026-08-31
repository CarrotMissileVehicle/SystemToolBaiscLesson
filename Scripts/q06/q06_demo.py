#!/usr/bin/env python3
"""第6题：语义重构演示（用 jedi 模拟 LSP：跳转定义、查找引用、重命名）。"""
import subprocess
import sys
import jedi

BASE = "/home/joe/q06"


def main() -> None:
    # PHASE 1: reset project to the 3 given files
    print("=== PHASE 1: reset 3 project files ===")
    files = {
        "math_utils.py": "def total_price(price: float, count: int) -> float:\n    return price * count\n",
        "app.py": "from math_utils import total_price\nprint(total_price(12.5, 4))\n",
        "test_math_utils.py": (
            "from math_utils import total_price\n"
            "def test_total_price():\n"
            "    assert total_price(12.5, 4) == 50.0\n"
        ),
    }
    for name, src in files.items():
        with open(f"{BASE}/{name}", "w", encoding="utf-8") as h:
            h.write(src)
        print(f"--- {name} ---\n{src}")

    # PHASE 2: LSP jump-to-def & find-references using jedi (LSP engine)
    print("=== PHASE 2: jump-to-def & find-references (jedi) ===")
    with open(f"{BASE}/app.py", encoding="utf-8") as h:
        app_src = h.read()
    s_app = jedi.Script(app_src, path=f"{BASE}/app.py")
    defs = s_app.infer(1, 27)  # the token 'total_price' in 'from math_utils import total_price'
    print("jump-to-def (total_price in app.py):")
    for d in defs:
        print(f"   -> {d.module_path}:{d.line}  {d.name}")

    with open(f"{BASE}/math_utils.py", encoding="utf-8") as h:
        mu_src = h.read()
    s_mu = jedi.Script(mu_src, path=f"{BASE}/math_utils.py")
    refs = s_mu.get_references(1, 4)  # 'total_price' def position
    print("find-references (total_price across project):")
    for r in refs:
        print(f"   {r.module_path}:{r.line}:{r.column}  {r.name}")

    # PHASE 3: rename symbol total_price -> calculate_total
    print("=== PHASE 3: rename total_price -> calculate_total ===")
    jobs = [
        (f"{BASE}/math_utils.py", 1, 4),
        (f"{BASE}/app.py", 1, 27),
        (f"{BASE}/test_math_utils.py", 1, 31),
    ]
    for path, line, col in jobs:
        with open(path, encoding="utf-8") as h:
            src = h.read()
        script = jedi.Script(src, path=path)
        renames = script.rename(line, col, new_name="calculate_total")
        renames.apply()
        print(f"renamed {path.split('/')[-1]}")
    for name in files:
        with open(f"{BASE}/{name}", encoding="utf-8") as h:
            print(f"--- {name} after rename ---\n{h.read()}")

    # PHASE 4: add unused import os -> ruff finds -> remove uses -> ruff pass
    print("=== PHASE 4: nodefault unused import os via ruff ===")
    with open(f"{BASE}/app.py", encoding="utf-8") as h:
        src = h.read()
    with open(f"{BASE}/app.py", "w", encoding="utf-8") as h:
        h.write(f"import os\n{src}")
    rr = subprocess.run(
        ["/home/joe/.local/bin/ruff", "check", "."], cwd=BASE,
        capture_output=True, text=True, check=False,
    )
    print("ruff with unused import (expect F401/X):\n" + (rr.stdout or rr.stderr))
    with open(f"{BASE}/app.py", "w", encoding="utf-8") as h:
        h.write(src)
    rr = subprocess.run(
        ["/home/joe/.local/bin/ruff", "check", "."], cwd=BASE,
        capture_output=True, text=True, check=False,
    )
    print("ruff after removing import os: rc=", rr.returncode, rr.stdout or "(pass)")

    # PHASE 5: final ruff + pytest
    print("=== PHASE 5: final ruff + pytest ===")
    rr = subprocess.run(
        ["/home/joe/.local/bin/ruff", "check", "."], cwd=BASE,
        capture_output=True, text=True, check=False,
    )
    print("ruff rc=", rr.returncode, rr.stdout or "(pass)")
    pr = subprocess.run(
        ["/home/joe/.local/bin/pytest", "test_math_utils.py", "-v"], cwd=BASE,
        capture_output=True, text=True, check=False,
    )
    print(pr.stdout or pr.stderr)
    print("===== ALL DONE =====")


if __name__ == "__main__":
    sys.exit(main())
