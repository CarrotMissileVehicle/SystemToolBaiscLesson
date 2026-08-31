import sys, pdb

sys.path.insert(0, "/home/joe/q07")
from merge_sort import merge

# DEBUG SESSION: run merge([1,3],[1,4]) with a breakpoint inside merge
# manually reimplement observation by instrumenting via pdb event hooks

print("=== pdb debug: observing merge([1,3],[1,4]) ===")

def traceit(frame, event, arg):
    if event == "line" and frame.f_code.co_name == "merge":
        local = frame.f_locals
        if "i" in local:
            i = local["i"]; j = local["j"]
            left = local["left"]; right = local["right"]
            # only print when about to execute the else/appending line
            co = frame.f_code
            lineno = frame.f_lineno
            if i < len(left) and j < len(right):
                print(f"  [merge] i={i} j={j}  left[i]={left[i]}  right[j]={right[j]}  (line {lineno})")
    return traceit

sys.settrace(traceit)
result = merge([1, 3], [1, 4])
sys.settrace(None)
print("merge([1,3],[1,4]) =", result)
print("expected:", sorted([1,3,1,4]))
