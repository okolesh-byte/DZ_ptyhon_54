import os
from datetime import datetime

path = input("Введите путь к файлу или папке: ")

if not os.path.exists(path):
    print("Указанный путь не существует.")
else:
    abs_path = os.path.abspath(path)
    print(f"Абсолютный путь: {abs_path}")

    if os.path.isfile(path):
        print("Тип объекта: Файл")
        size = os.path.getsize(path)
        print(f"Размер: {size} байт ({round(size / 1024, 2)} КБ)")

        mtime = os.path.getmtime(path)
        time_str = datetime.fromtimestamp(mtime).strftime('%d.%m.%Y %H:%M:%S')
        print(f"Время последнего изменения: {time_str}")
    elif os.path.isdir(path):
        print("Тип объекта: Директория")