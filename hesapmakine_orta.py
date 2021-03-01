print("""

[1] Toplama islemi
[2] cikarma islemi
[3] Carpma islemi
[4] Bolme islemi
[5] ust alma islemi
[0] Cikis



""")
giris= input("Seciniz:")
if giris=="1":
    x=float(input("birinci sayi gir:"))
    y=float(input("ikinci sayi gir:"))
    print("islem sonucu:",x+y)
elif giris=="2":
    x=float(input("birinci sayi gir:"))
    y=float(input("ikinci sayi gir:"))
    if x>y:
        print("islem sonucu:",x-y)
    else:
        print("islem sonucu:",y-x)
elif giris=="3":
    x=float(input("birinci sayi gir:"))
    y=float(input("ikinci sayi gir:"))
    print("islem sonucu:",x*y)
elif giris=="4":
    x=float(input("birinci sayi gir:"))
    y=float(input("ikinci sayi gir:"))
    if y==0:
        print("bolum 0 olamaz!!!")
    print("islem sonucu:",x/y)
elif giris=="5":
    x=float(input("birinci sayi gir:"))
    y=float(input("ikinci sayi gir:"))
    print("islem sonucu:",x**y) 
elif giris=="0":
    exit(0)
else :
    print("yanlis girildi!!")
    quit()
    