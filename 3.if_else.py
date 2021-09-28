# Логические и условные операторы

# Операторы сравнения

z = 3
w = 2

# Операция "равно"
# мы спрашиваем "значение z равно значению w ?"
result = z == w

# Операция "не равно"
result = z != w

# операция "меньше"
result = z < w

# операция "больше"
result = z > w

# операция "меньше либо равно"
result = z >= w


# чистые логчиеские операции

var_1 = True
var_2 = False
var_3 = False

# оператор "не" (not, инверсия)
result = not var_1

# оператор "И" (and, конъюнкция) логическое умножение - возвращает true только тогда, 
# когда оба переменных являются True
result = var_1 and var_2 and var_3

# оператор "ИЛИ" (or, дизъюнкция) логическое сложение
# возвращает False только тогда,
# когда оба переменных false
result = var_3 or var_2

# пример комбинация логических операторов
a = 5
b = 3
c = 3
result = ((a > b) and (b != c)) or (a == c)

#print (result)

# УСЛОВНЫЕ ОПЕРАТОРЫ
var = 10

#Оператор if
# if var != 0:
#     print("Hello")

# if True:
#     print("hi")

if not var < 12:
    print("helloooo")

# оператор else

# var = -1
# if var > 0:
#     print("больше нуля")
# else:
#     print("не больше нуля")

# оператор elif
var = 0
# if var > 0:
#     print("больше нуля")
# elif var < 0:
#     print("меньше нуля")
# else:
#     print("не больше нуля")

var = "a"
if var == "a":
    res = 'literal a'
elif var == "A":
    res = "literal A"
elif var == "B":
    res = "literal B"
elif var == "C":
    res = "literal C"

# print(res)




#calculator

num_1 = int(input("Введите число №1: "))
num_2 = int(input("Введите число №2: "))

op = input("Введите символ операции: ")

if op == "+":
    res = num_1 + num_2
elif op == "-":
    res = num_1 - num_2
elif op == "*":
    res = num_1 * num_2
elif op == "/":
    res = num_1 / num_2
else:
    res = "Символ операции некорректен :("


print(f"Результат = {res}")