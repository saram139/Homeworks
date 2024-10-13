import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, "r") as f:
        for line in f.readlines():
            line = line.strip()
            all_data.append(line)


if __name__ == "__main__":
    filenames = [f"./file {number}.txt" for number in range(1, 5)]

    # Линейный
    start = datetime.now()

    for filename in filenames:
        read_info(filename)

    end = datetime.now()
    print(f"{end - start} (линейный)")

    # Многопроцессный
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.now()
    print(f"{end - start} (многопроцессный)")
