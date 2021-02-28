class Car:
    def __init__(self, marka, model, year_of_release, speed = 0 ):
        self.__marka = marka
        self.__model = model
        self.__release = year_of_release
        self.__speed = speed

    def __increase(self , increase):
        print(f' Ты дал газку и твоя скорость {self.__speed + increase} км/ч')

    def __reduce(self, start, reduce):
        print(f' Ты сбавил обороты и твоя скорость(против тебя) {start - reduce} км/ч(%)')
    def __stop(self, decrese):
        print(f' Ты тормозишь и твоя скорость {decrese * 0} км/ч. Не тормози, сникерс сни')
    def __show_speed(self, speedi):
        print(f'Ваша скорость {speedi} км/ч')
    def __changes(self, speedy):
        print(f'Ты разворачиваешься и по законам физики твоя скорость {-(speedy)} км/ч')

car1 = Car('Tesal', 'modelX', 2012, )
car1._Car__increase(26)
car1._Car__reduce(100, 3)
car1._Car__stop(10)
car1._Car__show_speed(10)
car1._Car__changes(15)
