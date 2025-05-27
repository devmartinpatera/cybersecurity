import nmap 

print("Enter a target location:")
ip_adress = input()  
ip_adress = ip_adress.strip()  

# Vytvoří instanci třídy PortScanner, která umožňuje provádět skenování
scanner = nmap.PortScanner()

scanner.scan(ip_adress, arguments="-sV") # sken ip adresy, -sV zjistuje i sluzby a verze


for host in scanner.all_hosts():    # Projde všechny nalezené hosty (většinou jen jeden, ale může být více) 
    # v host je IP adresa
    print("Host:", host)  # Vypíše IP adresu hostitele
    print("State:", scanner[host].state())  # Vypíše stav hostitele (např. "up", "down")

    for proto in scanner[host].all_protocols():    # Projde všechny protokoly, které byly detekovány (např. "tcp", "udp")

        print("Protocol: ", proto)  # Vypíše typ protokolu

        ports = scanner[host][proto].keys()  # Získá všechny porty pro daný protokol .keys() bere vsechny klice ze slovniku

        for port in ports:         # Projde každý port a vypíše jeho číslo a stav (např. "open", "closed")


            # Pokusíme se získat název služby a verzi, pokud jsou dostupné
            service = scanner[host][proto][port].get('name', 'unknown') #key(co chci ziskat, co kdyz neexistuje)
            product = scanner[host][proto][port].get('product', '')
            version = scanner[host][proto][port].get('version', '')
            
            service_info = f"{service},{product},{version}".strip()

            print("Port: ", port, "State: ", scanner[host][proto][port]['state'], service_info)

