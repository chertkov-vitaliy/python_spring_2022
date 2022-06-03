# todo: 1 Реализовать итератор на базе класса Person.

class Profile:
    def __init__(self,  id, login,  password,  name,  age):
        self.id = id
        self.login = login
        self.__password = password
        self.name = name
        self.age = age


# Объект класса должен итерироваться циклом for
obj = Profile( 1, "admin", 123456, "Peter", 25 )
for i in obj:
    # функция должна выводить название и значение атрибута
    print(i)

2 Реализовать генератор на базе класса Profile. При итерировании циклом метод
должен выводить название и значение атрибута

3 Реализовать контекстный менеджер над DB . Класс должен возвращать соединение с БД