import math
"""program pro vypocet polohy jednotlivych poledniku a rovnobezek v danem zobrazeni"""


def zadani_osetreni_polomeru():
    """Vyzada od uzivatele polomer a osetri pripadne chybne vstupy, pro hodnotu 0 je polomer definovany 6371.11km."""
    while True:
        polomerstr = input("zadej polomer v km:")
        R = float(polomerstr)
        if R <0:
            print("chybne zadany polomer - zadejte kladne cislo")
        elif R ==0:
            return 6371.11*10000
        else:
            return R*10000


def zadani_osetreni_meritka():
    """Vyzada od uzivatele meritka v pomeru 1:x(x=zadana hodnota meritka) a osetri pripadne chybne vstupy."""
    while True:
        meritkostr = input("zadej meritko:")
        try:
            m = int(meritkostr)
            if m <=0:
                print("chybne zadane meritko - zadejte kladne cislo")
            else:
                m = m / 10
                return m
        except:
            print("chybne zadane meritko - zadejte cele cislo")



def zadani_osetreni_pismeneproZobr():
    """Vyzada od uzivatele druh zobrazeni, osetri pripadne chybne vstupy."""
    while True:
        zobrazeni = input("zadej pismeno A,B,M nebo L: ")
        if zobrazeni == "A" or zobrazeni == "B" or zobrazeni == "M" or zobrazeni == "L":
            return zobrazeni
        else:
            print("nespravne zadane pismeno")


def vypocet_poledniku (R,m):
    """Vytvori list poledniku po deseti stupnich a prazdny list, do ktereho se budou zapisovat vypocty. Provede vypocet poledniku,
    pokud jsou hodnoty vyssi nez jeden metr vrati hodnotu: - ."""
    v = [i for i in range(-180, 190, 10)]
    poledniky = []
    for i in v:
        x=(R*i*math.pi/180)/m
        x=round(x,1)
        #osetreni pokud je hodnota vyssi nez jeden metr
        if -100 >= x or x >=100:
            x="-"
        poledniky.append(x)
    return poledniky


#vypocet rovnobezek
def vypocet_rovnobezek(R,m,zobrazeni):
    """Vytvori list rovnobezek po deseti stupnich a prazdny list, do ktereho se budou zapisovat vypocty. Provede vypocet rovnobezek,
    v zavislosti na definovanem zobrazeni, pokud jsou hodnoty vyssi nez jeden metr vrati hodnotu: - ."""
    u = [i for i in range(-90, 100, 10)]
    rovnobezky = []
    v = [i for i in range(-180,190,10)]
    for i in u:

        if zobrazeni=="L":
            y=(R*math.sin(i*math.pi/180))/m
        elif zobrazeni=="A":
            y=(R*i*math.pi/180)/m
        elif zobrazeni=="B":
            y=(2*R*math.tan(i/2*math.pi/180))/m
        elif zobrazeni=="M":
            if abs(i)==90:
                y='-' #pol se nezobrazuje
            else:
                y=(R*math.log(math.tan(((i/2)+45)* math.pi / 180)))/m


        #osetreni pokud je hodnota vetsi nez jeden metr
        y=round(y,1)
        if -100 >= y or y >=100:
            y="-"

        rovnobezky.append(y)
    return rovnobezky


#volani funkci
R = zadani_osetreni_polomeru()
m=zadani_osetreni_meritka()
zobrazeni=zadani_osetreni_pismeneproZobr()
poledniky=vypocet_poledniku (R,m)
rovnobezky=vypocet_rovnobezek(R,m,zobrazeni)


#vypsani poledniku a rovnobezek
print ("Rovnobezky:",rovnobezky)
print ("Poledniky:",poledniky)

