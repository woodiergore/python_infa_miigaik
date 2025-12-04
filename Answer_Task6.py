print("Задание 1")
a = set("перевертыш")
b = set("баррикада")
print("Первое множество: ", end='')
print(a)
print("Второе множество: ", end='')
print(b)
ab_union = a.union(b)
print("Объединение OR: ", end='')
print(ab_union)
ab_intersection = a.intersection(b)
print("Логическое умножение AND: ", end='')
print(ab_intersection)
ab_dif = a - b
print("Первое минус второе: ", end='')
print(ab_dif)
ba_dif = b - a
print("Второе минус первое: ", end='')
print(ba_dif)
ab_sym_dif = a ^ b
print("Логическое вычитание XOR: ", end='')
print(ab_sym_dif)
print("Проверка на одинаковость множеств: ", end='')
print(a == b)

ab = a | b
print(ab)
almost_dict = set("Съешь ещё этих мягких французских булок, да выпей же чаю")
print(almost_dict)
print(ab)
print(ab & almost_dict)
print(ab - almost_dict)
# Значения ab и ab & almost_dict дают одинаковый (или почти одинаковый) результат,
# потому что множество ab содержит те же буквы, что множество almost_dict.
# Так же множество almost_dict включает в себя почти все буквы русского алфавита,
# поэтому при пересечении ab и almost_dict даст значения в основном из ab.

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
old_data = {'a': 1, 'b': 2, 'c': 3}
new_data = {'b': 2, 'c': 4, 'd': 5}
data_add = set()
data_del = set()
data_edit = set()

for key in new_data:
    if key not in old_data:
        data_add.add(key)
    elif old_data[key] != new_data[key]:
        data_edit.add(key)
for key in old_data:
    if key not in new_data:
        data_del.add(key)

print("Добавлены: ", end='')
print(data_add)
print("Удалены: ", end='')
print(data_del)
print("Изменены: ", end='')
print(data_edit)