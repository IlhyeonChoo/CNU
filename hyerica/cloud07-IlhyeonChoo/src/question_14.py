from collections import Counter

def find_topk_items(carts, k):
    """
    여러 사용자의 장바구니 목록(C)을 입력받아 가장 많이 담긴 물품을 찾는 함수이다.
    장바구니 목록을 하나의 리스트로 만들고, 가장 많이 담긴 물품 k 개를 찾으시오.
    (힌트: Counter의 most_common 메서드)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      carts: 여러 사용자의 장바구니에 담긴 물품 리스트
      k: 찾을 물품의 개수
    인자:
      carts (list): 여러 사용자의 장바구니에 담긴 물품 리스트
      k (int): 찾을 물품의 개수
    반환값:
      list: [(상품이름, 등장개수), ...]
    예시:
      >>> find_topk_items(C, 2)
          [('milk', 4), ('apple', 2)]
      >>> find_topk_items(C, 1)
          [('milk', 4)]
    """
    # ===== Your Code Here =====
    items = [item for cart in carts for item in cart]
    item_counter = Counter(items)
    # ==========================
    return item_counter.most_common(k)

if __name__ == '__main__':
    C = [['apple', 'banana', 'milk'], ['milk', 'bread'], ['apple', 'milk', 'egg'], ['banana', 'bread', 'milk']]
    K = 2
    #### 함수 호출 ####
    print(f'Top {K} Items: {find_topk_items(C, K)}')
    #################
