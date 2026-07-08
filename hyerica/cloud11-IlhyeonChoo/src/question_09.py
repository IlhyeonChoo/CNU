import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def solution(image, x1, y1, x2, y2):
    """
    흑백이미지를 표현하는 넘파이 배열 image가 주어졌을 때, image와 그 크기와 모양이 같으면서, 특정 영역(x1, y1, x2, y2로 표현되는)만 값이 255이고,
    나머지는 값이 0인 넘파이 배열(mask)을 만드세요. 이때, image의 모양은 (H, W) 입니다(흑백이미지이기 때문에, 뒤에 3이 없습니다).
    이때, 생성할 넘파이 배열 mask의 자료형은 "uint8"로 지정하여 생성하세요.

    참고:
        - 데이터의 특정 영역을 표현하기 위해, 데이터와 크기가 같으면서, 일부 영역만 값이 1이거나 255이고, 
          이외 영역은 값이 0인 바이너리 배열(0 또는 1, 0 또는 255 두 개의 수로만 구성된)을 mask 라고 부릅니다.

    인자:
        - image: (H, W) 차원의 넘파이 배열
        - x1: 영역의 가로 시작점
        - y1: 영역의 세로 시작점
        - x2: 영역의 가로 종점
        - y2: 영역의 세로 종점
    반환값:
        - mask: 특정 영역만 1이고 나머지는 0인 이미지 마스크( (H, W) 차원의 넘파이 배열)

    예상출력:
        파일 실행 후, resources/ 폴더 내에 q9_test1.jpg, q9_test2.jpg, q9_test3.jpg 파일을 확인해보세요.
        세 파일이 각각 q9_test1_truth.jpg, q9_test2_truth.jpg, q9_test3_truth.jpg 와 같으면 됩니다.
    """
    
    # ----- your code here -----
    mask = np.zeros_like(image, dtype=np.uint8)
    mask[y1:y2, x1:x2] = 255

    # --------------------------
    return mask


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("L")
    image = np.array(image) + 0 # + 0 지우지마세요

    H, W = image.shape[:2]

    Image.fromarray(solution(image, 0, 0, W//2, H//2)).save(os.path.join(root_dir, "resources", "q9_test1.jpg"))
    Image.fromarray(solution(image, W//2, 0, W, H)).save(os.path.join(root_dir, "resources", "q9_test2.jpg"))
    Image.fromarray(solution(image, int(W*0.25), int(H*0.25), int(W*0.75), int(H*0.75))).save(os.path.join(root_dir, "resources", "q9_test3.jpg"))
