number_of_quests = 15
if number_of_quests > 50:
    print('Идём в ресторан, т.к. нас', number_of_quests, 'персон')
elif number_of_quests >= 20 and number_of_quests <= 50:
    print('Идём в кафе, т.к. нас', number_of_quests, 'персон')
else:
    print('Отпразднуем дома, нефиг деньги трантить, т.к. нас всего лишь', number_of_quests, 'персон')