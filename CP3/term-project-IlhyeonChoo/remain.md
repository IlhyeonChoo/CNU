# test 결과 남은 작업

## 1. 프로그램 시작 시 작업

=== TC01-TC05: 프로그램 시작 / 인자 처리 [PRD §3] (5pt) ===
  [FAIL] TC01: Admin 시작 배너 '[Admin Program]' (0/1pt)
  [FAIL] TC02: Client 시작 배너 '[Client Program]' (0/1pt)
  [FAIL] TC03: 인자 없을 때 'Usage' 출력 (0/1pt)
    출력: [TIMEOUT]
  [FAIL] TC04: 'Loaded 3 students from' 로드 메시지 (0/1pt)
  [FAIL] TC05: 잘못된 CSV 헤더 → Error 출력 (0/1pt)
    출력: Goodbye

## 2. find(search) 관련

=== TC27-TC30: find 명령어 [PRD §8.6] (7pt) ===
  [FAIL] TC27: find 1 (Admin) → ID:1, Name:Alice, Score:90 (0/2pt)
    출력: Error: not implemented Goodbye
  [FAIL] TC28: find 2 (Client) → ID:2, Name:Bob, Score:85 (0/2pt)
    출력: Error: not implemented Goodbye
  [FAIL] TC29: find 미존재 학생 → 'student not found' (0/2pt)
    출력: Error: not implemented Goodbye
  [PASS] TC30: find 잘못된 ID → Error (+1pt)

## 3. stats

=== TC36-TC38 + TC39: stats 명령어 [PRD §8.8] (9pt) ===
  [FAIL] TC36: stats (3명) → Count:3, Average:90.0, Max:95, Min:85 (0/3pt)
    출력: Error: not implemented Goodbye
  [FAIL] TC37: stats 빈 목록 → 'No student data available' (0/1pt)
    출력: Error: not implemented Goodbye
  [FAIL] TC38: stats (1명) → Count:1, Average:73.0, Max=Min=73 (0/2pt)
    출력: Error: not implemented Goodbye
  [FAIL] TC39: stats (100명) → Count:100, Max:100, Min:54 (0/3pt)
    출력: Error: not implemented Goodbye

## 4. help

=== TC44-TC45: help 명령어 [PRD §8.9] (4pt) ===
  [FAIL] TC44: help (Admin) → save/add/delete/update 모두 표시 (0/2pt)
    출력: Error: not implemented Goodbye
  [FAIL] TC45: help (Client) → find/list 표시, save 미표시 (0/2pt)
    출력: Error: not implemented Goodbye

# 안해도 상관 없는 보너스들

## 5. sort

=== BONUS CSV-05: sort name + save [PRD §16] (+4pt) ===
  [BONUS FAIL] CSV-05: sort name → save → 알파벳 순서 CSV 정답 일치 (0/4pt)
  ────────────────────────────────────────
  줄 2:
    실제 : 3,Charlie,95
    정답 : 1,Alice,90
  줄 3:
    실제 : 1,Alice,90
    정답 : 2,Bob,85
  줄 4:
    실제 : 2,Bob,85
    정답 : 3,Charlie,95
  ────────────────────────────────────────

=== BONUS CSV-06: sort score + save [PRD §16] (+4pt) ===
  [BONUS FAIL] CSV-06: sort score → save → 점수 오름차순 CSV 정답 일치 (0/4pt)
  ────────────────────────────────────────
  줄 2:
    실제 : 1,Alice,90
    정답 : 2,Bob,85
  줄 3:
    실제 : 3,Charlie,95
    정답 : 1,Alice,90
  줄 4:
    실제 : 2,Bob,85
    정답 : 3,Charlie,95
  ────────────────────────────────────────

=== BONUS TC40 + TC43: sort 메시지 / 에러 [PRD §16] (+2pt) ===
  [BONUS FAIL] TC40: sort name → 'sorted by name' 메시지 (0/1pt)
    출력: Error: not implemented Goodbye
  [BONUS PASS] TC43: sort badkey → Error (+1pt)

## 6. multi 그런데 위에 해결하다보면 대부분 해결될듯

=== ADV-OUT-01: 수정 후 stats [복합] (3pt) ===
  [ADV FAIL] ADV-OUT-01: add/update/delete 후 stats → Count:3, Min:50, Max:85 (0/3pt)
    출력: Student added Student updated Student deleted Error: not implemented Goodbye

=== ADV-OUT-02: delete 후 find [복합] (2pt) ===
  [ADV FAIL] ADV-OUT-02: delete 2(Bob) 후 find 2 → 'student not found' (0/2pt)
    출력: Student deleted Error: not implemented Goodbye

=== ADV-OUT-03: update 후 find [복합] (2pt) ===
  [ADV FAIL] ADV-OUT-03: update 1→99 후 find 1 → Score: 99 (0/2pt)
    출력: Student updated Error: not implemented Goodbye

=== ADV-OUT-04: -f 다중 에러 처리 [복합] (3pt) ===
  [ADV PASS] ADV-OUT-04: -f 에러 줄 skip 후 계속 → Skipped line 2/3, [command file:4] find 1 (+3pt)

=== ADV-OUT-05: 경계값 stats [복합] (2pt) ===
  [ADV FAIL] ADV-OUT-05: 경계값 stats → Count:5, Min:0, Max:100, Average:74.0 (0/2pt)
    출력: Student added Student added Error: not implemented Goodbye

=== ADV-OUT-06: delete 후 동일 ID 재사용 [복합] (1pt) ===
  [ADV FAIL] ADV-OUT-06: delete 2→add 2 NewBob→find 2 → 'Name: NewBob' (0/1pt)
    출력: Student deleted Student added Error: not implemented Goodbye

=== ADV-OUT-07: 전체 삭제 후 list / stats [복합] (2pt) ===
  [ADV PASS] ADV-OUT-07: 전체 삭제 후 list → 'No students found' (+1pt)
  [ADV FAIL] ADV-OUT-07: 전체 삭제 후 stats → 'No student data available' (0/1pt)
    출력: Student deleted Student deleted Student deleted No students found Error: not implemented Goodbye
