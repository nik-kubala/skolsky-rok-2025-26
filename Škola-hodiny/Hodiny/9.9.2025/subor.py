fr = open("Škola-hodiny/Hodiny/9.9.2025/3_csv_statistika_podla_paragrafov_3_31.12.2018.csv", "r")

data = []

for riadok in fr:
    riadok_list = riadok.strip().split(",")
    if len(riadok_list) == 24:
        data.append(riadok_list)

data.pop(0)
data.pop(0)
data.pop(0)

for i in data:
    print(i[5])

