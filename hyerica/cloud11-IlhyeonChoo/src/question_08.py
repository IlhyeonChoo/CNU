import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def solution(image, x1, y1, x2, y2):
    """
    이미지의 특정 영역을 검은색으로 만드는 코드를 작성하세요.
    이미지를 표현하는 넘파이 배열 image에서, 슬라이싱을 통해 특정 영역의 뷰(view)를 가저온 후, 해당 뷰에 0을 대입하면 해당 영역이 검은색으로 변합니다.

    인자:
        - image: (H, W, 3) 모양의 넘파이 배열
        - x1: 영역의 가로 시작점
        - y1: 영역의 세로 시작점
        - x2: 영역의 가로 종점
        - y2: 영역의 세로 종점
    반환값:
        - 없음

    예상출력:
        파일 실행 후, resources/ 폴더 내에 q8_test1.jpg, q8_test2.jpg, q8_test3.jpg 파일을 확인해보세요.
        세 파일이 각각 q8_test1_truth.jpg, q8_test2_truth.jpg, q8_test3_truth.jpg 와 같으면 됩니다.

    참고:
        총 세 개의 이미지가 만들어지는데, 나중에 만들어진 이미지에는 이전에 만들어진 이미지에 적용된 마스크도 같이 적용되어 있습니다.
        그 이유가 무엇일지 생각해보시길 바랍니다.
    """

    # ----- your code here -----
    image[y1:y2, x1:x2] = 0

    # --------------------------
    return image


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("RGB")
    image = np.array(image) + 0 # + 0 지우지마세요

    H, W = image.shape[:2]

    Image.fromarray(solution(image, 0, 0, W//2, H//2)).save(os.path.join(root_dir, "resources", "q8_test1.jpg"))
    Image.fromarray(solution(image, W//2, 0, W, H)).save(os.path.join(root_dir, "resources", "q8_test2.jpg"))
    Image.fromarray(solution(image, int(W*0.25), int(H*0.25), int(W*0.75), int(H*0.75))).save(os.path.join(root_dir, "resources", "q8_test3.jpg"))
