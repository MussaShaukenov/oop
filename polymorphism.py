class Country:

    def __init__(self, name):
        self.name = name

    def greet(self, greeting):
        return greeting
    

country_one = Country(name='Казахстан')
country_two = Country(name='Англия')
country_three = Country(name='Франция')

print(country_one.greet('Салам'))
print(country_two.greet('Hello'))
print(country_three.greet('Salut'))

# Один и тот же метод работает по-разному в зависимости от объекта, где он вызван, и данных, которые ему передали.

