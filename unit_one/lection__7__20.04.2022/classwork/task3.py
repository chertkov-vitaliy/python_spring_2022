#todo: Модифицировать программу таким образом чтобы она выводила при повторном считывании стр. 5 приветствие "Hello"

f = open("text.txt", "w+t")
f.write("Hello\n")
print(f.read())

f.close()