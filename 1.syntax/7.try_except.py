# ИСКЛЮЧЕНИЯ (исключительные события/ситуации, ошибки)

# ошибки: синтаксические и логические

# # Пример исключения при делении на ноль
# a = 100
# b = 10

# c = a / b

# #отлов исключения
# try:
#     #потенциально аварийный код
#     c = a / b
# except:
#     #код, который должен сработать при исключении
#     c = 0

# print(c)

#Обработка множества исключений
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
# except ZeroDivisionError:
#     print("На ноль делить нельзя!!!")
# except ValueError:
#     print("Нужно ввести числовое выражение")
# #общее исключение
# except Exception as error:
#     print(error)

#Конструкция "try-except-finally"
# try:


# создаем классы ошибок КАСТОМИЗИРОВАННЫЕ исключения
# try:
#     a = input("Введите символ: ")
#     if a == 'A' :
#         raise Exception("Ошибка А")
#     elif a == 'B' :
#         raise Exception("Ошибка В")
#     elif a == 'С' :
#         raise Exception("Ошибка С")
# except Exception as err:
#     print(err)

#Пример приближенный к реальности
# while True:
#     try:
#         a = int(input("Введите число: "))
#         c = 100 / a
#     except ZeroDivisionError:
#         print("Деление на ноль нельзя")
#         continue
#     except ValueError:
#         print("Вы ввели не число")
#         continue
#     print(f"Result: {c}")
#     break

#Пример калькулятор
def calculate(n1, n2, op):
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    result = d[op](n1, n2)

while True:
    # ввод данных
    cmd = input("напишите команду: ")
    if cmd == "stop":
        print("Bye Bye")
        break

    try:
        num_1 = int(input("Введите 1 число: "))
        num_2 = int(input("Введите 2 число: "))
        op = input("Введите символ операции: ")

        # обработка данных
        result = calculate(num_1, num_2, op)
    except ZeroDivisionError:
        result = "На ноль делить нельзя"
        continue
    except ValueError:
        result = "вы ввели не число"
        continue
    finally:
    # вывод данных
        print(f"Результат: {result}")
        