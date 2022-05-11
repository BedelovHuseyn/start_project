"""dosya = open("icerik.txt", "w", encoding="utf-8")
dosya.write("Python kullaniyorum")
dosya.write("Python eylenceli")

dosya.close()

dosya = open("icerik.txt","a", encoding="utf-8")
dosya.write("\nPython sevdim")

dosya.close()

dosya = open("icerik.txt","r", encoding="utf-8")
print("ilk bolum")
metin = dosya.read()
print(metin)

print("ikinci bolum")
metin2 = dosya.read()
print(metin2)



dosya.close()

dosya = open("icerik.txt","r", encoding="utf-8")
print(dosya.readline(),end="")
print(dosya.readline(),end="")
print(dosya.readline(),end="")
print(dosya.readline(),end="")

dosya.close()

with  open("icerik.txt","r", encoding="utf-8") as dosya:
    for i in dosya:
        print(i,end="")

with  open("icerik.txt","r", encoding="utf-8") as dosya:
    print(dosya.tell())
    dosya.seek(6)
    print(dosya.tell())
    print(dosya.read(10)) 

with  open("icerik.txt","r+", encoding="utf-8") as dosya:
    metin = "Huseyn Bedelov \n"+dosya.read()
    dosya.seek(0)
    dosya.write(metin)

with open("icerik.txt","r+", encoding="utf-8") as dosya:
    liste = dosya.readlines()
    print(liste)
    liste.insert(3, "Bu yeni metin  ")
    dosya.seek(0)
    dosya.writelines(liste)"""""

mahalle = ["Ahmet","Mehmet","Omer","Faruk"]

ziyaret = iter(mahalle)

print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))
print(next(ziyaret))









