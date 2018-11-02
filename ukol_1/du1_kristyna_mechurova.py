import math
"""program pro vypocet polohy jednotlivych poledniku a rovnobezek v danem zobrazeni"""


#osetreni polomeru
def zadani_osetreni_polomeru():
    while True:
        polomerstr = input("zadej polomer v km:")
        polomer = float(polomerstr)
        if polomer <0:
            print("chybne zadany polomer")
        elif polomer ==0:
            return 6371.11
        else:
            return polomer

polomer = zadani_osetreni_polomeru()

#osetreni meritka
while True:
    meritkostr = input("zadej meritko:")
    meritko = int(meritkostr)
    if meritko <=0:
        print("chybne zadane meritko")
    else:
        break


m=meritko/10
R=polomer*10000
#vytvoreni listu stupnu polednikove a rovnikove site
u = [i for i in range(-90,100,10)]
v = [i for i in range(-180,190,10)]
#vytvoreni prazdneho listu do ktereho se budou zapisovat vypocty
poledniky=[]
rovnobezky=[]

#osetreni zadani pismene pro zobrazeni
while True:
    zobrazeni = input("zadej pismeno A,B,M nebo L: ")
    if zobrazeni == "A" or zobrazeni == "B" or zobrazeni == "M" or zobrazeni == "L":
        break
    else:
        print("nespravne zadane pismeno")

#vypocet poledniku
for i in v:
    x=(R*i*math.pi/180)/m
    x=round(x,1)
    if -100 >= x or x >=100:
        x="-"
    poledniky.append(x)

#vypocet rovnobezek
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
    #else:
       # print ("Chybne zadane pismeno")
       # break


    #osetreni pokud je hodnota vetsi nez jeden metr
    y=round(y,1)
    if -100 >= y or y >=100:
        y="-"
    rovnobezky.append(y)

#vypsani poledniku a rovnobezek
print ("Rovnobezky:",rovnobezky)
print ("Poledniky:",poledniky)

