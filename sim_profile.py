import os
import cProfile as prof
import pstats

from simulation import _default_inst

os.environ["RGB_SIM"] = "true"
os.environ["RGB_NT_SIM"] = "true"

from main import update, DELAY

_default_inst.getTable("GameInfo").putValue("stage", "disabled")

def run_a_bunch():
    frame = 0
    for _ in range(1000):
        update(1/10, frame)
        frame += 1
        frame %= 1_000_000

profiler = prof.Profile()
profiler.runcall(run_a_bunch)

res = pstats.Stats(profiler)
res.sort_stats("time", "name").print_stats()