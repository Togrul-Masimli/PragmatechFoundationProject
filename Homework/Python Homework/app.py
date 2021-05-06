import random
# mesaj = 'Hello World!'
# print(mesaj)

# ad = 'togrul'
# soyad = 'mesimli'

# tam_ad = ad.capitalize() + ' ' + soyad.capitalize()

# print(f'Salam {tam_ad}!')

# x = 2
# y = 5

# print(f'y power x: {pow(x,y)} ')
# print(f'x power y: {pow(y,x)} ')

# z = "4.92"
# z1 = int(float(z))
# print(type(z1))

# degree = int(input())
# if degree < 10:
#     print('Soyuq')
# elif degree == 20:
#     print('Normal')
# elif degree > 30:
#     print('Isti')

# s = 'Programlasdirma'

# if 'x' in s:
#     print('Programlasdirma sozunde "x" var')
# else:
#     print('Programlasdirma sozunde "x" yoxdur')

# str1 = 'Lorem'
# str2 = 'impus'

# str3 = str1 + ' ' + str2
# print(str3)







# Python Homework 2 

# Dairenin sahesi:

# pi = 3.14
# diametr = int(input("Dairenin diametrini daxil edin: "))
# sahe = (pi * pow(diametr,2))/4
# print(f"Dairenin sahesi: {sahe} ")

# 2.

# str1 = """ Sweep through the days Like children that can't stay awake """
# number = int(input("Uzunlugu daxil edin: "))
# if number > len(str1):
#     print("Daxil etdiyiniz deyer text-in uzunlugundan coxdur.")
# elif number < 0:
#     print("False")
# else:
#     print(str1[:number+1])

# 3.
# user_name = input("Adinizi daxil edin: ")
# user_surname = input("Soyadinizi daxil edin: ")
# print(user_name+user_surname+str(random.randint(1, 20))+"gmail.com")

# 4.
# number1 = int(input("Birinci deyer: "))
# number2 = int(input("Ikinci deyer: "))
# operator = input("Operatoru daxil edin: ")

# if operator == "+":
#     print(f"{number1} + {number2} = {number1+number2}")
# elif operator == "-":
#     print(f"{number1} - {number2} = {number1-number2}")
# elif operator == "*":
#     print(f"{number1} * {number2} = {number1*number2}")
# elif operator == "/":
#     print(f"{number1} / {number2} = {number1/number2}")
# elif operator !="+" or operator !="-" or operator !="*" or operator !="/":
#     print("Daxil etdiyiniz deyer riyazi operator deyil.")

# 5.

# n = int(input("Natural eded daxil edin: "))

# if n % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# 6.

# const = 24

# a = int(input("Birici reqemi daxil edin: "))
# b = int(input("Ikinci reqemi daxil edin: "))

# if const % a == 0 and const % b == 0:
#     print("YES")
# else:
#     print("NO")

# 7.

# n_7 = int(input())

# if n_7 < 0:
#     print("Negative")
# elif n_7 == 0:
#     print("Zero")
# else:
#     print("Positive")

# 7.1.

# side1 = int(input("Birinci teref: "))
# side2 = int(input("Ikinci teref: "))
# side3 = int(input("Ucuncu teref: "))

# if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#     print("YES")
# else:
#     print("NO")

# 8.

# mark = int(input("Qiymetinizi daxil edin: "))

# if 1 <= mark <= 3:
#     print("Initial")
# elif 4 <= mark <= 6:
#     print("Average")
# elif 7 <= mark <= 9:
#     print("Sufficient")
# elif 10 <= mark <= 12:
#     print("High")
# else:
#     print("Daxil etdiyiniz qiymet teyin olunmayib.")

# 9.

# n9 = int(input())
# print(n9-1)

# 10.

# n10_1 = int(input())
# n10_2 = int(input())
# tam_hisse = int(n10_1/n10_2)

# print(f"{n10_1} / {n10_2} : \t Tam hisse: {tam_hisse} \t Kesr hisse: {n10_1 % n10_2}")

# 11.

# n11 = int(input("Reqemi daxil edin: "))
# print(n11*-1)

# 12.

# num = int(input())
# sum = 0

# while num > 0:
#     deyer = num % 10
#     sum = sum + deyer
#     num //= 10

# print(pow(sum, 2))

# 13.

# name = input("Adinizi daxil edin: ")

# if len(name) < 3 or len(name) > 11:
#     print("Adinizin uzunlugu 3 den az 11 den cox ola bilmez.")
# else:
#     surname = input("Soyadinizi daxil edin: ")
#     if len(surname) < 5 or len(surname) > 15:
#         print("Soyadinizin uzunlugu 5 den az 15 den cox ola bilmez.")
#     else:
#         birth_year = input("Dogum ilinizi daxil edin: ")
#         if len(birth_year) != 4:
#             print("Dogum ilinizi 4 mertebeli reqemden yuxari ola bilmez.")
#         else:
#             email = input("Email-inizi daxil edin: ")
#             if len(email) < 10 or len(email) > 22:
#                 print("Emailinizin uzunlugu 10 dan az 22 den yuxari ola bilmez.")
#             elif not(email.endswith("@gmail.com")):
#                 print('Emailinizin sonu "@gmail.com" la bitmelidir.')
#             else:
#                 password = input("Parolunuzu daxil edin: ")
#                 if len(password) < 6 or len(password) > 13:
#                     print("Kod 6-13 arasi uzunluqda olmalidir.")
#                 else:
#                     password1 = input("Parolunuzu tesdiq edin: ")
#                     if password != password1:
#                         print("Tesdiqleme parolu parolla eyni deyil")
#                     else:
#                         print("Qeydiyyat tamamlandi!")
#                         print("Qeydiyyat detallarina baxmaq isteyirsiz?")
#                         answer = input()
#                         if answer == "he":
#                             print("==========================================================================")
#                             print(f"Ad: {name} Soyad: {surname} Yas: {2021 - int(birth_year)} Email: {email} Parol: {password}")
#                             print("==========================================================================")
#                         elif answer == "yox":
#                             print(f"{name} {surname}, Ugurlar!")


# Homework 3

# 1.

# mylist = [1,2,3,4,5,6]
# cem = 0

# for x in mylist:
#     cem = cem + x

# print(cem)

# 2.

# mylist = [1,2,15,4,5,6]
# maximum = 0

# for x in mylist:
#     if x > maximum:
#         maximum = x
    
# print(maximum)

# 3.

# mylist = [5,2,15,4,1,6]
# minimum = mylist[0]

# for x in mylist:
#     if x < minimum:
#         minimum = x
    
# print(minimum)

# 4.

# mylist = ['abc', 'xyz', 'aba', '1221']

# for x in mylist:
#     if len(x) >= 2 and x[0] == x[-1]:
#         print(x)

# 5.

# mylist = []

# if bool(mylist):
#     print("List is not empty")
# else:
#     print("List is empty")

# 6.

fruits = ("apple","cherry", "blackberry", "banana", "kiwi")

for x in fruits:
    print(x)

print("============")

fruits_list = list(fruits)
fruits_list[1:4] = ["mango", "tea", "coffee"]
fruits = tuple(fruits_list)

for x in fruits:
    print(x)
# 7.

# mylist = ["Togrul","Ahmed","admin","Fuad","Elnur"]

# for name in mylist:
#     if name == "admin":
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {name}, thank you for logging in again.")