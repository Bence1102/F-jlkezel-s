import random
def lista_letrehozasa():
    #generálj 100 véletlen egész számot [-50;150] között
    # a függvény térjen vissza a számokat tartalmazó listával
    lista=[]
    for i in range(0,100, 1):
        szamok:int=int(random.random()*(151+50)-50)
        lista.append(szamok)
    return lista




#Listában lévő számokat füzd össze stringgé, az elválasztó jel ; legyen 
# az utolsó után ne legyen ;

def szovegge_alakit(lista):
    szoveg:str=""
    for i in range(0, len(lista),1):
       if (i<len(lista)-1):
           szoveg+=f"{lista[i]};"
       else:
           szoveg+=f"{lista[i]}"
           
    return szoveg





def fajlba_mentes(szoveg):
    fajlom=open("adatok.txt","w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()




def fajlba_olvas():
    fajlom=open("adatok.txt","r", encoding='utf-8')
    szoveg_fajlbol:str=fajlom.read()
    szoveg_lista=szoveg_fajlbol.split(";")
    '''Végig nyomjuk a szöveglistán, és minden elemét számmá alakítom 
        és eltávolítom belőle a felesleges szóközöket'''
    lista=[]
    for i in range(0, len(szoveg_lista),1):
        szam:int=int(szoveg_lista[i].strip())
        lista.append(szam)
    '''print(szoveg_fajlbol)
    print(lista)'''
    fajlom.close()
    return lista


