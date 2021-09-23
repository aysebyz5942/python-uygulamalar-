def sagSlas(adet):
    for i in range(int(adet)):
        print("/",end="")

def solSlas(adet):
    for i in range(int(adet)):
        print("\\",end="") # burada sadece bir tane basar\ bundan.

def satirAtla(adet):
    for i in range(int(adet)):
        print()

def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")

def ustKisim(cap):
    baslangicBosluk=cap/2-1
    for i in range(int(cap/2)):
        bosluk(baslangicBosluk-i) #bosluk sayısını 1 eksiltiyoruz
        sagSlas(1)
        bosluk(i*2)
        solSlas(1)
        satirAtla(1)

def altKisim(cap):
    baslangicBosluk=cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solSlas(1)
        bosluk(baslangicBosluk-(i*2))
        sagSlas(1)
        satirAtla(1)

def paralelkenar(cap):
    ustKisim(cap)
    altKisim(cap)

#paralelkenar(21) #cift sayılar icin gecerlidir
paralelkenar(20)

