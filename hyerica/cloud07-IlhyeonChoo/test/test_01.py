import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_01 import calculate_mean, calculate_std


def test_solution():
    mean = calculate_mean(100, 85, 81, 93)
    std = calculate_std(100, 85, 81, 93)
    assert abs(mean - 89.75) < 1e-4 and abs(std - 7.327175444876422) < 1e-4

    mean = calculate_mean(100, 85, 81, 93, 13, 413)
    std = calculate_std(100, 85, 81, 93, 13, 413)
    assert abs(mean - 130.83333333333334) < 1e-4 and abs(std - 129.40172160970482) < 1e-4

    mean = calculate_mean(314, 81, 61, 13, 413)
    std = calculate_std(314, 81, 61, 13, 413)
    assert abs(mean - 176.4) < 1e-4 and abs(std - 157.49996825396505) < 1e-4

    mean = calculate_mean(91324, 81, 5161, 13, 413)
    std = calculate_std(91324, 81, 5161, 13, 413)
    assert abs(mean - 19398.4) < 1e-4 and abs(std - 36014.987389141206) < 1e-4

    mean = calculate_mean(314, 235, 81, 61, 13, 413)
    std = calculate_std(314, 235, 81, 61, 13, 413)
    assert abs(mean - 186.16666666666666) < 1e-4 and abs(std - 145.4262890799169) < 1e-4


