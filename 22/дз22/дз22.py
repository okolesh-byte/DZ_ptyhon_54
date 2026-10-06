filename = "test.txt"
with open(filename, "w") as f:
    f.write("Замена строки в текстовом файле;\n")
    f.write("изменить строку в списке;\n")
    f.write("записать список в файл;\n")

with open(filename, "r") as f:
    lines = f.readlines()

pos1 = 1
pos2 = 2
lines[pos1], lines[pos2] = lines[pos2], lines[pos1]

with open(filename, "w") as f:
    f.writelines(lines)

print("Задание 1. После замены строк:")
for line in lines:
    print(line.strip())

print("-" * 30)

with open(filename, "r") as f:
    lines = f.readlines()

lines.reverse()

with open(filename, "w") as f:
    f.writelines(lines)

print("Задание 2. После реверса строк:")
for line in lines:
    print(line.strip())

print("-" * 30)

file1 = "file1.txt"
file2 = "file2.txt"
file3 = "file3.txt"

with open(file1, "w") as f:
    f.write("Первый файл\n")
with open(file2, "w") as f:
    f.write("Второй файл\n")

with open(file1, "r") as f1, open(file2, "r") as f2:
    content1 = f1.read()
    content2 = f2.read()

with open(file3, "w") as f3:
    f3.write(content1 + content2)

with open(file3, "r") as f3:
    print("Задание 3. Объединенный файл:")
    print(f3.read().strip())