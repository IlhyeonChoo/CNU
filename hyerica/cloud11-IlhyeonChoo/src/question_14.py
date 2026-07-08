import numpy as np


def cosine_similarity_to_query(vectors, query):
    """
    여러 개의 벡터가(vectors) 주어졌을 때, 하나의 기준 벡터(query)와의 코사인 유사도를 계산하는 함수를 작성하세요.
    - 인자:
        - vectors (np.ndarray): (N, D) 크기의 입력 벡터
        - query (np.ndarray): (D,) 크기의 기준 벡터
    - 반환값:
        - np.ndarray: (N,) 크기의 코사인 유사도 배열
    - 힌트:
        - 각 벡터와 기준 벡터의 내적을 계산하세요. (예: [1, 2] · [3, 4] = 1*3 + 2*4 = 11)
        - 각 벡터의 크기(norm)를 계산하세요. (예: ||[3, 4]|| = np.sqrt((3**2 + 4**2)) = 5
        - 기준 벡터(query)의 크기도 계산하세요.
        - 아래 수식을 통해 벡터와 기준 벡터의 코사인 유사도를 구하세요.
        - 수식: cosine_sim(A, q) = (A · q) / (||A|| * ||q||)
    - 출력 예시:
        >>> cosine_similarity_to_query(vectors, query)
        >>> array([0.70710678, 0.70710678, 1.        ])
    """
    # ----- your code here -----
    dot_products = np.sum(vectors * query, axis=1)
    vector_norms = np.sqrt(np.sum(vectors**2, axis=1))
    query_norm = np.sqrt(np.sum(query**2))
    return dot_products / (vector_norms * query_norm)
    # --------------------------


if __name__ == "__main__":
    vector_arr = np.array([[1, 0], [0, 1], [1, 1]])
    query_arr = np.array([1, 1])
    result = cosine_similarity_to_query(vector_arr, query_arr)
    print("vectors와 query 벡터와의 코사인 유사도:", result)