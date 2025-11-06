print("ЗАДАНИЕ 1")
t0 = int(input("Вчерашняя температура: "))
t1 = int(input("Сегодняшняя температура: "))

if (t1>t0):
    print("Сегодня теплее, чем вчера")
elif (t1<t0):
    print("Сегодня холоднее, чем вчера")
else:
    print("Сегодня такая же температура, как и вчера")

print()
print("ЗАДАНИЕ 2")
age = int(input("Сколько вам лет? "))
student = input("Вы студент? ")
job = input("Вы работаете? ")

print("Вы - ", end='')
if (age < 18):
    print("не", end='')
print("совершеннолетний ", end='')
if (job == "да"):
    print("работающий ", end='')
elif (job == "нет"):
    print("безработный ", end='')
if (student == "нет"):
    print("не", end='')
print("студент.")