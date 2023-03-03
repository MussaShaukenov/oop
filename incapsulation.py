class Worker:

    # Добавляем новый приватный атрибут __salary
    # Чтобы объявить приватный атрибут надо поставить '__' перед переменной
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.__salary = salary

    def change_job(self, new_job) -> str:
        self.job = new_job

    def __str__(self) -> str:
        return f'{self.name} работает на должности "{self.job} с зп {self.__salary}"'

person_one = Worker(name='Азамат', job='Разработчик', salary='5000 тенге')
person_two = Worker(name='Ерлан', job='Директор', salary='10000 тенге')

print(person_one)
print(person_two)

print(person_one.__salary)
print(person_two.__salary)

# Для внешних объектов доступны только публичные атрибуты и методы. 