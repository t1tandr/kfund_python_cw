list = [['abc', 'abf', 'fddsfd'], 'ajskhdka', 'askjdfalkd' ,['abc', 'abf', 'fddsfd']]

for i in list:
    if i == list():
        for a in i:
            print(a)
    if i == list[0]:
        continue
    print(i)

a = (2, 50)
print(a[0])

dimensions = (200, 250)
dimensions = (230, 250)
print(dimensions)

i = int(input)

numbers = []
k = 0
n = int(input("Введите кол-во чисел: "))
while True:
    a = int(input("Введите значение: "))
    numbers.append(a)
    if len(numbers) >= n:
        break
for i in numbers:
    k += i
print(k)

user = {
    "u1": "Человек",
    "u2": "Супергерой"
}
new_user = user["u2"]
message = f"Ты прошел игру, теперь ты {new_user}"
print(message)
print(user)
user["u3"] = "Волк"
user["u4"] = "Лиса"
print(user)
