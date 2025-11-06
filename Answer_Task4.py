print("6 ноября 2025")
print("ЗАДАНИЕ 1")
a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))

for i in range(b):
    for j in range(a):
        print("*", end='')
    print()

print()
print("ЗАДАНИЕ 2")
for i in range(2, 10):
    for j in range(2, 10):
        if i%2==0 or j%2==0:
            continue
        elif i*j >= 50:
            break
        elif i*j == 25:
            pass
        else:
            print(f'{i} * {j} = {i*j}')

print()
print("ЗАДАНИЕ 3")
c = 0
pass1 = "OLeg"
pass2 = ""

for p in pass1:
    pc = ord(p)
    i = ord('A')
    while (i != pc):
        i = i + 1
        c = c + 1
    pass2 = pass2 + chr(i)

print("Подобран пароль: " + pass2)
print(f"Число попыток: {c}")