user = ['u1', 'u2', 'u3', 'u4']

user_v = []
i = 0

while len(user) > 0:
    u = user.pop(0)
    user_v.append(u)
print(user_v)
print(user)