import fajlkezelés
import feladatok

'''lista=fajlkezelés.lista_letrehozasa()
print(lista)

sz:str=fajlkezelés.lista_letrehozasa(lista)
print(sz)
fajlkezelés.fajlba_mentes(sz)'''

lista=fajlkezelés.fajlba_olvas()
print(lista)

'''1.Hány negatív szám van a lístában?'''
db:int=feladatok.negativ_szam(lista)
print(f"Ennyi negatív szám van: {db}")

'''2.Melyik a legnagyobb szám?'''
legnagyobb:int=feladatok.legnagyobb_szam(lista)
print(f"Ez a legnagyobb szám: {legnagyobb}")


paros:int=feladatok.paros_szamok(lista)
print(f"Páros számok: {paros}")



'''
1.Hány negatív szám van a lístában?
2.Melyik a legnagyobb szám?
3.Készíts új listát paros_lista néven és legyenek benne a páros számok
4.Mennyi az öttel oszható számok összege?
5.Hányadik helyen áll a legkisebb szám?

'''

