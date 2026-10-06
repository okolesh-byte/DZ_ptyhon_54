ids = ["1441751072", "6384137383", "8186377272", "7194236131", "3313812937"]
names = ["ebegbqa", "daeefed", "bdbqeab", "gafdbee", "gbfddgq"]
tels = ["7979251508", "6253294228", "9543402193", "6265065413", "5668240979"]

result = {}
for i in range(len(ids)):
    result[ids[i]] = {
        "name": names[i],
        "tel": tels[i]
    }

for key, value in result.items():
    print(f'"{key}": {{')
    print(f'    "name": "{value["name"]}",')
    print(f'    "tel": "{value["tel"]}"')
    print("},")