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