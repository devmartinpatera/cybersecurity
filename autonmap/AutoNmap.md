🔍 Nmap Scanner – Python Script
Tento jednoduchý Python skript umožňuje provést základní port scanning cílové IP adresy nebo hostitele pomocí knihovny python-nmap, která je wrapperem pro nástroj Nmap.

✅ Funkce
Naskenuje cílový hostitel pomocí nmap -sV (detekce verzí služeb).

Vypíše:

IP adresu hostitele

Stav hostitele (např. up, down)

Protokoly (tcp, udp)

Otevřené porty a jejich stav

Název služby, použitý software a jeho verzi (pokud je dostupná)

▶️ Jak skript funguje
Načtení IP adresy od uživatele:
Uživatel zadá cílovou IP adresu nebo hostname ke skenování.

Skenování pomocí Nmap:
Skript spustí nmap -sV na zadanou IP adresu – zjišťuje aktivní porty a verze běžících služeb.

Zpracování výsledků:

Projde všechny nalezené hostitele.

Zjistí aktivní protokoly (tcp, udp).

Vypíše informace o každém nalezeném portu.

💻 Ukázka výstupu
yaml
Copy
Edit
Enter a target location:
192.168.1.1
Host: 192.168.1.1
State: up
Protocol: tcp
Port: 22 State: open ssh,OpenSSH,7.9
Port: 80 State: open http,Apache httpd,2.4.41
🛠 Požadavky
Python 3.x

Nmap musí být nainstalovaný v systému

Python knihovna python-nmap

bash
Copy
Edit
pip install python-nmap