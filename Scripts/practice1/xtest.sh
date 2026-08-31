#!/usr/bin/env bash
# 演示 set -x: 打印每条被执行的命令
set -x
whoami
echo "hello, current user is $(whoami)"
set +x
echo "done"
