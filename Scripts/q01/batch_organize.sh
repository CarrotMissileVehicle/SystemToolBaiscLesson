#!/bin/bash

# 批量整理含空格文件名的脚本
# 功能：将当前目录下文件名中的空格替换为下划线

echo "=== 含空格文件名批量整理脚本 ==="
echo "当前目录: $(pwd)"
echo ""

# 统计含空格的文件数量
count=0
for file in *; do
    if [[ "$file" == *" "* ]]; then
        count=$((count + 1))
    fi
done

echo "发现 $count 个包含空格的文件"
echo ""

if [ $count -eq 0 ]; then
    echo "没有需要处理的文件"
    exit 0
fi

# 处理包含空格的文件
echo "开始重命名文件..."
for file in *; do
    if [[ "$file" == *" "* ]]; then
        # 将空格替换为下划线
        new_name="${file// /_}"
        echo "重命名: \"$file\" -> \"$new_name\""
        mv "$file" "$new_name"
    fi
done

echo ""
echo "整理完成！"
echo ""

# 显示整理后的文件列表
echo "整理后的文件列表:"
ls -la