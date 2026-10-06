import os

os.makedirs("Work/F1", exist_ok=True)
os.makedirs("Work/F2/F21", exist_ok=True)

with open("Work/w.txt", "w") as f:
    f.write("Текст в w.txt")
with open("Work/F1/f12.txt", "w") as f:
    f.write("Текст в f12.txt")
with open("Work/F2/F21/f211.txt", "w") as f:
    f.write("Текст в f211.txt")
with open("Work/F2/F21/f212.txt", "w") as f:
    f.write("Текст в f212.txt")

print("Обход Work снизу вверх")
for root, dirs, files in os.walk("Work", topdown=False):
    print(root)
    print(dirs)
    print(files)

print()
print("-" * 40)
print()

print("Обход Work сверху вниз")
for root, dirs, files in os.walk("Work", topdown=True):
    print(root)
    print(dirs)
    print(files)