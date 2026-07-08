import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

import numpy as np
from question_04 import standardize


def test_solution():
    assert np.abs(np.array(standardize(100, 85, 81, 93)) - np.array([1.3989019475666278, -0.6482716342381933, -1.1941845893861458, 0.44355427605771125])).max() < 1e-4
    assert np.abs(np.array(standardize(100, 85, 81, 93, 13, 413)) - np.array([-0.23827606734886683, -0.35419415416723443, -0.3851056439854658, -0.2923711745307717, -0.910600970895399, 2.1805480109277373])).max() < 1e-4
    assert np.abs(np.array(standardize(314, 81, 61, 13, 413)) - np.array([0.8736509697457411, -0.6057144078033699, -0.7326985603826928, -1.0374605265730676, 1.5022225250133892])).max() < 1e-4
    assert np.abs(np.array(standardize(0.31, 0.51, 1.23, -13.1, -2.3)) - np.array([0.5569858000323817, 0.5943673973499912, 0.7289411476933855, -1.949450300113336, 0.06915595503757761])).max() < 1e-4
    assert np.abs(np.array(standardize(5.13, 6.13, 4.51, 3.45, 8.123)) - np.array([-0.2133690925994132, 0.41678180107871116, -0.6040626466798504, -1.272022593978662, 1.6726725321792126])).max() < 1e-4
