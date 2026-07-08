import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def solution(image, mask):
    """
    이미지를 나타내는 넘파이 배열 image와 마스크를 나타내는 넘파이 배열 mask가 주어졌을 때,
    마스크에 해당하는 이미지 영역만 살리고 나머지는 0으로(검은색으로) 만드는 코드를 작성하세요.

    이때, 이미지 배열과 마스크 배열은 모두 (H, W) 모양입니다.
    이미지 배열은 0~255 사이 자연수로 구성되며, 마스크 배열은 0 아니면 255 값이 담긴 배열입니다.
    마스크 배열을 255로 나누어 값이 255인 원소를 1로 만들고 이미지와 곱하면 됩니다.

    인자:
        - image: 이미지를 담은 (H, W) 차원의 넘파이 배열
        - mask: 0 또는 255 값으로만 구성된 마스크를 표현하는 (H, W) 차원의 넘파이 배열

    반환값:
        - image: 마스킹된 이미지

    예상출력:
        파일 실행 후, resources/ 폴더 내에 q10_test1.jpg, q10_test2.jpg, q10_test3.jpg 파일을 확인해보세요.
        세 파일이 각각 q10_test1_truth.jpg, q10_test2_truth.jpg, q10_test3_truth.jpg 와 같으면 됩니다.
    """

    image = image.astype(np.float32)
    mask = mask.astype(np.float32)
    
    # ----- your code here -----
    image = image * (mask / 255)

    # --------------------------

    image = image.astype(np.uint8)
    return image


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("L")

    image1 = np.array(image) + 0 # + 0 지우지마세요. 깊은 복사 효과를 위해 넣었습니다.
    H, W = image1.shape[:2]
    mask1 = Image.open(os.path.join(root_dir, "resources", "truth", "q9_test1_truth.jpg")).convert("L")
    mask1 = np.array(mask1)
    Image.fromarray(solution(image1, mask1)).save(os.path.join(root_dir, "resources", "q10_test1.jpg"))
    
    image2 = np.array(image) + 0 # + 0 지우지마세요.  깊은 복사 효과를 위해 넣었습니다.
    H, W = image2.shape[:2]
    mask2 = Image.open(os.path.join(root_dir, "resources", "truth", "q9_test2_truth.jpg")).convert("L")
    mask2 = np.array(mask2)
    Image.fromarray(solution(image2, mask2)).save(os.path.join(root_dir, "resources", "q10_test2.jpg"))
    
    image3 = np.array(image) + 0 # + 0 지우지마세요.  깊은 복사 효과를 위해 넣었습니다.
    H, W = image3.shape[:2]
    mask3 = Image.open(os.path.join(root_dir, "resources", "truth", "q9_test3_truth.jpg")).convert("L")
    mask3 = np.array(mask3)
    Image.fromarray(solution(image3, mask3)).save(os.path.join(root_dir, "resources", "q10_test3.jpg"))
