import numpy as np

def count_pixels_over_threshold(img, threshold):
    """
    주어진 2차원 이미지 배열에서 threshold보다 큰 픽셀의 개수를 반환하세요.
    - 입력값:
        - img (np.ndarray): 2차원 정수형 이미지 배열 (예: 0~255 범위)
        - threshold (int): 픽셀 임계값
    - 반환값:
        - int: threshold보다 큰 픽셀의 개수
    - 출력 예시:
        >>> count_pixels_over_threshold(img_array, 180)
        >>> 4
    """
    # ----- your code here -----
    return int(np.sum(img > threshold))
    # --------------------------

if __name__ == "__main__":
    img_array = np.array([
        [100, 120, 180, 200],
        [210, 250, 90, 80],
        [130, 70, 60, 255]
    ])
    result = count_pixels_over_threshold(img_array, 180)
    print("threshold보다 큰 픽셀 수:", result)