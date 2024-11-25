import hashlib
from time import sleep



class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        return int(hashlib.sha256(password.encode()).hexdigest(),16)

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname and other.password == self.password

class Video:
    def __init__(self, title, duration, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
    def __eq__(self, other):
        return self.title.lower() == other.title.lower()
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in (self, nickname, password):
        hashed_password = User.hash_password(password)
        user = next((u for u in self.users if u.nickname == nickname
                     and u.password == hashed_password), None)
        if user:
            self.current_user = user
        else:
            print('Не верное имя или пароль')

    def register (self, nickname, age, password):
        if any (u.nickname == nickname for u in self.users):
            print(f'пользователь {nickname} уже существует')
        else:
            user = User(nickname, age, password)
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add (self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos (self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video (self, title):
        if not  self.current_user:
            print('Авторизуйтесь для просмотра видео')
            return
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            return
        if video.adult_mode and self.current_user.age < 18:
            print('Вам еще нет 18')
            return
        while video.time_now < video.duration:
            video.time_now += 1
            print(video.time_now, end = ' ', flush = True)
            sleep(0.5)
        print(' Конец видео')
        video.time_now = 0


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')








