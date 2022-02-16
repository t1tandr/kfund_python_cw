#1 ex

# browsers = {
#     'opera': '4.44',
#     'chrome': '40.5',
#     'safari': '12.53',
#     'firefox': '2.46'
# }
# for i, g in browsers.items():
#     print(f'Браузер {i.title()} использует {g} процента(-ов) населения нашей планеты')

# 2 ex

# voc = {
#     'today': 'Помыть посуду',
#     'tomorrow': 'Поскладывать вещи',
#     'today': 'Помыть обувь',
#     'tomorrow': 'Написать сочинение',
#     'today': 'Сделать домашнюю работу',
#     'tomorrow': 'Позвонить бабуле <3',
# }
# today = []
# tomorrow =[]

# for i, g in voc.items():
#     print(f'{i} {g}')
#     # if i == 'today':
#     #     # today.append(g)
#     #     print(g)
#     # else:
#     #     tomorrow.append(g)
# # print(today)

# 3 ex
# users ={
#     '532149': 'nick',
#     '129875': 'jack',
#     '647895': 'oleg',
#     '': 'dima',
#     '23789': 'yana',
# }
# for i, g in users.items():
#     if i != '':
#         print(f'Hello, {g.title()}. \nYour code: {i}')
#     else:
#         print(f'Hi, {g.title()}. \nYou have not got your code (((')

# 4 ex

# obj = {
#     'book': 1,
#     'pistol': 15,
#     'pen': 3,
#     'shoes': 2,
# }
# for i, g in obj.items():
#     if g <= 1:
#         print(f'Hi! You have {g} {i}')
#     else:
#         print(f'Hi! You have {g} {i}s')

# 5 ex

# number = int(input('ВВедите число: '))
# voc = {}

# for i in range(number+1):
#     voc[i] = i**2
# # print(voc)
# for i, g in voc.items():
#     print(f'Квадрат числа {i} = {g}')

# 6 ex

# voc = {
#     'Спорт': 'FIFA',
#     'Прикоючения': 'STALKER',
#     'Шутер': 'CS:GO'
# }
# for i, g in voc.items():
#     print(f'В жанре {i}, мне очень нравится игра {g}')

# 7 ex

# voc = {
#     'Den1': '18.05.2004',
#     'Den2': '31.12.1998',
#     'Den3': '01.01.2001',
#     'Den4': '08.03.2000',
# }
# date = input('ВВедите дату в формате dd.mm.yyyy: ')
# for i, g in voc.items():
#     if g == date:
#         print(f'В этот день родился: {i}')

# 8 ex

# voc = {
#     'огурец': 'зеленый длинный',
#     'помидор': 'красный круглый',
#     'слива': 'Круглая сладкая',
#     'пирог': 'Вкусный',
# }
# a = input('ВВедите название продукта: ')
# for i in voc.keys():
#     if i == a:
#         print(f'{i.title()} есть в холодильнике!')
#     else:
#         print('К сожалению, такой продукт отсутствует')

# 9 ex

# cities = {
#     'киев': 'столица Украины, исторический город',
#     'варшава': 'Столица Польши, старинный город',
#     'харьков': 'первая столица Харькова, любимый город',
# }
# for i,g in cities.items():
#     print(f'{i.title()} - {g}')