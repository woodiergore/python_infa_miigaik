print("Задание 1.")
words = ["яблоко", "апельсин", "банан"]
for i in range(len(words)):
    if i == 0:
        words[i] = words[i].capitalize()
    print(words[i], end='')
    if i+1 != len(words):
        print(", ", end='')
    else:
        print(".")

print()
print("Задание 2.")
my_list = [10, 20, 30, 40, 50]
my_list.pop(4)
my_list.pop(1)
my_list.pop(0)
for i in my_list:
    print(i)

print()
print("Задание 3.")
numbers = [1, 2, 3, 4, 5]

