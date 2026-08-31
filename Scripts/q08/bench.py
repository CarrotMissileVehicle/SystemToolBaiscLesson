import subprocess
import time
import sys


def run(file):
    t0 = time.perf_counter()
    subprocess.run([sys.executable, file, "words.txt"], check=True)
    return time.perf_counter() - t0


SLOW = 5
FAST = 5


def median(xs):
    s = sorted(xs)
    n = len(s)
    if n % 2:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


slow_times = []
for _ in range(SLOW):
    slow_times.append(run("wordfreq.py"))
fast_times = []
for _ in range(FAST):
    fast_times.append(run("wordfreq_fast.py"))

slow_med = median(slow_times)
fast_med = median(fast_times)
print("slow version raw:", [f"{t:.3f}" for t in slow_times])
print("fast version raw:", [f"{t:.3f}" for t in fast_times])
print(f"SLOW median = {slow_med:.3f}s")
print(f"FAST median = {fast_med:.3f}s")
print(f"speedup ratio = {slow_med / fast_med:.1f}x")
