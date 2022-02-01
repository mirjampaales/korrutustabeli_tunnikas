from random import *
import time

#########################################
ulatus = 10 #mis arvuni võivad tegurid ulatuda (10, kui harjutad tervet korrutustabelit)
aega = 3*60   # sekundid, võib olla väljendatud tehtena
kysimusi = 10 #ülesannete arv
tagasiside_oige = 'Hästi!' #mida õige vastuse korral näidata
tagasiside_vale = ':(' #mida vale vastuse korral näidata
tagasiside_tyhi = 'Jätsid vastuse vahele.' #kui vajutab vastamata enter või sisestab mitte-numbri
#########################################

nimi = input("Kirjuta oma nimi õigesti ja vajuta enter ")


timeout_start = time.time() #programm läheb käima, siis käivitub taimer ka kohe

ok = 0 #mitu õigesti oli
i = 1 #see on tsüklimuutuja, ehk ülesande järjekorra number, mis while tsükli sees kasvab
while time.time() < timeout_start + aega and i <= kysimusi : #kuni aega on ja küsimused pole otsas
    
    esimene = randint(1, ulatus) #esimene juhuslik tehte liige
    teine = randint(1, ulatus) #teine juhuslik tehte liige
    tehe = randint(0,1) #mis tehe tuleb
    if tehe == 0: #läheb korrutamisega
        try:
            vastus = int(input(f"{i}.   {esimene} ⋅ {teine} = "))
            if(vastus == esimene * teine): #kui vastus on õige
                ok = ok + 1
                print(tagasiside_oige) 
            else:
                print(tagasiside_vale) 
        except ValueError:
            print(tagasiside_tyhi)
            
    elif tehe == 1: #läheb jagamisega
        try:
            jagatav = esimene * teine
            vastus = int(input(f"{i}.   {jagatav} : {teine} = "))
            if(vastus == jagatav / teine): #kui vastus on õige
                ok = ok + 1
                print(tagasiside_oige) 
            else:
                print(tagasiside_vale) 
        except ValueError:
            print(tagasiside_tyhi)
    i = i + 1
        
print(f"Õigeid vastuseid oli {ok}. Tubli!")

failinimi = nimi + "-" + str(ok) + ".txt"
f = open(failinimi, "w")  