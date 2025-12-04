print("Задание 1")
n = input("Введите своё Имя: ")
s = input("Введите свою Фамилию: ")

sn = s + "\n" + n + "\n"
print(sn * 10)

print()
print("Задание 2")
birthday = int(input("Введите свою дату рождения в формате YYYYMMDD: "))

print(birthday % 100)
print(birthday % 10000 // 100)
print(birthday // 10000)