import numpy as np


def my_endswith(input_str, query_str):
    if input_str.find(query_str) == -1:
        return False
    elif input_str.find(query_str) + len(query_str) == len(input_str):
        return True
    else:
        return False


if __name__ == "__main__":
    print(my_endswith("Hello, World! world!", "ld!"))
    print(my_endswith("Hello, World! world!", "Hello"))
    print(my_endswith("Hello, World! world!", " Python"))
    v = np.arange(10, dtype="int16").reshape(2, 5)
    print(v)
    v1 = v.reshape(5, 2)
    print(v1)
    v[0, 1] = -1
    print(v1)
    v1[2, 1] = -2
    print(v)
    avg = np.array([84., 92.])
    print(avg)
    print(np.shape(avg))
    avg1 = avg.reshape((2,1))
    avg = avg.reshape(2, 1)
    print(avg)
    print(np.shape(avg))

    print(avg1)
    print(np.shape(avg1))