# Задача 10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

kolvo_monet = int(input("Введите кол-во монет: "))
summa_orel = 0
summa_reshka = 0
for i in range (kolvo_monet):
    moneta = int(input())
    if moneta == 1:
        summa_reshka += 1
    else:
        summa_orel += 1
if summa_reshka > summa_orel:
    print("переверни {} монет".format(summa_orel))
else:
    print("переверни {} монет".format(summa_reshka))