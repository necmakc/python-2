# -------------------------------------------------------------------------------------------------------
# Задача 1:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую 
# степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
# -------------------------------------------------------------------------------------------------------

# def Exponent(num_A, num_B) -> int:
#     if num_B<2:
#         return num_A
#     num_B -= 1
#     return num_A * Exponent(num_A,num_B)

# num_A, num_B = int(input("Введите число: ")),int(input("Введите степень: "))
# print(Exponent(num_A,num_B))

# -------------------------------------------------------------------------------------------------------
# Задача 2: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
# -------------------------------------------------------------------------------------------------------

def sum(num_a, num_b) -> int:
    return sum(num_a+1, num_b-1) if num_b > 0 else num_a

num_a, num_b = int(input("Введите первое число: ")),int(input("Введите второе число: "))
print(sum(num_a,num_b))