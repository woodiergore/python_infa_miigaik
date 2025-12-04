print("Задание 1")

print()

print("Задание 2")
num = {}
i = 1
while i < 6:
    i2 = i*i
    n = {i: i2}
    num.update(n)
    i += 1
for n1, n2 in num.items():
    print(n1, n2)
print()

print("Задание 3")