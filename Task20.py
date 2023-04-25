# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.

scrabble_points = {}
one = 'A, E, I, O, U, L, N, S, T, R'
two = 'D, G'
three = 'B, C, M, P'
four = 'F, H, V, W, Y'
five = 'K'
eight = 'J, X'
ten = 'Q, Z'
scrabble_points[1] = [i for i in one.split(', ')]
scrabble_points[2] = [i for i in two.split(', ')]
scrabble_points[3] = [i for i in three.split(', ')]
scrabble_points[4] = [i for i in four.split(', ')]
scrabble_points[5] = [i for i in five.split(', ')]
scrabble_points[8] = [i for i in eight.split(', ')]
scrabble_points[10] = [i for i in ten.split(', ')]

word = input('введите слово: ').upper()
word_cost = 0
for letter in word:
    for key in scrabble_points:
        if letter in scrabble_points[key]:
            word_cost += int(key)
print('стоимость слова:', word_cost)