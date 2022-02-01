from random import *
import time

#########################################
aega = 3*60   # sekundid, võib olla väljendatud tehtena
kysimusi = 10 #ülesannete arv
#########################################

nimi = input("Kirjuta oma nimi õigesti ja vajuta enter ")


timeout_start = time.time() #programm läheb käima, siis käivitub taimer ka kohe

ok = 0 #mitu õigesti oli
i = 1 #see on tsüklimuutuja, ehk ülesande järjekorra number, mis while tsükli sees kasvab
while time.time() < timeout_start + aega and i <= kysimusi : #kuni aega on ja küsimused pole otsas
    
    esimene = randint(1, 10) #esimene juhuslik tehte liige
    teine = randint(1, 10) #teine juhuslik tehte liige
    tehe = randint(0,1) #mis tehe tuleb
    if tehe == 0: #läheb korrutamisega
        try:
            vastus = int(input(f"{i}.   {esimene} ⋅ {teine} = "))
            if(vastus == esimene * teine):
                ok = ok + 1
                print('Hästi!') #mida õige vastuse korral näidata
            else:
                print(':(') #mida vale vastuse korral näidata
        except ValueError:
            print("Jätsid vastuse vahele")
            
    elif tehe == 1: #läheb jagamisega
        try:
            jagatav = esimene * teine
            vastus = int(input(f"{i}.   {jagatav} : {teine} = "))
            if(vastus == jagatav / teine):
                ok = ok + 1
                print('Hästi!') #mida õige vastuse korral näidata
            else:
                print(':(') #mida vale vastuse korral näidata
        except ValueError:
            print("Jätsid vastuse vahele")
    i = i + 1
        
print(f"Õigeid vastuseid oli {ok}. Tubli!")

failinimi = nimi + "-" + str(ok) + ".txt"
f = open(failinimi, "w")  