import re

text = "123456@i.ru, 123_456@ru.name.ru, login1@i.ru, login-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"

pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)

print(emails)