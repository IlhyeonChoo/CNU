from collections import namedtuple

def parse_log(log):
    """
    단일 로그 라인 문자열을 입력받아 타임스탬프, 로그 레벨, 메시지 문자열로 분리하여 튜플로 반환하는 함수이다.
    입력된 로그 문자열을 공백 기준으로 분리한다. 첫 두 요소를 '/'로 연결하여 타임스탬프를 만들고,
    세 번째 요소를 로그 레벨로 (대괄호 포함), 나머지 요소들을 공백으로 연결하여 메시지로 만든다.
    (주의: 예시의 결과와 동일하게 문자열을 만들어야합니다.)
    (힌트: 문자열의 split()과 join() 메소드를 활용하여 로그를 파싱합니다.)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      log: 파싱할 단일 로그 라인 (str)
    인자:
      log (str): 파싱할 원본 로그 문자열.
    반환값:
      tuple: (타임스탬프 문자열, 로그 레벨 문자열, 메시지 문자열) 형태의 튜플.
    예시:
      >>> parse_log(log_line)
      ('2025-05-02/13:00:00', '[INFO]', 'User logged in')
    """
    # ===== Your Code Here =====
    parts = log.split()
    timestamp = "/".join(parts[:2])
    level = parts[2]
    message = " ".join(parts[3:])
    # ==========================
    return timestamp, level, message

def create_logs(logs):
    """
    ** create_logs 함수 내부에서 parse_log 함수를 반복하여 호출하는 구조입니다. **
    로그 라인 문자열 리스트(log_lines)를 입력받아, 각 라인을 파싱하고 그 결과를 LogEntry 네임드튜플 객체로 변환하여 리스트로 반환하는 함수이다.
    입력된 로그 리스트의 각 문자열에 대해 parse_log 함수를 호출하여 파싱 결과를 얻는다.
    이 결과를 사용하여 'timestamp', 'level', 'message' 필드를 가지는 LogEntry 네임드튜플 객체를 생성하고,
    이 객체들을 리스트에 담아 반환한다.
    (힌트: 내부적으로 parse_log 함수를 사용하여 각 라인을 처리하고, 결과를 구조화하기 위해 namedtuple을 활용합니다.)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      logs: 여러 개의 로그 라인 문자열을 담고 있는 리스트
    인자:
      logs (list): 로그 라인 문자열들로 이루어진 리스트.
    반환값:
      list: 각 요소가 파싱된 로그 정보를 담은 LogEntry 네임드튜플 객체인 리스트.
    예시:
      >>> create_logs(log_lines)
      [LogEntry(timestamp='2025-05-02/13:00:00', level='[INFO]', message='User logged in'), LogEntry(timestamp='2025-05-02/14:00:00', level='[INFO]', message='User Buy item'), LogEntry(timestamp='2025-05-02/15:00:00', level='[INFO]', message='User logged out')]
    """
    # ===== Your Code Here =====
    LogEntry = namedtuple("LogEntry", ["timestamp", "level", "message"])
    parsed_logs = [LogEntry(*parse_log(log)) for log in logs]
    # ==========================
    return parsed_logs
    
if __name__ == '__main__':
    log_lines = ["2025-05-02 13:00:00 [INFO] User logged in",\
                "2025-05-02 14:00:00 [INFO] User Buy item",\
                "2025-05-02 15:00:00 [INFO] User logged out"]
    #### 함수 호출 ####
    print(create_logs(log_lines))
    #################
