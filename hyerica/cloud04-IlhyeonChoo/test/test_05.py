import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_05 import preprocess_data

def test_path_join():
    date_list = ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"]
    weather_list = ["Sunny", "SUNNY", "cloudy", "Cloudy"]
    preprocessed_data = preprocess_data(date_list, weather_list)
    single_case_test(preprocessed_data, ["sunny", "sunny", "cloudy", "cloudy"])

    date_list = ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"]
    weather_list = ["RAINY", "rainy", "cloudy", "CLOUDY"]
    preprocessed_data = preprocess_data(date_list, weather_list)
    single_case_test(preprocessed_data, ["rainy", "rainy", "cloudy", "cloudy"])

    date_list = ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"]
    weather_list = ["SUNNY", "SUNNY", "CLOUDY", "Cloudy"]
    preprocessed_data = preprocess_data(date_list, weather_list)
    single_case_test(preprocessed_data, ["sunny", "sunny", "cloudy", "cloudy"])


def single_case_test(preprocessed_data, target_weather):
    assert len(preprocessed_data["Date"]) == len(preprocessed_data["Weather"])
    assert_equal_list(preprocessed_data["Weather"], target_weather)


def assert_equal_list(lst1, lst2):
    assert len(lst1) == len(lst2)
    for i1, i2 in zip(lst1, lst2):
        assert i1 == i2
    


test_path_join()