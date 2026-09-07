核心提示：q10 的 greetlab 缺陷——`--name` 仅含空白字符时仍输出问候并以0退出；目标：使 main 以 SystemExit(2) 结束；约束：只修改实现、不改变正常姓名行为；测试命令 `~/lab/venv/bin/python -m pytest test_cli.py -v`。
智能体改动：在 `cli.py` 的 `parse_args()` 后新增 `if not a.name.strip(): p.error("name must not be blank")`，共2行，并自测通过。
人工验证：检查 `git diff`，撤销无关改动（`__pycache__/` 字节码缓存，已加入 .gitignore 并从索引移除），确认 diff 仅含 cli.py。
复测：`~/lab/venv/bin/python -m pytest test_cli.py -v` 通过。
正常行为回归：`sdt-greet --name 25020007191` 仍输出 `Hello, 25020007191!`，退出码0。