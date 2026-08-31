#!/usr/bin/env bash
# analyze.sh - 第2题：随机访问日志统计
# 用法: ./analyze.sh <csv文件路径>
# 输出: 5xx次数最多的前2个path(按次数降序,相同按path字典序) + 平均latency_ms(两位小数)

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "usage: $0 <csv-path>" >&2
    exit 2
fi

CSV="$1"

if [ ! -f "$CSV" ]; then
    echo "error: no such file: $CSV" >&2
    exit 3
fi

echo "== top 2 paths by 5xx count =="
awk -F, 'NR>1 && $4 ~ /^5[0-9][0-9]$/ {print $3}' "$CSV" \
    | sort | uniq -c | sort -k1,1nr -k2,2 \
    | head -2 \
    | awk '{printf "%d %s\n", $1, $2}'

echo "== average latency (ms) =="
awk -F, 'NR>1 {sum += $5; n++} END { if (n>0) printf "%.2f\n", sum/n }' "$CSV"
