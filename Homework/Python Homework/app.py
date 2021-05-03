mesaj = 'Hello World!'
print(mesaj)

ad = 'togrul'
soyad = 'mesimli'

tam_ad = ad.capitalize() + ' ' + soyad.capitalize()

print(f'Salam {tam_ad}!')

x = 2
y = 5

print(f'y power x: {pow(x,y)} ')
print(f'x power y: {pow(y,x)} ')

z = "4.92"
z1 = int(float(z))
print(type(z1))

degree = int(input())
if degree < 10:
    print('Soyuq')
elif degree == 20:
    print('Normal')
elif degree > 30:
    print('Isti')

s = 'Programlasdirma'

if 'x' in s:
    print('Programlasdirma sozunde "x" var')
else:
    print('Programlasdirma sozunde "x" yoxdur')

str1 = 'Lorem'
str2 = 'impus'

str3 = str1 + ' ' + str2
print(str3)