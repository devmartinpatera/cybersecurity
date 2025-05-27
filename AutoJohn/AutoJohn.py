import subprocess

import sys

def konec():
    print("Ukončuji program")
    sys.exit()

while True: #nekonečná smyčka, ukončená pouze break
    print("Zadej cestu k souborům s hash:")
    print("Zadej \"exit\" pro ukončení")

    hash_soubor = input().strip()

    if hash_soubor == "":
        print("Chyba - prázdný input")
        print("Zadej cestu k souborům s hash:")

    elif hash_soubor == "exit":
        konec()

    else:
        break

while True: #nekonečná smyčka, ukončená pouze break
        print("Zadej cestu k wordlistu: (x = pro rockyou.txt)")
        print("Zadej \"exit\" pro ukončení")

        wordlist_soubor = input().strip()

        if wordlist_soubor == "x":
            wordlist_soubor = "/usr/share/wordlists/rockyou.txt"
            subprocess.run(["john", hash_soubor, "--wordlist="+ wordlist_soubor])
            print("-------------------------------------------------------------")
            subprocess.run(["john", "--show",hash_soubor ])
            break
        elif wordlist_soubor == "exit":
            konec()

        elif wordlist_soubor == "":
            print("Chyba - prázdný input")
            print("Zadej cestu k souborům s hash:")

        else:
            subprocess.run(["john", hash_soubor, "--wordlist="+ wordlist_soubor])
            print("-------------------------------------------------------------")
            subprocess.run(["john", "--show",hash_soubor ])



