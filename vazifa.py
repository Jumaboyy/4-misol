#masala1
"""Ushbu classning barcha metodlariqa property decoratorini ulang.
Tashqaridan class objecti orqali bu ma'lumotlarni ko'rish, o'zgartirish va o'chirish imkoni bo'lsin.
"""
# class Car:
#     def __init__(self, model: str, color: str, speed: int, price: int):
#         self._model = model
#         self._color = color
#         self._speed = speed
#         self._price = price
#
#     @property
#     def model(self):
#         return self._model
#
#     @model.setter
#     def model(self, new_model):
#         self._model = new_model
#
#     @property
#     def color(self):
#         return self._color
#
#     @color.setter
#     def color(self, new_color):
#         self._color = new_color
#
#     @property
#     def speed(self):
#         return self._speed
#
#     @speed.setter
#     def speed(self, new_speed):
#         self._speed = new_speed
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self, new_price):
#         self._price = new_price
#
# model = input("Modelni kiriting: ")
# color = input('Rangini kiriting: ')
# speed = int(input('Tezlikni kiriting: '))
# price = int(input('Narxni kiriting: '))
#
# mashina = Car(model, color, speed, price)
# print(f"Model: {mashina.model}")
# print(f"Color: {mashina.color}")
# print(f"Speed: {mashina.speed}")
# print(f"Price: ${mashina.price}")

#masala2

"""2.Figure nomli class yozing. 
class ichida uchburchak perimeterini hisoblab beruvchi trianqle perimeterfa, b, c), 
uchburchak yuzasini hisiblovchi trianqle area(a. b, c), 
to'g'ri to'rtburchak perimeterini hisoblovchi rectanqle perimeter(a, b), 
to'g'ri to'rtburchak yuzasini hisoblovchi reactangle_area(a, b) nomli metodlar yozing. 
Bu metodlar barchasi static bolsin."""

# import math
# class Figure:
#     @staticmethod
#     def triangle_perimeter(a, b, c):
#         return a + b + c
#     @staticmethod
#     def triangle_area(a, b, c):
#         s = (a + b + c) / 2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         return area
#     @staticmethod
#     def rectangle_perimeter(a, b):
#         return 2 * (a + b)
#     @staticmethod
#     def rectangle_area(a, b):
#         return a * b
# a = int(input("A tomonni kiriting: "))
# b = int(input("B tomonni kiriting: "))
# c = int(input("C tomonni kiriting: "))
# triangle_perimeter = Figure.triangle_perimeter(a, b, c)
# triangle_area = Figure.triangle_area(a, b, c)
# rectangle_perimeter = Figure.rectangle_perimeter(a, b)
# rectangle_area = Figure.rectangle_area(a, b)
# print(f"Uchburchakning perimetri: {triangle_perimeter}")
# print(f"Uchburchakning yuzasi: {triangle_area}")
# print(f"To'g'ri to'rtburchakning perimetri: {rectangle_perimeter}")
# print(f"To'g'ri to'rtburchakning yuzasi: {rectangle_area}")


"""3.Animal nomli class yozing. 
setattr(), getattr(), hassattr(), delattr() metodlaridan foydalanib, ushbu class ichiga attributlar qo'shing, 
ularni qiymatini ko'ring va ularni o'chiring."""
# class Animal:
#     def __init__(self, ism, ovoz, oyoq):
#         self.ism = ism
#         self.ovoz = ovoz
#         self.oyoq = oyoq
# animal = Animal(ism="Dog", ovoz="Bark", oyoq=4)
#
# setattr(animal, "color", "Brown")
#
# name_value = getattr(animal, "ism")
#
# has_color = hasattr(animal, "color")
#
# delattr(animal, "oyoq")
#
# print(f"Nomi: {name_value}")
# print(f"Rangi bor yoki yo`qligi: {has_color}")
# print(f"Hayvon oyoqlari: {getattr(animal, 'a', 'Oyoq atributi yo`q')}")
#
# print(f"Animal legs: {getattr(animal, 'oyoq', 'Oyoq atributi yo`q')}")
#
# print(f"Name: {name_value}")
# print(f"Color exists: {has_color}")
# print(f"Animal legs: {getattr(animal, 'a', 'No legs attribute')}")
#
# # Atributlarni o'chirildi
# print("After deleting 'legs' attribute:")
# print(f"Animal legs: {getattr(animal, 'a', 'No legs attribute')}")