class BlockOfFlats:
    def __init__(self, floors, apartments, elevators):
        self.__floors = floors
        self.__apartments = apartments
        self.__elevators = elevators

    def number_of_residents(self, value):
        print(f'мы посчитали количесво жильцов и их {self.__apartments * value}')

    def demolition(self, value=0):
        print(f'У нас тут снос, поэтому количество этажей уменьшилось до {self.__elevators * value}')

    def get_floors(self):
        return self.__floors
    def set_floors(self, value):
        if not isinstance(value, int):
            raise ValueError('Этажи должны быть числом')
        self.__floors = value

    def get_apartsments(self):
        return self.__apartments
    def set_apartsments(self, value):
        if not isinstance(value, int):
            raise ValueError('Квартиры должны быть числом')
        self.__apartsments = value

    def get_elevators(self):
        return self.__elevators
    def set_elevators(self, value):
        if not isinstance(value, int):
            raise ValueError('Лифты должны быть числом')
        self.__elevators = value





class BankAccount:
    def __init__(self, name, balance, credits):
        self.__name = name
        self.__balance = balance
        self.__credits = credits

    def removal_of_money(self, value=0.3):
        print(f'У нас обычно снимают 30% от суммы на счёте, поэтому ваш баланс стал равен {self.__balance * value} у.е')

    def increase_of_debt(self, value=1.2):
        print(f'Так как вы брали кредит под 20% годовых, то ваш долг возрос до {self.__credits * value} у.е.')
    def get_name(self):
        return self.__name
    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError('Имя должны быть строкой')
        self.__name = value

    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if not isinstance(value, int):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def get_credits(self):
        return self.__credits
    def set_credits(self, value):
        if not isinstance(value, int):
            raise ValueError('Кредиты должны быть числом')
        self.__credits = value

class Apartment:
    def __init__(self, number_of_zielzov, owner, number_of_rooms):
        self.__number_of_zielzov = number_of_zielzov
        self.__owner = owner
        self.__number_of_rooms = number_of_rooms

    def eviction(self, value = 0):
        print(f'Т.к. вы укрываете протестующих, то их сейчас тут станет {self.__number_of_zielzov * value}')

    def release_rooms(self, value=2):
        print(f'Шо ж, прараб сказал, б****, шо можно сноcить стенку, значит комнат у вас теперь станет {self.__number_of_rooms - value} ёб*** в рот')

    def get_owner(self):
        return self.__owner
    def set_owner(self, value):
        if not isinstance(value, str):
            raise ValueError('Имя должны быть строкой')
        self.__owner = value

    def get_number_of_zielzov(self):
        return self.__number_of_zielzov
    def set_number_of_zielzov(self, value):
        if not isinstance(value, int):
            raise ValueError('М^2 должны быть числом')
        self.__number_of_zielzov = value

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    def set_number_of_rooms(self, value):
        if not isinstance(value, int):
            raise ValueError('Количество комнат должно быть числом')
        self.__number_of_rooms = value


a1 = BlockOfFlats(5, 18, 3)
a1.number_of_residents(5)
a1.demolition()
print(f'У нас в доме {a1.get_floors()} этажей')

Vasya = BankAccount('Vasya', 400, 800)
Vasya.removal_of_money()
Vasya.increase_of_debt()
print(f'Ваш баланс состовляет {Vasya.get_balance()} у.е.')

kv103 = Apartment(5, 'Anton', 5)
kv103.eviction()
kv103.release_rooms()
print(f'Тут проживает один высокоморальный и прекрасный собой  человек по имени {kv103.get_owner()}')