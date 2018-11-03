Dokumentace ukol_1

Program pro výpočet polohy jednotlivých poledníků a rovnoběžek v daném zobrazení

Program provede výpočet souřadnic poledníků a rovnoběžek pro zvolené zobrazení, měřítko a poloměr Země. Vypíše, na jakých souřadnicích na papíře se dané poledníky a rovnoběžky nacházejí.



Vstupní parametry: 
   Měřítko:      nutné zadat celočíselný, kladný formát čísla x, který bude odpovídat měřítku 1:x.
   Zobrazení:    program může provádět vypočet souřadnic na čtyřech různých zobrazeních. Je nutné zadat, pro které zobrazení se mají
                 rovnoběžky a poledníky počítat (možnosti: L-Lambert,A-Marini,B-Braun,M-Mercator).
   Poloměr Země: nutný kladný formát čísla, poloměr se udává v kilometrech, pokud uživatel zadá hodnotu 0 program bude počítat s poloměrem                  6371.11 km.
  
  
  
Výstupní  parametry:
   Poledníky:     výpočet souřadnic na papíře pro poledníky v daném zobrazení v cm
   Rovnoběžky:    výpočet souřadnic na papíře pro rovnoběžky v daném zobrazení v cm
   
   Pokud je hodnota souřadnic vyšší než jeden metr, zobrazí se místo čísla pomlčka. 
   
   
   
Běh programu:
   Nejprve jsou od uživatele vyžádany všechny vstupní parametry a jsou hned ošetřeny před případnými chybami. Pokud uživatel zadá chybně vstupní parametry, program to zahlásí a vyžádá si daný vstupní parametr znovu. Funkce: zadani_osetreni_polomeru(), zadani_osetreni_meritka(), zadani_osetreni_pismeneproZobr() - nemají žádné vstupy, výstupem jsou korektní hodnoty.
   Dále je jak u poledníků, tak i u rovnoběžek vytvořen list hodnot po deseti stupních a prázdný list, do kterého se budou zapisovat výpočty. Jsou provedeny výpočty. U poledníků jsou všechny výpočty konstantní, u rovnoběžek záleží na vstupním parametru zobrazení. Ve funkci je definována podmínka: pokud výsledná hodnota překročí hodnotu jednoho metru, je takováto hodnota nahrazena pomlčkou. Funkce: vypocet_poledniku (R,m), vypocet_rovnobezek(R,m,zobrazeni) - vstupními hodnotami jsou R - poloměr Země, m - měřítko, zobrazení - druh zobrazení(pouze u výpočtu rovnoběžek). Výstupem jsou souřadnice poledníků a rovnoběžek pro vykreslení dané sítě.
   Na závěr program vypíše souřadnice poledníků a rovnoběžek. 
