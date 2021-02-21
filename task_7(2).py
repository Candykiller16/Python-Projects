def inches_to_centimeters(inches): #1
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters): #2
    inches = centimeters / 2.54
    return inches

def miles_to_kilometers(miles): #3
    kilometers = miles * 1.61
    return kilometers

def kilometers_to_miles(kilometers): #4
    miles = kilometers / 1.61
    return miles

def pounds_to_kilograms(pounds): #5
    kilograms = pounds * 0.45
    return kilograms


def kilograms_to_pounds(kilograms): #6
    pounds = kilograms / 0.45
    return pounds

def ounces_to_gram(ounces): #7
    gram = ounces * 28.35
    return gram

def gram_to_ounces(gram): #8
    ounces = gram / 28.35
    return ounces

def gallon_to_liters(gallon): #9
    liters = gallon * 4.55
    return liters

def liters_to_gallon(liters): #10
    gallon = liters / 4.55
    return gallon

def pints_to_litreses(pints): #11
    litreses = pints * 0.57
    return litreses

def litresses_to_pints(litreses): #12
    pints = litreses / 0.57
    return pints

welcom = int(input('Вітаю цябе! Выберы лічбу таго, што ты хочаш зрабіць:'))
while welcom > 0 and welcom <= 12:
    if welcom == 1:
        one = input('Увядзі колькасць :')
        print(inches_to_centimeters(int(one)))
    elif welcom == 2:
        two = input('Увядзі колькасць :')
        print(centimeters_to_inches(int(two)))
    elif welcom == 3:
        three = input('Увядзі колькасць :')
        print(miles_to_kilometers(int(three)))
    elif welcom == 4:
        four = input('Увядзі колькасць :')
        print(kilometers_to_miles(int(four)))
    elif welcom == 5:
        five = input('Увядзі колькасць :')
        print(pounds_to_kilograms(int(five)))
    elif welcom == 6:
        six = input('Увядзі колькасць :')
        print(kilograms_to_pounds(int(six)))
    elif welcom == 7:
        seven = input('Увядзі колькасць :')
        print(ounces_to_gram(int(seven)))
    elif welcom == 8:
        eight = input('Увядзі колькасць :')
        print(gram_to_ounces(int(eight)))
    elif welcom == 9:
        nine = input('Увядзі колькасць :')
        print(gallon_to_liters(int(nine)))
    elif welcom == 10:
        ten = input('Увядзі колькасць :')
        print(liters_to_gallon(int(ten)))
    elif welcom == 11:
        eleven = input('Увядзі колькасць :')
        print(pints_to_litreses(int(eleven)))
    elif welcom == 12:
        twelve = input('Увядзі колькасць :')
        print(litresses_to_pints(int(twelve)))
    elif welcom == 0:
        break
    welcom = int(input('''Калі ласка, увядзіце лік ад 0 да 12 або 0, каб выйсці:'''))







