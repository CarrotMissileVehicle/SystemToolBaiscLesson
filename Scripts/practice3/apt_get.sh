#!/bin/bash
set -u
echo 'Zyj@070505' | sudo -S apt-get install -y vim-scripts vim-addon-manager >/tmp/apt.log 2>&1
RC=$?
tail -5 /tmp/apt.log
echo "APT_RC=$RC"
echo '--- vim version ---'
vim --version | head -3
echo '--- addons available ---'
list=$(vim-addon-manager list 2>/dev/null)
echo "$list" | head -40