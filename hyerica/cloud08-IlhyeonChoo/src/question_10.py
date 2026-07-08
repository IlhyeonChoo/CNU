from collections import Counter, namedtuple

def get_bestseller(sales):
    """
    판매 기록(sales)을 받아 가장 많이 팔린 상품의 정보를 BestSeller namedtuple로 반환하는 함수이다.
    함수 내에서 'name', 'count' 필드를 가지는 BestSeller namedtuple을 정의하시오.
    Counter를 사용하여 각 상품의 판매 횟수를 세고, most_common(1)로 1위 상품을 찾으시오.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      sales: 판매된 상품 이름의 리스트 (같은 상품이 여러 번 등장 가능)
    인자:
      sales (list): 판매된 상품 이름이 담긴 리스트
    반환값:
      BestSeller: name(상품명)과 count(판매횟수) 필드를 가진 BestSeller namedtuple
    예시:
      >>> get_bestseller(['shirt', 'pants', 'shirt', 'shoes', 'shirt', 'pants'])
          BestSeller(name='shirt', count=3)
    """
    # ===== Your Code Here =====
    BestSeller = namedtuple('BestSeller', ['name', 'count'])
    name, count = Counter(sales).most_common(1)[0]
    return BestSeller(name, count)
    # ==========================

if __name__ == '__main__':
    sales = ['shirt', 'pants', 'shirt', 'shoes', 'shirt', 'pants', 'shoes', 'shoes', 'shoes']
    #### 함수 호출 ####
    best = get_bestseller(sales)
    print(f'베스트셀러: {best}')
    #################
