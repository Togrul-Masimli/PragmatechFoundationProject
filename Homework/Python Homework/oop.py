class Person():
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self,tamad):
        name, surname = tamad.split(' ')
        self.name = name
        self.surname = surname




p1 = Person('Togrul','Masimli')
print(p1.fullname)

p1.name = 'John'
p1.surname = 'Doe'
print(p1.fullname)

p1.fullname = 'Corey Schafer'
print(p1.name)
print(p1.surname)
print(p1.fullname)
    