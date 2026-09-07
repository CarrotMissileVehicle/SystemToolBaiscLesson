# communication.md

## Issue

- 环境：Windows、Python 3.13、greetlab 0.1.0（版本待确认）
- 复现命令：`sdt-greet --name " "`（报错待确认）
- 期望结果：空白姓名非零退出码结束、不输出问候
- 实际结果：输出 `Hello, !`，退出码 0

## 提交信息

标题：Reject blank --name with exit code 2

正文：`main()` 未校验空白姓名。修复：`parse_args()` 后调用 `p.error()` 拒绝空白输入（退出码 2）。

## 评审意见

Blocking：`--name " "` 仍输出问候且以 0 退出，空数据会污染下游。请在 `main()` 中校验 `a.name.strip()` 为空时调用 `p.error()`（退出码 2）。