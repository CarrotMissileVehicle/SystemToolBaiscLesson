#!/bin/bash
set -u
grep -q 'set -o vi' ~/.bashrc || echo 'set -o vi' >> ~/.bashrc
touch ~/.inputrc
grep -q 'editing-mode vi' ~/.inputrc || echo 'set editing-mode vi' >> ~/.inputrc
echo '--- .bashrc tail ---'
grep -n 'vi' ~/.bashrc
echo '--- .inputrc ---'
cat ~/.inputrc
echo '--- verification (interactive bash) ---'
BUFF=$(printf 'set -o vi\nset -o | grep -E "vi|emacs"\nexit\n')
echo "$BUFF" | bash -i 2>&1 | grep -E 'vi|emacs' | grep 'on\|off'