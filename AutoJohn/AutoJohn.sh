#!/bin/bash

echo "Zadej cestu k souborm s hash:"
echo "napis --exit-- pro ukonceni"
read hash_soubor

if [[ -z $hash_soubor ]]; then
	echo "chyba spatny vstup"
	exit
elif [[ $hash_soubor == "exit" ]]; then
	echo "ukoncuji"
	exit
fi

echo "zadej cestu k wordlistu (x = rockyou.txt)"
echo "napis --exit-- pro ukonceni"

read wordlist_soubor

if [[ $wordlist_soubor == "x" ]]; then
	wordlist_soubor="/usr/share/wordlists/rockyou.txt"
elif [[ $wordlist_soubor == "exit" ]]; then
	echo "ukoncuji"
	exit
fi
 
john $hash_soubor  --wordlist=$wordlist_soubor
john --show $hash_soubor 




