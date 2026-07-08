import numpy as np

def mean_of_filtered_pixels(img):
    """
    주어진 2x2 이미지 배열에서 128 이상인 픽셀 값들의 평균을 계산하여 반환하는 함수를 작성하세요.
    특정 조건을 만족하는 값만 골라 평균을 계산하는 마스킹 연산입니다.
    2x2 이미지 배열을 넘파이 배열로 변한하여 계산하세요.
    - 인자:
        - img (List): 0~255 범위의 2x2 이미지 배열
    - 반환값:
        - float: 조건을 만족하는 픽셀 값들의 평균
    - 출력 예시:
        >>> mean_of_filtered_pixels(img)
        >>> 167.5
    """
    # ----- your code here -----
    img = np.array(img)
    return img[img >= 128].mean()
    # --------------------------

if __name__ == "__main__":
    img_array = [[120, 135], 
                 [200, 90]]
    result = mean_of_filtered_pixels(img_array)
    print("128 이상인 픽셀 평균:", result)