import sys, pdb

sys.path.insert(0, "/home/joe/q07")

BUF = __import__("io").StringIO
OUT = __import__("sys").stdout

results = []
def run_pdb():
    p = pdb.Pdb()
    # 把命令放入 pdb 的命令队列：先在缺陷行(第8行, 含 right[i])设断点
    p.cmdqueue.extend([
        "break /home/joe/q07/merge_sort.py:8",
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
    except Exception as e:
        # quit 会抛 BdbQuit
        if not isinstance(e, pdb.bdb.BdbQuit):
            print("err", type(e).__name__, e)

if __name__ == "__main__":
    run_pdb()
