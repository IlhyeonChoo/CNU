class Song:
    """
    노래 정보를 저장하는 클래스 (제목, 아티스트, 재생 시간)
    생성자:
        - title (str): 노래 제목
        - artist (str): 아티스트 이름
        - duration (int): 재생 시간 (초 단위)
    메서드:
        - __str__: 노래 정보를 문자열로 반환하는 메서드
            - 재생 시간(초)를 분과 초로 변환하고 아래와 같이 문자열을 반환
            - 분: duration // 60
            - 초: duration % 60 
            - Song 객체를 print 했을때, 아래와 같은 포맷으로 출력되어야함
            - 예시: Too Bad - GD (3:22)
    """

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        minute = self.duration // 60
        second = self.duration % 60
        return f"{self.title} - {self.artist} ({minute}:{second:02d})"

class PlayList:
    """
    Song 객체들을 저장하고 관리하는 클래스
    생성자:
        - 매개변수 없음
        - songs (list): Song 객체들을 저장할 빈 리스트로 초기화
    메서드:
        - add_song:
            - song (Song): 추가할 노래 객체
            - 반환값 (PlayList): 메서드를 중복 호출 할 수 있도록 self를 반환
        - __len__:
            - 반환값 (int): 곡 수
        - __getitem__:
            - index (int): 접근할 곡의 인덱스
            - 반환값 (Song): 해당 인덱스의 노래 객체
        - __str__:
            - 반환값 (str): 전체 곡 목록을 문자열로 반환하는 메서드
            - PlayList 객체를 print 했을때, 아래와 같은 포맷으로 출력되어야함
            - 출력 예시:
                PlayList:
                1. Too Bad - GD (3:22)
                2. Attention - NewJeans (2:58)
    """

    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        return self

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __str__(self):
        lines = ["PlayList:"]
        for index, song in enumerate(self.songs, start=1):
            lines.append(f"{index}. {song}")
        return "\n".join(lines)
    
if __name__ == '__main__':
    p = PlayList()
    s1 = Song("Too Bad", "GD", 202)
    s2 = Song("Attention", "NewJeans", 178)
    p.add_song(s1).add_song(s2)
    
    print(p)
    print("총 곡 수:", len(p))
    print("두 번째 곡:", p[1])
