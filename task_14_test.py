class Car:
    def __init__(self, marka, model, year_of_release, speed=0):
        self.__marka = marka
        self.__model = model
        self.__release = year_of_release
        self.__speed = speed

    def increase(self):
        # print(f' Ты дал газку и твоя скорость {self.__speed} км/ч')
        if self.__speed <= 0:
            raise ValueError('Ты не можешь давать газку с отрицательной скоростью')
        else:
            return self.__speed + 10


    def reduce(self):
        # print(f' Ты сбавил обороты и твоя скорость(против тебя) {self.__speed} км/ч(%)')
        if self.__speed < 0:
            raise ValueError('У тебя скорость меньше 0, как ты можешь её ещё уменьшить')
        else:
            return self.__speed - 5

    def stop(self):
        if self.__speed != 0:
            return self.__speed == 0
        else:
            print('Ты и так стоишь')

    def show_speed(self):
        if self.__speed <= 0:
            raise ValueError('Проблема либо с тобой, либо с твоим спидометром')
        else:
            return self.__speed

    def changes(self):
        if self.__speed != 0:
            return self.__speed * -1
        else:
            return f'Ты же стоишь'

