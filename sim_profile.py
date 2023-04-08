import os
import cProfile as prof
import pstats

os.environ["RGB_SIM"] = "true"

from main import update, DELAY

def run_a_bunch():
    for _ in range(1000):
        update(1/10)

profiler = prof.Profile()
profiler.runcall(run_a_bunch)

res = pstats.Stats(profiler)
res.sort_stats("time", "name").print_stats()