from collections import namedtuple

def create_products(data):
    """
    원시 데이터 튜플 리스트(data_list)를 입력받아, 각 튜플을 Product 네임드튜플 객체로 변환하여 리스트로 반환하는 함수이다.
    함수 내에서 'product_id', 'name', 'price', 'category' 필드를 가지는 Product 네임드튜플을 정의하고,
    입력된 데이터 리스트의 각 튜플을 사용하여 Product 객체를 생성한 후 리스트에 담아 반환한다.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      data: 각 요소가 (ID, 이름, 가격, 카테고리) 순서의 값을 가지는 튜플들의 리스트
    인자:
      data (list): 상품 정보 (ID, 이름, 가격, 카테고리) 튜플로 이루어진 리스트
    반환값:
      list: 각 요소가 Product 네임드튜플 객체인 리스트
    예시:
      >>> create_products(data_list)
      [Product(product_id=1, name='Laptop', price=1000, category='Electronics'), Product(product_id=2, name='Python Programming', price=2000, category='Books'), Product(product_id=3, name='Chocolate', price=3000, category='Food')]
"""
    # ===== Your Code Here =====
    Product = namedtuple("Product", ["product_id", "name", "price", "category"])
    products = [Product(*item) for item in data]
    # ==========================
    return products

def filter_category(products, category):
    """
    Product 네임드튜플 객체 리스트와 특정 카테고리 이름을 입력받아, 해당 카테고리에 속하는 상품들만 필터링하여 새로운 리스트로 반환하는 함수이다.
    입력된 상품 리스트(products)를 순회하며 각 상품의 category 필드 값을 입력된 category 값과 비교한다.
    두 값이 일치하는 상품 객체만 filtered_products 리스트에 추가하여 최종적으로 반환한다.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      products: Product 네임드튜플 객체들로 이루어진 리스트 (create_products의 반환값)
      category: 필터링할 카테고리 이름 (str)
    인자:
      products (list): Product 네임드튜플 객체의 리스트
      category (str): 필터링 기준으로 사용할 카테고리 이름
    반환값:
      list: 입력된 category와 일치하는 Product 네임드튜플 객체만 포함하는 리스트. 일치하는 상품이 없으면 빈 리스트.
    예시:
      >>> filter_category(p_list, 'Electronics')
      [Product(product_id=1, name='Laptop', price=1000, category='Electronics')]
      >>> filter_category(p_list, 'Food')
      [Product(product_id=3, name='Chocolate', price=3000, category='Food')]
    """
    # ===== Your Code Here =====
    filtered_products = [
        product for product in products if product.category == category
    ]
    # ==========================
    return filtered_products

if __name__ == '__main__':
    data_list = [(1, 'Laptop', 1000, 'Electronics'), (2, 'Python Programming', 2000, 'Books'), (3, 'Chocolate', 3000, 'Food')]
    
    #### 함수 호출 ####
    p_list = create_products(data_list)
    print(filter_category(p_list, 'Electronics'))
    #################
