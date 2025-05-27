udělám soubor s koncovkou .sh
ovevřu pomocí nano

v podmince musim mit mezery mezi zavorkami
pri prirazovani nesmim mit mezery (x="neco")

#!/bin/bash == tento soubor ma spustit bash, musi byt na uplne prvnim radku kazdeho bash scriptu

echo "nejaky text" = jako print v pythonu

pristup k promene = "$nazev_promenne"  (ano v uvozockach, je to bezpecnejsi)

read nazev_promenne = ceka na vstup od uzivatele, vlozena hodnota se ulozi do nazev_promenne

if musim uzavrit fi >> podminka se pise do [ [ ] ]
-z >> je zero length 

if [[x == 1]];then 
    >> prikaz ktery se provede kdyz podminka je pravdiva
fi

exit skript ukonci

bash mujskript.sh = udela skript spustileny
