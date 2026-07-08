from collections import defaultdict

def generate_team_dict(scores):
    """
    팀별 점수 목록(S)을 입력받아, 팀별 총 점수를 계산하여 딕셔너리 형태로 반환하는 함수이다.
    입력된 점수 리스트를 순회하며 각 팀의 점수를 누적한다.
    (힌트: defaultdict(int)를 사용하면 키 존재 여부를 확인할 필요 없이 바로 점수를 누적할 수 있음)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      scores: 팀 이름과 해당 라운드에서 얻은 점수로 구성된 튜플들의 리스트
    인자:
      scores (list): 팀 이름과 점수 튜플((팀명, 점수))로 이루어진 리스트
    반환값:
      defaultdict: 팀 이름을 키로, 해당 팀의 총점을 값으로 가지는 defaultdict 객체
    예시:
      >>> generate_team_dict(S)
      defaultdict(<class 'int'>, {'Blue': 15, 'Red': 25, 'Green': 20})
    """
    # ===== Your Code Here =====
    team_scores = defaultdict(int)
    for team, score in scores:
        team_scores[team] += score
    # ==========================
    return team_scores

if __name__ == '__main__':
    S = [('Blue', 10), ('Red', 15), ('Blue', 5), ('Green', 20), ('Red', 10)]
    #### 함수 호출 ####
    team_scores = generate_team_dict(S)
    #################
    print(team_scores)
