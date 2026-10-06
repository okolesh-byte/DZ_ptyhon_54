import csv

data = [
    ["hostname", "vendor", "model", "location"],
    ["sw1", "Cisco", "3750", "London"],
    ["sw2", "Cisco", "3850", "Liverpool"],
    ["sw3", "Cisco", "3650", "Liverpool"],
    ["sw4", "Cisco", "3650", "London"]
]

with open("data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(data)

print("Даные успешно записаны в файл data.csv")
print("-" * 35)

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(f"{row[0]} - {row[1]} {row[2]} ({row[3]})")