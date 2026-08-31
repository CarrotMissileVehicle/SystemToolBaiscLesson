import sys, pdb

sys.path.insert(0, "/home/joe/practice2")

def run_pdb():
    p = pdb.Pdb()
    p.cmdqueue.extend([
        "break /home/joe/practice2/merge_sort.py:8",
        "continue",
        "p i",
        "p j",
        "p left[i]",
        "p right",
        "continue",
        "p i",
        "p j",
        "p right",
        "quit",
    ])
    try:
        p.run("from merge_sort import merge; print('result=', merge([1,3],[1,4]))")
    except pdb.bdb.BdbQuit:
        pass
    except Exception as e:
        print("err", type(e).__name__, e)

if __name__ == "__main__":
    run_pdb()
