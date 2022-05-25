# a = float(input('Kvadrati hesablanacaq reqemi daxil edin: '))


# str soz dizisidir
# a = 7 --->int tam ededlerdir
# a = 13.7  ---> float kəsr ədədlərə deyilir
# b = 14.5  ----> double floatin basqa adı
# a = 'Gorushdukde ilk sozu "salam", oldu'
# (3<5)-->{True} boolen cavab olaraq True ve Folse deyerini dondurur
# a = ["str","int","input"] ---->array basqa adi ile liste
##   ###   ####

# diller = {"php":25,"Java":30,"SQL":15}   #------>dictionary
# diller["Python"] = 35   elave etmek ucun isdifade olunur
# diller.clear()  ----> butun dictionary(sozluk) silinir
# diller.pop("php") ---> secilen dili silir
# diller.popitem() ----> rastgele birini siler
# diller2 = diller.copy() ----> yeni sozluk yaradar ve isdediyin sozluyu kopyalayar
# key = 'SQL'
# print(diller[key])
# a = None

# print(type(a))

# a = 5
# while True:
#     a += 1
#     if (a % 2 == 0):
#         continue
#     print(a)
#
#     if a == 199:
#         break

# arr = ['huseyn', 'eldar', 'eli', 'veli', 'pirveli']
# for var in arr:
#     print(var)
# print(type(range(1, 200)))

# var = 'elektirkleshdirdiklerimizdensinizmi?'
# boyut = len(var)
# for nums in range(0, boyut):
#     print(var[nums])


#var = 'elektirkleshdirdiklerimizdensinizmi?'
#boyut = len(var)
#a = 0
#while a < boyut:
#    print(var[a])
#    a += 1

'''

def fakt(n):
    if n>=0:
        if (n==1 or n==0):
            return 1
        else:
            return n*fakt(n-1)
    else:
        return "menfi reqem daxil etmeyin"
a = int(input("Faktoriyal hesablamaq isdediyiniz sayini yazin; "))
print(fakt(a))
'''

'''
a = 25
print(float(a))


a = ['Eldar','Huseyn','Python']
del(a[2])
print(a)  '''

### Return --->    funksiyamizin vereceyi deyeri gore bilmek ucun
#import random
#a = random.random()   #----> 0- ile, 1 arasinda float dondurur
#print(a)
#
#b = random.uniform(1,50)     #   verilen araliqda float dondurur
#print(b)
#
#c = random.randint(1,50)      #      verilen araliqda int dondurur
#print(c)
#
#d = random.randrange(1,50)      #   int dondurur amma sonuncu reqemide daxil edir
#print(d)
#
#sayilar = range(0,50)      #   rastgele birini secir
#e = random.choice(sayilar)
#print("Sayilar" , e)
#
#f = random.sample(sayilar, 3)     #  verilen say qeder regem verir
#print(f)
#
'''
a = int(input("ededi daxil edin"))
b = int(input("quvveti daxil edin"))


def quvvet(say1,say2,a=0):
    b = 1
    while a < say2:
        b = b * say1
        a += 1
    return (b)
print(quvvet(a,b))

'''
# def say(say1):
#     print(say1)



say(3)
### While -donguler ard-arda yapilan islemlere deyilir.

### Fonkksiyonlar --->  daha sonra istifade etmek ucun isledilir, her fonktion oz adi var

### Return --->    funksiyamizin vereceyi deyeri gore bilmek ucun

### While -donguler ard-arda yapilan islemlere deyilir.

''' 
import random
a = random.random()   #----> 0- ile, 1 arasinda float dondurur
print(a)

b = random.uniform(1,50)     #   verilen araliqda float dondurur
print(b)

c = random.randint(1,50)      #      verilen araliqda int dondurur
print(c)

d = random.randrange(1,50)      #   int dondurur amma sonuncu reqemide daxil edir
print(d)

sayilar = range(0,50)      #   rastgele birini secir
e = random.choice(sayilar)
print("Sayilar" , e)




f = random.sample(sayilar, 3)     #  verilen say qeder regem verir
print(f)    '''

# Loop-lar ya bir elementi dondurur, ya da bir shert esasinda donur
# while loopu if kimi ishleyir ve daxiline yazilmish shertden True qayitdigi ana qeder donur
# Meselen
# a = 6
# print(a<10) bu kod True qaytarir
# while(a<10):
#     print(a)
#     a+=1
# Bu kod 10-e qeder 10 daxil olmamaq serti ile ekrana 6,7,8,9 ededlerini yazir ve kod sonlanir!
# print(a<10) bu kod loop bitdikde deyeri 10-a beraber oldugu ucun False qaytarir

### Fonkksiyonlar --->  daha sonra istifade etmek ucun isledilir, her fonktion oz adi var

# For - loopu arrayin icinde olan verileri tek tek oxuyur sonra yeni bir  deyisen icinde yazdirir

# Return fonksiyonu - funksiyadan qayidan cavabinin neticesi hansi simvol olmasini gosterir  -> fonksiyonun dondureceyi deyeridi

#Map - arrayda verilenleri funtionda calisdirir(birinci function, ikinci arrayin adi yazilir)


#modul --> Fonksiyon db. YAzilan fonksiyonu ozunde saxliyir. istisade elemek isdediyimiz yerde cagira bilirik(import *name*)

#import math
#a = math.factorial(5)
#print(a)

# Return fonksiyonu - funksiyadan qayidan cavabinin neticesi hansi simvol olmasini gosterir  -> fonksiyonun dondureceyi deyeridi

#Map - arrayda verilenleri funtionda calisdirir(birinci function, ikinci arrayin adi yazilir)


#modul --> Fonksiyon db. YAzilan fonksiyonu ozunde saxliyir. istisade elemek isdediyimiz yerde cagira bilirik(import *name*)

#import math
#a = math.factorial(5)
#print(a)



# while for arasindaki fark

# For döngüsü, programcının belirli sayıda kez yürütmesi gereken bir döngüyü verimli bir şekilde yazmasına olanak tanıyan
# bir tekrar kontrol yapısıdır.
# While döngüsü, verilen koşul doğru olduğu sürece hedef ifadeleri yürüten bir tekrar kontrol yapısıdır.
# Kullanım
# For döngüsü, yineleme sayısı bilindiğinde kullanılabilir.	While döngüsü, yineleme sayısı bilinmediğinde kullanılabilir.
# Başlatma
# Başlatma, döngüde bir kez gerçekleşir.	While döngüsünde, başlatma ifadesi döngünün içindeyse, döngü her yinelendiğinde başlatma yapılır.



###################
# Dosya islemleri
# "r" - Oxumaq standartdır, oxumaq üçün faylı açır. Fayl mövcud deyilsə, xəta atır.
# "a" - Əlavə məlumat daxil etmək üçün faylı açır, fayl yoxdursa yenisini yaradır.
# "w" - Write faylı yazmaq üçün açır, fayl yoxdursa yenisini yaradır.
# "x" - Əgər fayl artıq mövcuddursa, Build xəta verir.



# map, verilen bir fonksiyonu sıralı nesnenin her elemanına tek tek uygulayarak bir liste yaratır.
#
# filter fonksiyonu bir Boolean (“doğru” veya “yanlış” veren) fonksiyon ve bir sıralı nesne alır, fonksiyon sonucunda
# “doğru” sonuç çıkaran elemanları içeren bir lxiste verir.


# dosya islemleri
# W - yazma ucun isdifade olunur. eger txt file yoxdusa yaradir
# a - append yeni elave etmek rolunu oynuyur
# r - right oxumaq ucundur
# r++ -- .seek yazim isdediyimiz yere data elave ede bilerik