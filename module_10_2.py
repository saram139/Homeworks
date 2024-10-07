from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemyes = 100
        self.time = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemyes > 0:
            sleep(1)
            self.time += 1
            self.enemyes -= self.power
            print(f"{self.name} сражается {self.time} день(дня)..., осталось {self.enemyes} воинов.")
        print(f"{self.name} одержал победу спустя {self.time} дней(дня)!")


# Создание класса
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print(f"Все битвы закончились!")
