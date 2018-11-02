import math
"""program pro vypocet polohy jednotlivych poledniku a rovnobezek v danem zobrazeni"""


polomerstr=input("zadej polomer v km:")
polomer=float(polomerstr)

#osetreni polomeru
if polomer <=0:
    print("chybne zadany polomer")
else:
    meritkostr=input("zadej meritko:")
    meritko=float(meritkostr)

#osetreni meritka
    if meritko<=0:
        print ("chybne zadane meritko")
    else:
        m2=meritko/10
        m3= round(m2, 0)
        m=int(m3)
        #print(m)
        R=polomer*10000
        #vytvoreni listu stupnu polednikove a rovnikove site
        u = [i for i in range(-90,100,10)]
        v = [i for i in range(-180,190,10)]
        #vytvoreni prazdneho listu do ktereho se budou zapisovat vypocty
        poledniky=[]
        rovnobezky=[]

        #osetreni zadani pismene pro zobrazeni
        while 1==1:
            zobrazeni = input("zadej pismeno A,B,M nebo L:")
            if zobrazeni == "A":
                zobrazeni = "A"
                break
            if zobrazeni == "B":
                zobrazeni = "B"
                break
            if zobrazeni == "M":
                zobrazeni = "M"
                break
            if zobrazeni == "L":
                zobrazeni = "L"
                break
            print("nespravne zadane pismeno")

        #vypocet poledniku
        for i in v:
            x=(R*i*math.pi/180)/m
            xvystup=round(x,1)
            poledniky.append(xvystup)

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
            yvystup=round(y,1)
            if yvystup !=9999:
                if yvystup>=100:
                    yvystup="-"
            rovnobezky.append(yvystup)

        #vypsani poledniku a rovnobezek
        print ("Rovnobezky:",rovnobezky)
        print ("Poledniky:",poledniky)

