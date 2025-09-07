fr = open("C:/Users/Notebook/Documents/Py/Škola-hodiny/2.9.2025/hada.txt", "r")
fw = open("C:/Users/Notebook/Documents/Py/Škola-hodiny/2.9.2025/zapis.txt", "w")

counter = 1
row_counter = 0
row_lenght = 0
row_short = float('inf')

for riadok in fr:
    row_counter += 1
    if len(riadok) < row_short:
        row_short = len(riadok.strip())
    if len(riadok) > row_lenght:
        row_lenght = len(riadok)
    for i in range(1, len(riadok)):
        if riadok[i] == riadok[i - 1]:
            counter += 1
        else:
            fw.write(riadok[i - 1] + str(counter) + " ")
            counter = 1
fw.write("\n")
print(f"Najdlhsia hra bola {row_lenght}")
print(f"Najkratsia hra bola {row_short}")
fw.close()