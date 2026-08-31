#!/usr/bin/env bash
# batch_organize.sh - 第1题：含空格文件名的批量整理
# 在q01中创建目录/文件，复制.txt到work/，设权限，生成inventory.txt

set -euo pipefail
STUDENT_ID="25020007191"
BASE="$(pwd)"

echo "=== 创建目录结构 ==="
mkdir -p "$BASE/input/docs" "$BASE/input/tmp"

echo "=== 创建测试文件 ==="
printf 'alpha\nbeta\n' > "$BASE/input/docs/notes one.txt"
printf 'hidden\n'      > "$BASE/input/docs/.secret.txt"
touch "$BASE/input/tmp/empty.txt"
printf 'line1: boot ok\nline2: ssh ok\n' > "$BASE/input/run.log"

echo "=== q01 绝对路径 ==="
readlink -f "$BASE"

echo "=== ls -la input（含隐藏文件）==="
ls -la "$BASE/input"

echo "=== 复制 .txt 文件到 work/$STUDENT_ID（保留相对目录结构）==="
mkdir -p "$BASE/work/$STUDENT_ID"
cd "$BASE/input" && find . -name '*.txt' -exec cp --parents {} "$BASE/work/$STUDENT_ID/" \;

echo "=== 设置权限：目录750，文件640 ==="
find "$BASE/work/$STUDENT_ID" -type d -exec chmod 750 {} +
find "$BASE/work/$STUDENT_ID" -type f -exec chmod 640 {} +

echo "=== 生成 inventory.txt ==="
cd "$BASE/work/$STUDENT_ID"
find . -type f ! -name inventory.txt -printf '%P %s\n' | sort > inventory.txt

echo "=== inventory.txt 内容 ==="
cat inventory.txt

echo "=== 最终目录结构 ==="
find "$BASE" -type f -o -type d | sort
