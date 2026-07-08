import os
import numpy as np
from PIL import Image


def solution(image):
    """
    이미지가 (H, W, 3) 모양의 넘파이 배열로 주어졌을 때, 이미지의 R, G, B 채널을 분리하여 반환하는 코드를 작성하세요.
    이때, 이미지의 가로, 세로 길이는 W, H이며, 이미지를 구성하는 픽셀 하나는 3개의 값(빨강, 초록, 파랑 색상값)으로 이루어집니다.

    이미지로부터, 빨강 색상만 분리한 (H, W) 모양의 넘파이 배열,
    초록 색상만 분리한 (H, W) 모양이 넘파이 배열,
    파랑 색상만 분리한 (H, W) 모양이 넘파이 배열,

    이 새 가지 배열을 반환하세요.

    인자:
        - image: (H, W, 3) 모양의 넘파이 배열
    반환값:
        - red: (H, W) 모양의 넘파이 배열
        - green: (H, W) 모양의 넘파이 배열
        - blue: (H, W) 모양의 넘파이 배열

    예상출력:
        파일 실행 후, resources/ 폴더 내에 q6_red_intensity.jpg, q6_green_intensity.jpg, q6_blue_intensity.jpg 파일을 확인해보세요.
        세 파일이 각각 q6_red_intensity_truth.jpg, q6_green_intensity_truth.jpg, q6_blue_intensity_truth.jpg 와 같으면 됩니다.

    참고: 세 파일을 확인해보면, 붉은색이나 푸른색 없이 다 흑백이미지로 나오는 것을 확인할 수 있습니다.
         이는, 세 파일이 실제 색상을 저장한 것이 아니라, 각 색상의 세기(intensity) 값들을 저장했기 때문입니다.
         예를들어, q6_red_intensity.jpg를 확인할 경우, 원본이미지(color.png) 에서 붉은 부분 영역이 흰색으로 변한 것을 확인할 수 있고,
         q6_green_intensity의 경우, 초록 부분이 밝은 색으로 표현된 것을 확인할 수 있습니다. 세기(intensity) 값을 흑백이미지로 저장할 경우,
         세기가 강한 부분은 밝은 색으로 저장되기 때문입니다.
    """
    
    # ----- your code here -----
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    # --------------------------
    return red, green, blue


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "color.png")).convert("RGB")
    image = np.array(image)

    r, g, b = solution(image)
    Image.fromarray(r).save(os.path.join(root_dir, "resources", "q6_red_intensity.jpg"))
    Image.fromarray(g).save(os.path.join(root_dir, "resources", "q6_green_intensity.jpg"))
    Image.fromarray(b).save(os.path.join(root_dir, "resources", "q6_blue_intensity.jpg"))
