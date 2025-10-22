print("ЗАДАНИЕ 5")
n = int(input("Введите число: "))
i = 1
while i < 11:
    print(f"{n}*{i}={n*i}")
    i += 1
print()
for i in range(1, 11):
    print(f"{n}*{i}={n * i}")
print(1)
print("ЗАДАНИЕ 6")
for i in range(11):
    print(i, end=" ")
print()
for i in range(10, -1, -1):
    print(i, end=" ")
print()
for i in range(10, -1, +1):
    print(i, end=" ")