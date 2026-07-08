import numpy as np

def mean_subtract_channels(img):
    """
    주어진 RGB 이미지 배열에서 각 채널(R, G, B)의 평균값을 계산하고,
    각 픽셀에서 해당 채널의 평균을 뺀 정규화된 이미지를 반환하는 함수를 작성하세요.
    이 연산은 이미지 데이터 전처리 과정에서 사용되는 채널 정규화 방식입니다.
    각 채널의 평균을 계산한 뒤, 해당 평균을 각 채널 위치에 빼주는 방식입니다.
    - 인자:
        - img (np.ndarray): 2x2x3 이미지 배열 (0~255 정수값)
    - 반환값:
        - np.ndarray:  2x2x3 크기의 이미지 배열
    - 출력 예시:
        >>> result = mean_subtract_channels(img_array)
        >>> [[[-25.   25.  112.5]
              [-75.  -75.  -37.5]]
             [[ 25.   75.   12.5]
              [ 75.  -25.  -87.5]]]
    """
    # ----- your code here -----
    channel_means = img.mean(axis=(0, 1))
    return img - channel_means
    # --------------------------

if __name__ == "__main__":
    img_array = np.array([[[100, 150, 200], [50, 50, 50]],
                          [[150, 200, 100], [200, 100, 0]]])

    result = mean_subtract_channels(img_array)
    print(result)