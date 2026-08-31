#!/usr/bin/env bash
# 检查文件（或其它类型路径）是否存在, 用法 ./check.sh <path>
if [ -f "$1" ]; then
    echo "EXISTS (regular file): $1"
else
    echo "MISSING (not a regular file): $1"
fi
