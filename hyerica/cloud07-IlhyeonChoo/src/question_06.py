def is_valid_path(path):
    """
    파일시스템에 .png 파일만 있고, .jpg 파일은 없다고 가정한 함수입니다.
    """
    return path.endswith(".png")


def preprocess_data(data_list):
    """
    이미지 데이터 경로와 그 이미지가 어떤 이미지인지에 대한 카테고리로 이루어진 리스트 data_list가 주어졌을 때, 
    이 데이터들 중 유효한 경로를 가진 데이터만 골라내는 코드를 작성하세요.
    이때, data_list의 원소 하나(데이터 하나)는 경로와 카테고리를 담은 튜플이며 다음처럼 구성됩니다.
        data_list = [("data/a/a.png", "dog"), ("data/a/b.png", "dog"), ...]
    여기서, 각 데이터의 경로가 유효한 데이터만 추출하여 preprocessed_data_list로 만드세요.
    "경로가 유효하다"라는 의미는, 파일시스템(디스크)에 해당 경로로 된 파일이 존재한다 라는 의미입니다.
    
    데이터 경로가 유효한지는 판단하는 것은 위에 정의된 is_valid_path 함수를 사용하세요.
    is_valid_path는 데이터 경로를 입력받아, 유효한 경로이면 True를, 유효하지 않은 경로이면 False를 반환하는 함수입니다.

    for 문 대신 filter 함수를 이용하세요.

    인자:
    - data_list: [("data/a/a.png", "dog"), ("data/a/b.png", "dog"), ...] 형식의 리스트

    반환값:
    - preprocessed_data_list: 유효하지 않은 경로 데이터가 제거된 데이터리스트
    """

    # ----- Your code here -----
    preprocessed_data_list = list(
        filter(lambda data: is_valid_path(data[0]), data_list)
    )
    # --------------------------

    return preprocessed_data_list


if __name__ == "__main__":
    """
    예상출력:
        [('data/a/a1.png', 'dog'), ('data/a/a2.png', 'cat'), ('data/a/a3.png', 'tiger'), ('data/a/a4.png', 'dog')]
        [('data/b/b1.png', 'dog'), ('data/b/b2.png', 'cat')]
        [('data/c/c2.png', 'cat'), ('data/c/c3.png', 'tiger')]
    """
    
    data_list = [
        ("data/a/a1.png", "dog"),
        ("data/a/a2.png", "cat"),
        ("data/a/a3.png", "tiger"),
        ("data/a/a4.png", "dog"),
    ]
    print(preprocess_data(data_list))
    
    data_list = [
        ("data/b/b1.png", "dog"),
        ("data/b/b2.png", "cat"),
        ("data/b/b3.jpg", "tiger"),
        ("data/b/b4.jpg", "dog"),
    ]
    print(preprocess_data(data_list))
    
    data_list = [
        ("data/c/c1.jpg", "dog"),
        ("data/c/c2.png", "cat"),
        ("data/c/c3.png", "tiger"),
        ("data/c/c4.jpeg", "dog"),
    ]
    print(preprocess_data(data_list))
