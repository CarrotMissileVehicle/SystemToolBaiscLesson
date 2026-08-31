#!/usr/bin/env bash
# q03_git_conflict.sh - 第3题：从零创建Git仓库，制造并解决一次合并冲突
# 说明：在 q03 目录中执行，用于复现合并冲突的全过程。

set -euo pipefail
DIR="$HOME/q03"

rm -rf "$DIR" && mkdir -p "$DIR"
git -C "$DIR" init -b main
git -C "$DIR" config user.email "zhou@example.com"
git -C "$DIR" config user.name "zhou"

printf 'mode=normal\n' > "$DIR/config.txt"
git -C "$DIR" add config.txt
git -C "$DIR" commit -q -m "init: mode=normal"

# feature-a: mode=safe
git -C "$DIR" checkout -q -b feature-a
printf 'mode=safe\n' > "$DIR/config.txt"
git -C "$DIR" add config.txt
git -C "$DIR" commit -q -m "feature-a: mode=safe"

# feature-b: mode=fast（从初始 main 创建）
git -C "$DIR" checkout -q main
git -C "$DIR" checkout -q -b feature-b main
printf 'mode=fast\n' > "$DIR/config.txt"
git -C "$DIR" add config.txt
git -C "$DIR" commit -q -m "feature-b: mode=fast"

# 回 main，先合并 feature-a，再合并 feature-b（产生冲突）
git -C "$DIR" checkout -q main
git -C "$DIR" merge --no-ff -m "merge feature-a" feature-a
git -C "$DIR" merge feature-b || echo ">>> CONFLICT expected, now resolving"

# 解决冲突：保留 mode=safe，另加 note=reviewed
printf 'mode=safe\nnote=reviewed\n' > "$DIR/config.txt"
git -C "$DIR" add config.txt
git -C "$DIR" commit -q -m "resolve conflict: keep mode=safe, add note=reviewed"

echo "=== worktree clean check ==="
git -C "$DIR" status
echo "=== git log --all --graph --decorate --oneline ==="
git -C "$DIR" log --all --graph --decorate --oneline
