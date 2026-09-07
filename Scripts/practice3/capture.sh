#!/bin/bash
set -u
source ~/lab/venv/bin/activate
OUT=/tmp/caps
mkdir -p $OUT

echo "########## Q09 BUILD ##########" 
cd ~/lab/q09
python -m build --wheel --sdist > $OUT/q09_build.log 2>&1
ls -1 $OUT/q09_build.log && tail -6 $OUT/q09_build.log
echo "---- artifacts ----"
ls -1 dist/

echo "########## Q09 INSTALL+RUN ##########"
/usr/bin/python3 -m venv ~/lab/q09_cleanenv >/dev/null 2>&1
~/lab/q09_cleanenv/bin/pip install -q dist/greetlab_25020007191-0.1.0-py3-none-any.whl
~/lab/q09_cleanenv/bin/sdt-greet --name 25020007191

echo "########## Q10 TEST FAIL ##########"
cd ~/lab/q10
~/lab/venv/bin/pytest -q > $OUT/q10_fail.log 2>&1; echo "pytest rc=$? (expect 1)"
tail -8 $OUT/q10_fail.log
echo "---- baseline commit ----"
git log --oneline -3

echo "########## Q10 TEST PASS ##########"
~/lab/venv/bin/pytest -q > $OUT/q10_pass.log 2>&1; echo "pytest rc=$? (expect 0)"
tail -4 $OUT/q10_pass.log
echo "---- ai_log.md ----"
cat ai_log.md

echo "########## Q11 communication.md chars ##########"
wc -m communication.md

echo "########## Q12 TRAIN ##########"
cd ~/lab/q12
source ~/lab/venv/bin/activate
python train.py

echo "########## P3 LSP ##########"
cd ~/lab/practice3
python lsp_client.py > $OUT/p3_lsp.log 2>&1; echo "lsp rc=$?"
cat $OUT/p3_lsp.log

echo "########## P3 VIM MODE ##########"
bash -c 'set -o vi; set -o | grep -E "^(vi|emacs)"'

echo "########## P3 VIMGOLF ##########"
vim -n -u NONE -i NONE -s golf_keys.vim golf_start.txt >/dev/null 2>&1
if diff -q golf_start.txt golf_expected.txt >/dev/null; then echo "VIMGOLF PASS (output matches)"; else echo "VIMGOLF FAIL"; fi

echo "########## P3 ALIGN PLUGIN ##########"
printf 'x=1\nyyy=22\nzz=333\n' > /tmp/align2.txt
printf ':1,3Align =\n:x\n' > /tmp/align2_keys.vim
vim -n -u NONE -i NONE -c 'set nocp' -c 'runtime plugin/AlignPlugin.vim' -s /tmp/align2_keys.vim /tmp/align2.txt >/dev/null 2>&1
echo "before: x=1 / yyy=22 / zz=333  ; after:"
sed -n '1,3p' /tmp/align2.txt
ls ~/.vim/plugin/

echo "########## DONE ##########"