class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    

class Student(Person):

    def __init__(self, name, university):
        # Можно наследовать атрибуты двумя способами
        # Person.__init__(university)
        super().__init__(name)
        self.university = university

    def __str__(self):
        return f'{self.name} учится в университете {self.university}'
    
# Можно создавать классы и объекты, которые похожи друг на друга, но немного отличаются — имеют дополнительные атрибуты и методы.
    

person = Person(name='Азамат')
student = Student(name='Бекзат', university='КБТУ')

print(person)
print(student)

