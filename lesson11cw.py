# info = {"x": 10, "y": 30, "player_speed": "medium"}
# if info["player_speed"] == "medium":
#     x_increment = 2
# elif info["player_speed"] == "fastest":
#     x_increment = 10
# else:
#     x_increment = 1
# info["x"] += x_increment
# print(f"Новая позиция игрока: {info['x']}")


language = {
    "aleksey": "python",
    "ilya": "c++",
    "xlebich": "js",
    "vanya": "python(crutoy)",
    "nikiton": "php"
}
print(
    f"Я люблю программировать на {language['aleksey'].title()} языке программирования")
for i, g in language.items():
    print(
        f"Меня зовут {i.title()}.Я люблю программировать на {g} языке программирования")

# .keys() .values()

# list_huge = []
# for i in range(30):
#     info = {
#         "color": "yellow",
#         "points": "15"
#     }
#     list_huge.append(info)
#     print(f"{list_huge}")
# for x in list_huge:
#     print(x)
#     print(f"Количсетво игроков {len(list_huge)}")
# for p in list_huge[0:3]:
#     if p["color"] == "yellow":
#         p["color"] = "blue"
#         p["points"] = 100


# list_huge = []
# for i in range(30):
#     info = {
#         "color1": "yellow",
#         "points": 15
#     }
#     list_huge.append(info)
#     print(f"{list_huge}")
# for p in list_huge[0:3]:
#     if p["color1"] == "yellow":
#         p["color1"] = "blue"
#         p["points"] = 100
# for x in list_huge:
#     print(x)
# print(f"кол-во игроков {len(list_huge)}")
