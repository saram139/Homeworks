from time import sleep
from datetime import datetime
from threading import Thread

time_start1 = datetime.now()


def write_words(word_count, file_name):

    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i+1}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f"Работа потоков {time_res1}")

time_start2 = datetime.now()

file1 = Thread(target=write_words, args=(10, "example5.txt"))
file1.start()
file2 = Thread(target=write_words, args=(30, "example6.txt"))
file2.start()
file3 = Thread(target=write_words, args=(200, "example7.txt"))
file3.start()
file4 = Thread(target=write_words, args=(100, "example8.txt"))
file4.start()

file1.join()
file2.join()
file3.join()
file4.join()


time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(f"Работа потоков {time_res2}")
