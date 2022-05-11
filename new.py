#Kopyslsms islemi
import re

import pyautogui

"""
pyautogui.keyDown("ctrl")
pyautogui.press("c")
pyautogui.keyUp("ctrl")

pyautogui.click()

pyautogui.keyDown("ctrl")
pyautogui.press("v")
pyautogui.keyUp("ctrl")


pyautogui.click()

pyautogui.keyDown("ctrl")
pyautogui.press("v")
pyautogui.keyUp("ctrl")


pyautogui.mouseDown(button="left")
pyautogui.moveRel(0,-200,duration=1)
pyautogui.mouseUp()


pyautogui.hotkey("ctrl","c")
pyautogui.click()
pyautogui.hotkey("ctrl","v")

pyautogui.mouseDown(button="left")
pyautogui.moveRel(0,-200,duration=1)
pyautogui.mouseUp()


pyautogui.hotkey("ctrl","c")
pyautogui.click()
pyautogui.hotkey("ctrl","v")


print("Kopyalama islemi basari ile tamamlandi")
"""

#Kullanici ile etkilesim

"""
uyari = pyautogui.alert(text="Bu bir deneme mesajidir ", title="Deneme baslik", button="Tamam")
print("Uyari")

uyari2 = pyautogui.confirm(text="Onayliyormusunuz?",title="Onaylama raporu",buttons=["Iptal","Tamam"])
    if(uyari2=="Tamam"):
        print("Onayladiniz")

    elif(uyari2=="Iptal"):
        print("Iptal etdiniz")

    else:
        print("Hic bir sey yapmadiniz")

#ISim( bilgisi
isim = pyautogui.prompt(text="Isminiz nedir",title="Isim bilgisi",default="")
print(isim)


#Sifre bilgisi
sifre = pyautogui.password(text="Sifrenizi giriniz:",title="Sifre bilgisi:",mask="*")
print(sifre)
"""

"""
#Metakarakterler
#Nokta karakteri
import re

metin = "Python ile hayat cok guzel. Mython ile her sey cok kolay"
bul = re.findall(".ython",metin)
print(bul)

#Yildiz karakteri     evvelde olan yazinin ne olub olmasi hec neyi deyisdirmez
metin = "E-posta adreslerimiz:  test@mail.com, test@gmail.com, test@ggggmail.com"
bul = re.findall("@g*mail",metin)
print(bul)


#Arti karakteri  ->  karakterin 1 veya daha artiq sayida olmasini sorguluyar
metin = "E-posta adreslerimiz:  test@mail.com, test@gmail.com, test@ggggmail.com"
bul = re.findall("g+mail",metin)
print(bul) 


#Soru isaret Karakteri  ->  Karakterin  veya en fazlakez olmasini sorgular.
metin = "E-posta adreslerimiz:  test@mail.com, test@gmail.com, test@ggggmail.com"
bul = re.findall("@g?mail",metin)
print(bul)

#Koseli parantezler
metin = "Hilal ve Bilal cok yakin arkadaslar. Celal ise onlari kiskaniyor"
bul=re.findall("[HBC][ie]lal",metin)
print(bul)


#Suslu parantezler
metin = "Ahmetin beraat haberini duyan camaat, icraata gecerek imamin da kiraati ile insaata basladilar."\
        "Artiq icraat zamani!"
bul = re.findall("[a-z]*a{2}t",metin)
print(bul)
"""