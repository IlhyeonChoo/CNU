import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_06 import Character


def test_solution():
    names = ["Jane", "Henry", "Robert", "David", "Rose"]
    positions = [(0, 0), (100, 100), (50, 100), (20, 25), (25, 30)]
    hps = [100, 80, 90, 70, 70]

    for name, position, hp in zip(names, positions, hps):
        character = Character(name, position, hp)
        assert hasattr(character, "name")
        assert hasattr(character, "position")
        assert hasattr(character, "hp")
        assert character.name == name
        assert character.position == position
        assert character.hp == hp


