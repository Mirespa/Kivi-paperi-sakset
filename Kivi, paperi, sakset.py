p1_pisteet = 0
p2_pisteet = 0

while True:
    p1 = input("Pelaaja 1 valinta: ")
    if p1 != "":
        p2 = input("Pelaaja 2 valinta: ")
    if p1 == "":
        break
    if p1 == "kivi":
        if p2 == "paperi":
            p2_pisteet += 1
            print("Pelaaja 2 voitti")
        elif p2 == "sakset":
            p1_pisteet += 1
            print("Pelaaja 1 voitti")
        else:
            print("Tasapeli")
    if p1 == "paperi":
        if p2 == "sakset":
            p2_pisteet += 1
            print("Pelaaja 2 voitti")
        elif p2 == "kivi":
            p1_pisteet += 1
            print("Pelaaja 1 voitti")
        else:
            print("Tasapeli")
    if p1 == "sakset":
        if p2 == "kivi":
            p2_pisteet += 1
            print("Pelaaja 2 voitti")
        elif p2 == "paperi":
            p1_pisteet += 1
            print("Pelaaja 1 voitti")
        else:
            print("Tasapeli")

print("Peli loppui")
print(f"pelaaja 1 sai {p1_pisteet} pistettä")
print(f"pelaaja 2 sai {p2_pisteet} pistettä")