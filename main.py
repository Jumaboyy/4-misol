"""2.Figure nomli class yozing.
class ichida uchburchak perimeterini hisoblab beruvchi trianqle perimeter a, b, c), 
uchburchak yuzasini hisiblovchi trianqle yusasi(a. b, c), 
to'g'ri to'rtburchak perimeterini hisoblovchi rectanqle perimeteri(a, b),
to'g'ri to'rtburchak yuzasini hisoblovchi reactangle_area(a, b) nomli metodlar yozing. 
Bu metodlar barchasi static bolsin."""
import math
shakl = str(input("Siz qaysi shaklni yuzasi va perimetrini hisoblamoqchisiz (uchburchak yoki tortburchak): "))
class Figure:
    if shakl == 'uchburchak':
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def perimetri(self):
            return self.a + self.b + self.c

        def yuza(self):
            s = self.perimetri() / 2
            yuza = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return yuza

        a = int(input('Uchburchakni A tomonini kiriting: '))
        b = int(input('Uchburchakni B tomonini kiriting: '))
        c = int(input('Uchburchakni C tomonini kiriting: '))
        uchburchak =Figure(a, b, c)
        print("Uchburchakning perimetri:",uchburchak.perimetri())
        print("Uchburchakning yuzasi: ",uchburchak.yuza())

    elif shakl == 'tortburchak':
class Tortburchak:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def perimetri(self):
            return (self.a + self.b) * 2

        def yuzasi(self):
            return self.a * self.b

        a = int(input('To`rtburchakni A tomonini kiriting: '))
        b = int(input('To`rtburchakni B tomonini kiriting: '))
        tortburchak = To(a,b)
        print("To`rtburchak perimetri", tortburchak.perimetri())
        print('To`rtburchak yuzasi', tortburchak.yuzasi())
#1masala

"""Ushbu classning barcha metodlariqa property decoratorini ulang.
Tashqaridan class objecti orqali bu ma'lumotlarni ko'rish, o'zgartirish va o'chirish imkoni bo'lsin
"""

# class Car:
#     def	(self, model: str, color: str, speed: int, price: int):
#         self.	model = model
#         self.	color = color
#         self.	spead = speed
#         self.	price = price
#2masala






        




