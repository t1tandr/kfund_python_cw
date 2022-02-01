# n = 1
# x = 10

# while x <= 20:
#     x = x*1.1
#     n+=1

# print(n)

#zadacha 2
# x = 1
# while x <= 10:
#     y = x**2
#     print(f'При Х ={x} , У ={y}')
#     x = x + 1

#zadacha 3
# x = 1
# s = 0
# n = int(input('Введите значение для Н: '))
# while x <= n:
#     s = s + x
#     x = x + 1

# print(s)

#Вычислить факториал числа к

k = int(input('Введите число, факториал которого будет равнятся К: '))
k0 = k
s = 1
while k >= 1:
    s = s*k
    k -= 1
print(f'Факториал числа {k0} равняется {s}')