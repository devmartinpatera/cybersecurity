Tento Python skript slouží k automatickému spuštění nástroje John the Ripper pro crackování hashů pomocí wordlistu.
Uživatel je postupně vyzván k zadání:

Cesty k souboru s hashi

Cesty k wordlistu (nebo může zvolit x pro přednastavený rockyou.txt)

Skript obsahuje ochranu proti prázdnému vstupu a umožňuje kdykoli zadat exit pro ukončení.
Po zadání platných cest automaticky spustí john a následně vypíše nalezená hesla (john --show).

Chybí dodělat:  validace vstupů
                output do souboru
