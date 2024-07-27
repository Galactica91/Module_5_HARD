import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == int(hashlib.sha256(password.encode()).hexdigest(), 16):
                self.current_user = user
                print("Вход выполнен успешно.")
                return True
        print("Неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return False
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print("Регистрация выполнена успешно. Вы авторизованы.")
        return True

    def log_out(self):
        self.current_user = None
        print("Выход из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f"Видео '{video.title}' успешно добавлено.")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = []
        for video in self.videos:
            if search_word in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Просмотр видео '{video.title}'")
                while video.time_now < video.duration:
                    print(video.time_now)
                    video.time_now += 1
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return

        print("Видео не найдено.")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)

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
