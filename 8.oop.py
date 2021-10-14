class Cat:
    def __init__(self):
        self.name = None
        self.color = None
    
    def mur(self):
        print("Mur-mur!!!")

    def speech(self):
        print(f"Name: {self.name}, Color: {self.color}")

    def __call__(self, a, b):
        return a + b

cat_1 = Cat()
cat_2 = Cat()

cat_1.name = "Pashka"
cat_1.color = "black"

cat_2.name = "Oliver"
cat_2.color = "white"

# print(cat_1.name)
# print(cat_2.name)

# вызов методом
# cat_1.mur()
# cat_1.speech()

result = cat_1(100, 20)
# print(result)


# Принципы ООП
# 1. Принцип наследования
# создание родительского (предкового) класса
class Animal:
    def __init__(self, n_legs):
        self.legs = n_legs

    def move(self):
        print("Я двигаюсь!")

# создание дочерних классов
class Human(Animal):
    def __init__(self, n_legs, name):
        super().__init__(n_legs)
        self.name = name

    def speech(self):
        print(f"My name is {self.name}. Legs: {self.legs}")

class Cat_2(Animal):
    def __init__(self, legs, name, color):
        super().__init__(legs)
        self.name = name
        self.color = color

    def speech(self):
        print(f"My name is {self.name}. Legs: {self.legs}, color: {self.color}")

    def mur(self):
        print("Mur-mur!!")

#Создание объекта
bug = Animal(6)

man_1 = Human(2, "Petya")
woman_1 = Human(2, "Katya")

cat_1 = Cat_2(4, "Pushok", "green")

bug.move()
print(bug.legs)

man_1.move()
man_1.speech()

cat_1.move()
cat_1.speech()
cat_1.mur()

