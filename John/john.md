vezme zašiforvaná hesla a snaží se je rozluštit

1. slovníkový - wordlist
2. brute-force - všechny možné kombinace
3. hybrid - slovník, číslovaní, permutace

použití - john (název souboru s hash.txt) --wordlist=(cesta k wordlistu.txt)

john --show password.txt - ukáže jména a hesla které prolomil

john --show password.txt > vystup.txt (jména a hesla uloží do .txt, PŘEPÍŠE)
john --show password.txt >> vystup.txt (NEPŘEPÍŠE)
