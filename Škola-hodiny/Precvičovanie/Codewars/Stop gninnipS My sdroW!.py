def spin_words(sentence):
    zoznam_slov = sentence.split()
    konecna_veta = " "
    for slovo in zoznam_slov:
        if len(slovo) > 4:
            konecna_veta = slovo[::-1] + " "
        else:
            konecna_veta += slovo + " "
    print(konecna_veta)
    #return konecna_veta.strip()

spin_words("Hey wollef sroirraw" )