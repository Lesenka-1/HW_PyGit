# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def stepen(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

a = int(input('a = '))
b = int(input('b = '))
print(stepen(a, b))