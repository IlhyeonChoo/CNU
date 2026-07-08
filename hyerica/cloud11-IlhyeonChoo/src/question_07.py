import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def solution(image, x1, y1, x2, y2):
    """
    (H, W, 3) 모양의 넘파이 배열로 이미지가 주어졌을 때, 이 이미지를 가로로 x1부터 x2까지, 세로로 y1부터 y2까지 자르는 코드를 작성하세요.
    이미지를 자르는 것은 넘파이 배열을 자르는 것과 같으며, 인덱스 슬라이싱을 이용하면 됩니다.
    배열을 자를 때, x축의 x1, y축의 y1 좌표는 포함하지만, x2, y2는 포함하지 않습니다.

    이미지를 표현한 넘파이 배열의 첫 번째 축은 세로, 두 번째 축이 가로라는 것을 유의하세요(행렬이기 때문에, 첫 번째 축이 "행" 축입니다).

    인자:
        - image: (H, W, 3) 모양의 넘파이 배열
        - x1: 가로로 자르는 시작점
        - y1: 세로로 자르는 시작점
        - x2: 가로로 자르는 종점
        - y2: 세로로 자르는 종점
    반환값:
        - (y2-y1, x2-x1, 3) 모양의 넘파이 배열

    예상출력:
        파일 실행 후, resources/ 폴더 내에 q7_test1.jpg, q7_test2.jpg, q7_test3.jpg 파일을 확인해보세요.
        세 파일이 각각 q7_test1_truth.jpg, q7_test2_truth.jpg, q7_test3_truth.jpg 와 같으면 됩니다.
    """
    
    # ----- your code here -----
    return image[y1:y2, x1:x2]

    # --------------------------


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("RGB")
    image = np.array(image)

    H, W = image.shape[:2]

    Image.fromarray(solution(image, 0, 0, W//2, H//2)).save(os.path.join(root_dir, "resources", "q7_test1.jpg"))
    Image.fromarray(solution(image, W//2, 0, W, H)).save(os.path.join(root_dir, "resources", "q7_test2.jpg"))
    Image.fromarray(solution(image, int(W*0.25), int(H*0.25), int(W*0.75), int(H*0.75))).save(os.path.join(root_dir, "resources", "q7_test3.jpg"))
