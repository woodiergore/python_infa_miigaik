birthday = int(input("Введите свою дату рождения в формате YYYYMMDD: "))

print(birthday % 100)
print(birthday % 10000 // 100)
print(birthday // 10000)