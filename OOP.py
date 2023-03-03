# Класс Worker это схема/шаблон для создания объектов, которые имеют два атрибута: имя и задание.
class Worker:

    # Необходимо проинициализировать переменные 
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # Метод класса который меняет должность рабочего
    def change_job(self, new_job) -> str:
        self.job = new_job

    def __str__(self) -> str:
        return f'{self.name} работает на должности "{self.job}"'

# Создаем объекты класса
person_one = Worker(name='Азамат', job='Разработчик')
person_two = Worker(name='Ерлан', job='Директор')

print(person_one)
print(person_two)

person_one.change_job(new_job='Старший разработчик')

print(person_one)






        