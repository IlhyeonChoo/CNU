import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_11 import city_location, get_location

def test():
    C = ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Ulsan']
    L = [(37.56, 126.97), (35.17, 129.07), (37.45, 126.70), (35.87, 128.60), (35.54, 129.31)]

    city_locations = city_location(C, L)
    city, location = get_location(city_locations, 'Daegu')
    assert city == 'Daegu' and location == (35.87, 128.60)