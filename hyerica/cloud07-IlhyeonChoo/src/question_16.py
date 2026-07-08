from collections import defaultdict

def group_employees_by_dept(employees):
    """
  직원 정보 목록(E)을 입력받아, 부서별로 직원들을 그룹화하고 각 직원의 이름과 입사 연도를 저장하는 딕셔너리를 반환하는 함수이다.
  입력된 직원 목록을 순회하며 defaultdict(list)를 사용하여 각 부서를 키(key)로,
  해당 부서 직원들의 (이름, 입사 연도) 튜플 리스트를 값(value)으로 저장한다.
  (힌트: defaultdict(list)를 사용하면 부서가 처음 등장할 때도 키 존재 여부 확인 없이 바로 .append()를 사용할 수 있음)
  함수에 사용되는 매개변수를 다음과 같이 설정하시오:
    employees: 각 직원의 이름, 부서, 입사 연도로 구성된 튜플들의 리스트
  인자:
    employees (list): 직원 정보 튜플 (이름, 부서, 입사 연도)로 이루어진 리스트
  반환값:
    defaultdict: 부서 이름을 키로, 해당 부서 소속 직원들의 (이름, 입사 연도) 튜플 리스트를 값으로 가지는 defaultdict 객체
  예시:
    >>> group_employees_by_dept(E)
    defaultdict(<class 'list'>, {'HR': [('Kim', 2022), ('Choi', 2023)], 'Dev': [('Lee', 2021), ('Park', 2022), ('Jung', 2021)]})
  """
    # ===== Your Code Here =====
    grouped_employees = defaultdict(list)
    for name, dept, year in employees:
        grouped_employees[dept].append((name, year))
    # ==========================
    return grouped_employees

if __name__ == '__main__':
    E = [('Kim', 'HR', 2022), ('Lee', 'Dev', 2021), ('Park', 'Dev', 2022), ('Choi', 'HR', 2023), ('Jung', 'Dev', 2021)]

    #### 함수 호출 ####
    grouped_employees = group_employees_by_dept(E)
    print(grouped_employees)
    ################
    
