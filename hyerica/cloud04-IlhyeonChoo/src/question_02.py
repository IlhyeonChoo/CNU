def filter_gary(fullnames):
    """
    **문제**
    - 풀네임(이름 + 성)의 리스트가 주어졌을 때, 이름이 "Gary"인 사람으로만 구성된 리스트를 구하세요.
    - fullnames는 풀네임의 리스트입니다. fullnames = ["이름1 성1", "이름2 성2"]
    - fullnames 안에 들어있는 이름 문자열들은 모두 "{이름} {성}" 형식으로 구성되어 있습니다.
    
    - (Optional) 실습문제와 별개로, Gary라는 이름도 외부에서 입력받을 수 있게 함수를 만들어보세요. 예: def filter_name(fullnames, target_name)
      !단, 이 파일에 작성하시면 안되고, commit 및 푸쉬해서도 안됩니다.

    **힌트**
    - 문자열의 startswith 메서드를 활용하세요.

    **예상출력**
    - Test case 1
    -     ["Gary Neville", "Gary Cahill"]
    - Test case 2
    -     ["Gary O'Neil"]
    - Test case 3
    -     ["Gary Lineker", "Gary Rowett"]
    """

    filtered_fullnames = []

    for fullname in fullnames:
        # ===== Your code here =====
        # if에 들어갈 조건문을 완성하세요. False를 지우고 작성하세요.
        if fullname.startswith("Gary"):
            filtered_fullnames.append(fullname) # 건들지마세요.
        # ==========================

    return filtered_fullnames
            

if __name__ == "__main__":
    print("Test case 1")
    fullnames = ["Jordan Henderson", "Nick Powell", "Gary Neville", "Wayne Rooney", "Gary Cahill"]
    filtered_fullnames = filter_gary(fullnames)
    print(f"\t{filtered_fullnames}") # \t는 space 네 칸(칸수는 다를 수 있음) 띄우기 입니다.

    print("Test case 2")
    fullnames = ["Gary O'Neil", "Phil Foden", "Jesse Lingard",]
    filtered_fullnames = filter_gary(fullnames)
    print(f"\t{filtered_fullnames}") 

    print("Test case 3")
    fullnames = ["Harry Kane", "Nicky Butt", "Gary Lineker", "Bukayo Saka", "Gary Rowett"]
    filtered_fullnames = filter_gary(fullnames)
    print(f"\t{filtered_fullnames}") 

