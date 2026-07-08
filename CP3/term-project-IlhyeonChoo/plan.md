# 전체 구현 계획

## 구현 순서

1. Student 구조 및 불러오기 구현
2. exit 구현
3. save, add, delete, update 구현 {Amdin 전용}
4. 전체 출력, 화면 지우기 구현
5. 학생 검색 구현
6. 통계 기능 및 출력 구현
7. help 작성
8. 예외처리 구현
9. sort 구현
10. save 시에 경고 구현
11. 명령어 파일 입력 구현

## 기능별 위치

1. 파일 읽기, 쓰기 file_io
2. 구조, 검색, 통계 student
3. 버퍼에 추가 제거 student
4. 전체 출력 student
5. help : main
6. 예외 처리 : command

## 워크플로우

### 1. 실행

1. main 에서 옵션 분석 (명령어 파일 입력 or 기본, io 파일)
2. file_io 에서 파일 읽어오고 오류 검사
3. student에서 데이터 버퍼로 로드
4. 출력

### 2. 기본 동작

1. command 파싱, 의미 분석
2. main에서 student로 전달
3. student cmd()에서 각 명령어 함수 실행
4. main에서 루프

### 3. 저장, 종료

1. student에서 버퍼 확인
2. student에서 file_io 이용해서 저장? 이럴거면 실행도 student로?
3. 저장 후 main 복귀 종료
