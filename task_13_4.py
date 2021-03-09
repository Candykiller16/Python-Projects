class Car:
    def __init__(self, marka, model, year_of_release, speed = -10 ):
        self.__marka = marka
        self.__model = model
        self.__release = year_of_release
        self.__speed = speed

    def __increase(self):
        self.__speed += 10
        print(f' Ты дал газку и твоя скорость {self.__speed} км/ч')
        if self.__speed <=0:
            raise ValueError('Ты не можешь давать газку с отрицательной скоростью')
                    
    def __reduce(self):
        self.__speed -= 5
        print(f' Ты сбавил обороты и твоя скорость(против тебя) {self.__speed} км/ч(%)')
        if self.__speed <=0:
            raise ValueError('У тебя скорость меньше 0, как ты можешь её ещё уменьшить')
    def __stop(self):
        self.__speed = 0
        print(f' Ты тормозишь и твоя скорость {self.__speed} км/ч. Не тормози, сникерс сни')
        
    def __show_speed(self):
        print(f'Ваша скорость {self.__speed} км/ч')
        if self.__speed <=0:
            raise ValueError('Проблема либо с тобой, либо с твоим спидометром')
    def __changes(self):
        self.__speed *= -1
        print(f'Ты разворачиваешься и по законам физики твоя скорость {self.__speed} км/ч')
        if self.__speed >=0:
            raise ValueError('Слишком хорошо разовачиваешься, разгоняясь')

car1 = Car('Tesal', 'modelX', 2012)
#car1._Car__increase()
#car1._Car__reduce()
#car1._Car__stop()
#car1._Car__show_speed()
car1._Car__changes()
