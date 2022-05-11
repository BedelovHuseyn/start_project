"""a = 3     #int
b = 3.14     #float
c = "Python"    #str
d = [1,2,3,4,5,"Python"]    #list
e = (1,2,3,4,5, "Python")    #tuple
f = {"Elma":3,"ARmut":4}    #dict
g = False     #bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print("{} + {} = {}".format(2,3,2+3))

print("31","01","2003",sep = "/")   #dogum tarihi yazma

#Matamatiksel operatorler

print(3 + 4)
print(10 - 3)
print(10 * 3)
print(10 / 4)
print(10 // 4)   #bolunenden alinan tam sayi
print(10 % 4)


a = "Metin"
print(a[len(a)-1])
print(a[0:4 ])


a = 3
b = 4
if a == 3 or b == 5:
    print("Harika")
else:
    print("Malesef")

if (not(3 == 4)):
    print("Evet")
    print("3, 4e beraber deyil, evvelinde not olduguna gore eks cavab qebul edilir")

a = 2
while a < 10:
    print("a: ", a)
    a += 2

i = 1
while (i < 1000):
    print("i:" , i)
    i *= 2

i = 0
while (i < 10):
    if i == 3 or i == 5:
        i += 1
        continue
    print("i:", i)
    i += 1


a = [1,2,3,4,5,6]
b = "Python"
for eleman in b:
    print(eleman)

a = ("araba")

a = a.replace("a","o")
print(a)
          """

liste = [1,2,3,4,5]
liste.append(0)
print(liste)

