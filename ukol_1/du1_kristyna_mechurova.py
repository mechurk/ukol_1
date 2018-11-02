import math
"""program pro vypocet polohy jednotlivych poledniku a rovnobezek v danem zobrazeni"""


#osetreni polomeru
def zadani_osetreni_polomeru():
    while True:
        polomerstr = input("zadej R v km:")
        R = float(polomerstr)
        if R <0:
            print("chybne zadany R")
        elif R ==0:
            return 6371.11*10000
        else:
            return R*10000



#osetreni meritka
def zadani_osetreni_meritka():
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



#osetreni zadani pismene pro zobrazeni
def zadani_osetreni_pismeneproZobr():
    while True:
        zobrazeni = input("zadej pismeno A,B,M nebo L: ")
        if zobrazeni == "A" or zobrazeni == "B" or zobrazeni == "M" or zobrazeni == "L":
            return zobrazeni
        else:
            print("nespravne zadane pismeno")



#vypocet poledniku

def vypocet_poledniku (R,m):
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

R = zadani_osetreni_polomeru()
m=zadani_osetreni_meritka()
zobrazeni=zadani_osetreni_pismeneproZobr()
poledniky=vypocet_poledniku (R,m)
rovnobezky=vypocet_rovnobezek(R,m,zobrazeni)

#vypsani poledniku a rovnobezek
print ("Rovnobezky:",rovnobezky)
print ("Poledniky:",poledniky)

