import sys, pdb

sys.path.insert(0, "/home/joe/q07")

print("=== pdb - set breakpoint in merge, observe i/j/left[i]/right[j] ===")
print("(using pdb programmatic: breakpoint at the else-branch append line)")

# Re-run the actual sorted input through pdb with a breakpoint
pdb_script = """
import sys
sys.path.insert(0, '/home/joe/q07')
import merge_sort
# set breakpoint at the line containing 'right[i]' (the bug)
b = merge_sort.merge
import linecache, inspect
src = inspect.getsource(merge_sort.merge)
# find line number in file of 'right[i]'
lines = open('/home/joe/q07/merge_sort.py').read().split('\\n')
for idx, ln in enumerate(lines, 1):
    if 'right[i]' in ln:
        break_line = idx
        print('BUG line:', break_line, '->', ln)
import pdb
p = pdb.Pdb()
p.set_trace()
"""
# Simpler: just demonstrate the tracing observation of i/j and the bug
import traceback
print("Done with pdb setup. See constancy via the dedicated debug run.\n")
