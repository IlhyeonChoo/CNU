def solution(name, fruits):
    """
    **문제**
    과일 이름과 가격이 저장된 딕셔너리(fruits)에서, 특정 과일의 이름(name)을 입력받아 해당 항목을 제거하는 코드를 작성하세요.

    - 과일이 존재하면 딕셔너리에서 제거하고, 그 과일의 가격(정수)을 반환하세요.
    - 과일이 존재하지 않으면 None을 반환하세요.

    **예시**
    - 제거할 과일: Banana → 출력: 500
    - 제거할 과일: Mango → 출력: None

    **힌트**
    - 딕셔너리의 메서드를 사용하면 키가 없을 때 기본값을 반환할 수 있습니다.

    **주의**
    - 함수 내부에서는 외부 전역 변수(products 등)를 직접 참조하지 말고, 함수로 전달된 인자를 사용해야 합니다.
    - 대소문자를 구분합니다 (예: 'banana'는 'Banana'와 다릅니다).
    """
    # ===== Your code here =====
    price = fruits.pop(name, None)

    # ==========================

    
    return price
    
if __name__ == "__main__":
    products = {'Apple': 1000, 'Banana': 500, 'Orange': 800}
    target = input("삭제할 제품을 입력하세요: ")
    answer = solution(target, products)
    print(answer)
