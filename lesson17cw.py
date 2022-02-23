from turtle import done


# list = ['for dogs', 'landing', 'for offers', 'for sales', 'for game', 'navigator']
# done_list = []
# def function():
#     while list:
#         a = list.pop(0)
#         print(f'{a} в разработке')
#         done_list.append(a)
#         print(done_list)
#     for i in done_list:
#         print(f'{i} готов!')
# function()


def pizza(*b):
    for i in b:
        print(f'I like {i}')
pizza('amerikanka', 'firmennaya')