import hashlib


class Member:
    name = ""
    user_name = ""
    password = ""
    # 일단 비워두고 인스턴스로 속성을 부여하려고 합니다.

    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = self.hash_password(password)
    # 생성자 메소드 만들기. 기본적인 틀입니다.

    def hash_password(self, password):
        hash_object = hashlib.sha256(password.encode("utf-8"))
        return hash_object.hexdigest()
    # 비밀번호 해싱 알아보고 적용해봤습니다.
    # 발음이 특이한 인도분의 영상을 보고 배워 해싱에 대해 제대로 이해하진 못했지만 일단 넣어봤습니다.
    # 비밀번호에 소금(salt)을 치라는데 무슨 말인지 몰라서 다음에 찾아보려고 합니다.

    def display(self):
        print(f"성함: {self.name}, ID: {self.user_name}")
    # 회원정보를 display 메소드를 통해 보여줍니다.
    # 비밀번호는 안알랴줌니다.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    # Post도 똑같이 틀을 잡아줍니다.

    def __repr__(self):
        return f"제목: {self.title} / {self.content} / 작성자: {self.author}"
    # 포스트 내용을 출력하는 메소드입니다. str을 쓰려고 했는데 찾아보니 사용자 입장에서 보기 편하게 출력해주는 메소드가 따로 있더군요.
    # 그래서 그 메소드를 이용해보고자 __repr__을 사용했습니다.
    # 이 메소드는 나중에 for문을 돌면서 뭔가 찾아낼 때 쓰려고 만들었습니다.


members = []

m1 = Member(
    name="Ronnie Coleman",
    user_name="800Solid-assPound",
    password="yeahbuddy"
)

m2 = Member(
    name="Dorian Yates",
    user_name="KingofBack",
    password="mindalwaysfailsfirst"
)

m3 = Member(
    name="Tom Platz",
    user_name="InsaneQaud",
    password="failureachieved"
)
# 유저 인스턴스 3개입니다.
# 제가 존경하는 전설적인 바디빌더 3명입니다.

members.append(m1)
members.append(m2)
members.append(m3)
# 만들어둔 멤버 인스턴스를 리스트 안에 넣습니다.


posts = []

m1_p1 = Post(
    "오늘의 운동일지/월요일",
    "예압 버디~ 오늘은 가슴하는 날이었어. #오운완#가슴운동#덤벨#lightweightbaby",
    m1.user_name
)

m1_p2 = Post(
    "오늘의 일기",
    "제이 커틀러가 몸이 점점 커지고 있어... 이대로 가다간 우승을 못할 것 같아. #긴장감#제이커틀러#올림피아8승",
    m1.user_name
)

m1_p3 = Post(
    "오늘의 운동일지/수요일",
    "오늘은 1톤 레그프레스를 했어. 8reps 했는데 가볍더라. #오운완#하체운동#1톤레그프레스",
    m1.user_name
)
# 1번 회원 로니 콜먼의 포스트들입니다. 본인의 마음으로 써봤습니다. 로니는 성격이 유쾌하고 가볍습니다.

posts.append(m1_p1)
posts.append(m1_p2)
posts.append(m1_p3)
# 그리고 이 포스트들을 리스트에 넣어줍니다.

m2_p1 = Post(
    "2024.02.26 운동기록",
    "오늘은 등하는 날이었습니다. 제 주특기죠. 로우가 잘먹어서 좋았습니다. #오운완#등운동#바벨로우#등신",
    m2.user_name
)

m2_p2 = Post(
    "2024.02.27 운동기록",
    "오늘은 가슴했습니다. 벤치가 잘 먹어서 좋네요. #오운완#가슴운동#벤치프레스",
    m2.user_name
)

m2_p3 = Post(
    "2024.02.28 운동기록",
    "오늘은 어깨했습니다. 새로 들어온 머신이 참 좋더군요. #오운완#어깨운동#헤머스트렝스최고",
    m2.user_name
)
# 2번 회원 도리안 예이츠의 포스트입니다. 도리안은 성격이 꼼꼼해서 항상 운동할 것 같아요.

posts.append(m2_p1)
posts.append(m2_p2)
posts.append(m2_p3)
# 똑같이 리스트에 넣어줍니다.

m3_p1 = Post(
    "명언",
    "실패를 경험하지 않으면 성장하지 못한다. #명언#마음가짐#자기계발",
    m3.user_name
)

m3_p2 = Post(
    "2024.02.28 운동일지",
    "오늘은 헬스장에 도리안이 있었다. 같이 어깨운동을 했는데 도리안은 역시 올림피안다운 실력을 가졌다. #오운완#올림피아#헬스",
    m3.user_name
)

m3_p3 = Post(
    "나도 올림피아 우승하고 싶다",
    "왜 우승을 못하는 거지... 왜 나는 하체만 좋은거지... #열등감#올림피아#우승하고싶다",
    m3.user_name
)
# 3번 회원 톰 플라트의 포스트입니다. 강한 정신력을 가진 전설적인 빌더지만 한 번도 올림피아 우승을 못해봐서 젊은 시절에는 열등감에 시달렸다고 합니다.

posts.append(m3_p1)
posts.append(m3_p2)
posts.append(m3_p3)
# 또 똑같이 리스트에 넣어줍니다.
# 총 9개가 들어가게 됐습니다.

# print(posts)
# 글이 길어서 제대로 들어갔나 확인해보기 위해 출력해줍니다.

for member in members:
    print(member.name)
# 5-a 리스트를 돌면서 멤버들의 이름만 출력합니다.

for post in posts:
    if post.author == members.user_name:
        print(post.title)
# 6-a for문을 돌며 특정 유저가 작성한 게시글의 제목을 전부 출력합니다.


keyword = input("오운완")
for post in posts:
    if keyword in post.content:
        print(post.title)
# 6-b for문을 돌면서 특정 단어가 content에 포함되어 있으면 게시글의 제목을 모두 출력합니다.
# 오운완이 들어간 게시글의 제목을 전부 출력합니다.
