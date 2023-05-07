# Задача 30:  Заполните массив элементами арифметической 
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для 
# получения n-го члена прогрессии: an = a1 + (n-1) * d. 
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_el = int(input('Первый элемент: '))
raznost = int(input('Разность: '))
kolvo_el = int(input('Кол-во элементов: '))
progressia = [i for i in range(first_el, first_el + (kolvo_el - 1) * raznost + 1, raznost)]
print(progressia)

# for i in range(kolvo_el):
#     print(first_el + i * raznost)