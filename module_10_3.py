from threading import Lock, Thread
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            value = randint(50, 500)
            self.balance += value
            print(f"Пополнение: {value}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for _ in range(100):
            value = randint(50, 500)
            print(f"Запрос на {value}")
            if value <= self.balance:
                self.balance -= value
                print(f"Снятие: {value}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
