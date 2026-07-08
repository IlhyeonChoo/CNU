import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from collections import deque
from question_19 import temperature_generator, run

def test():
    logs = deque()
    simulation_time = 4
    run(logs, simulation_time)
    assert len(logs) == 3
    assert type(logs[0]) == float