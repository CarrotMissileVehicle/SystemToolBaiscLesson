#!/bin/bash
set -u
printf 'a=1\nbcd=22\nef=333\n' > /tmp/align_in.txt
printf ':1,3Align =\n:x\n' > /tmp/align_keys.vim
vim -n -u NONE -i NONE -c 'set nocp' -c 'runtime plugin/AlignPlugin.vim' -c 'echo "Align loaded: ".exists(":Align")' -s /tmp/align_keys.vim /tmp/align_in.txt >/dev/null 2>&1
echo '--- after :1,3Align = ---'
cat -A /tmp/align_in.txt