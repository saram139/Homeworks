import numpy as np

"""NumPy — это фундаментальный пакет для научных вычислений на Python. 
Это библиотека Python, которая предоставляет многомерный объект массива, различные 
производные объекты (такие как маскированные массивы и матрицы) и набор процедур для 
быстрых операций с массивами, включая математические, логические, манипуляции с формой, 
сортировку, выборку, ввод-вывод, дискретные преобразования Фурье, базовую линейную алгебру, 
базовые статистические операции, случайное моделирование и многое другое."""


"""Создание массивов из списков"""

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a1)
print(a2)


"""Создание массива с нулевыми значениями"""

a3 = np.zeros((3, 4))
print(a3)


"""Oбъединения четырех массивов 2 на 2 в массив 4 на 4"""

A = np.ones((2, 2))
B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))
a4 = np.block([[A, B], [C, D]])

print(a4)


import matplotlib.pyplot as plt


"""Matplotlib — популярная Python-библиотека для визуализации данных. 
Она используется для создания любых видов графиков: линейных, круговых диаграмм, 
построчных гистограмм и других — в зависимости от задач."""


"""Создание графика с изменением цвета и добавлением надписей"""

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cos, sin = np.cos(X), np.sin(X)
plt.plot(X, cos, color="blue", label="cos")
plt.plot(X, sin, color="red", label="sin")
plt.legend(loc="upper left", frameon=False)
plt.show()

"""Создание круговой диаграммы"""

names = "Tom", "Dick", "Harry", "Jill", "Meredith", "George"
speed = [8, 7, 12, 4, 3, 2]
colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue", "red", "blue"]
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(
    speed,
    explode=explode,
    labels=names,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)
plt.axis("equal")
plt.show()


from PIL import Image

"""Pillow и его предшественник PIL — это оригинальные библиотеки Python 
для работы с изображениями. Несмотря на то, что существуют другие 
библиотеки Python для обработки изображений, Pillow остается важным 
инструментом для понимания и работы в целом. Для оперирования и обработки 
изображений Pillow предоставляет инструменты, аналогичные тем, которые 
можно найти в программном обеспечении, таком как Photoshop. 
Некоторые из более современных библиотек обработки изображений Python 
построены на основе Pillow и часто предоставляют более продвинутую функциональность."""

filename = "test_image.jpg"
with Image.open(filename) as img:
    img.load()

    """Обрезка изображения"""

    obrezka_img = img.crop((200, 200, 800, 1000))

    """Изменение размера изображения"""

    umensheniye_img = obrezka_img.resize((obrezka_img.width // 4, obrezka_img.height // 4))
    umensheniye_img.show()

    print(umensheniye_img.size)
    
    """Преобразование в режим вывода изображения в градациях серого"""

    gray_img = img.convert("L")
    gray_img.show()

    print(gray_img.getbands())

    
