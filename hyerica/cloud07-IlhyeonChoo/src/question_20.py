import copy

def return_True(original, copy):
    """
    ** 이 함수를 수정하지 마세요 **
    두 객체가 동일한 객체인지 (is) 확인하여 True/False를 반환 (True 반환 기대)
    """
    return original is copy

def return_False(original, copy):
    """
    ** 이 함수를 수정하지 마세요 **
    두 객체가 동일한 객체인지 (is) 확인하여 True/False를 반환 (False 반환 기대)
    """
    return original is copy
        
if __name__ == '__main__':
    """
    **문제**
    두 튜플 A,B와 각 튜플의 깊은복사본 A_copy, B_copy가 주어졌을때, 두 함수의 출력에 맞게 올바른 인자를 전달하시오.
    각 함수는 원본 튜플 A와 복사본 A_copy 또는 원본 튜플 B와 B_copy 를 입력받습니다.
    return_True 함수는 True를 반환해야하며(동일 객체), return_False 함수는 False를 반환해야합니다(다른 객체).
    각 함수에 올바른 인자를 전달하고 이유를 생각해보세요.
    **예시**
    >>> return_True(???, ???)
    >>> True 가 반환되어야함
    >>> return_False(???, ???)
    >>> False 가 반환되어야함
    """
    A = (1,2,3,['a','b','c'])
    B = (1,2,3,'a','b','c')
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    true_result = return_True(B, B_copy)
    print(true_result)
    false_result = return_False(A, A_copy)
    print(false_result)

    
