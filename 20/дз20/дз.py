import re

passwords = ["my-p@ssw0rd", "short", "toolongpassword123456789", "bad password!"]
for pwd in passwords:
    pattern = r"^[a-zA-Z0-9_@-]{6,18}$"
    if re.match(pattern, pwd):
        print(f"Пароль '{pwd}' подходит")
    else:
        print(f"Пароль '{pwd}' не подходит")

print()

text = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)
print(dates)