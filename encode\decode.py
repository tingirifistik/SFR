from random import sample
from os import system
from time import sleep

def anahtar():
    while True:
        kontrol = True
        alfabe = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        a = sample(alfabe, 16)
        key = ''.join(a)
        for i in key.lower():
            if (key.lower()).count(i) > 1:
                kontrol = False
        if kontrol:
            print(key)
            input("\n")
            break
        else:
            pass

def encode():
    ozel_kar = ['`','~','!','@','#','$','%','^','&','*','_','-','+','=','{','[',']','}','}','|', ':',';','"','<',',','>','.','?','/',' ','\n',"(",")"]
    sayi = ["0","1","2","3","4","5","6","7","8","9"]
    alfabe = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dosya = input("File path: ")
    with open(dosya,"r", encoding="utf-8") as f:
        r = f.read()
    
    uzanti = dosya.split(".")
    with open(f"encoded-{uzanti[1]}.txt", "a", encoding="utf-8") as file:
        for i in r:
            if i in ozel_kar:
                file.write(i+"½")
            if i in sayi:
                sayi_degistir = int(i)+3
                file.write(str(sayi_degistir)+"ş"+"½")
            try:
                x = alfabe.index(i)
                file.write(str(x+1)+"½")
            except ValueError:
                pass
        
def decode():
    ozel_kar = ['`','~','!','@','#','$','%','^','&','*','_','-','+','=','{','[',']','}','}','|', ':',';','"','<',',','>','.','?','/',' ','\n',"(",")"]
    alfabe = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dosya = input("File path: ")
    with open(dosya,"r", encoding="utf-8") as f:
        r = f.read()
   
    a = ((dosya.split(".")[0]).split("-")[1])
    with open(f"decoded.{a}", "a", encoding="utf-8") as file:
        bol = r.split("½")
        for i in bol:
            if i in ozel_kar:
                file.write(i)
            if "ş" in i:
                sayi = i.split("ş")
                sayi_bol = sayi[0]
                sayi_degistir = int(sayi_bol)-3
                file.write(str(sayi_degistir))
            try:
                x = alfabe[int(i)-1]
                file.write(str(x))
            except ValueError:
                pass  

def anahtar_encode(anahtar):
    ozel_kar = ['`','~','!','@','#','$','%','^','&','*','_','-','+','=','{','[',']','}','}','|', ':',';','"','<',',','>','.','?','/',' ','\n',"(",")"]
    sayi = ["0","1","2","3","4","5","6","7","8","9"]
    alfabe = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dosya = input("File path: ")
    with open(dosya,"r", encoding="utf-8") as f:
        r = f.read()
    
    uzanti = dosya.split(".")
    with open(f"encoded-{uzanti[1]}.txt", "a+", encoding="utf-8") as file:
        for i in r:
            if i in anahtar:
                x = alfabe.index(i)
                liste = list(anahtar)
                file.write(liste[x]+"½")
            if i in ozel_kar:
                file.write(i+"½")
            if i in sayi:
                sayi_degistir = int(i)+3
                file.write(str(sayi_degistir)+"ş"+"½")
            if i not in anahtar:
                try:
                    x = alfabe.index(i)
                    file.write(str(x)+"½")
                except ValueError:
                    pass
            
def anahtar_decode(anahtar):
    ozel_kar = ['`','~','!','@','#','$','%','^','&','*','_','-','+','=','{','[',']','}','}','|', ':',';','"','<',',','>','.','?','/',' ','\n',"(",")"]
    sayi = ["0","1","2","3","4","5","6","7","8","9"]
    alfabe = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dosya = input("File path: ")
    with open(dosya,"r", encoding="utf-8") as f:
        r = f.read()
    
    a = ((dosya.split(".")[0]).split("-")[1])
    with open(f"decoded.{a}", "a+", encoding="utf-8") as file:
        bol = r.split("½")
        for i in bol:
            if i in anahtar:
                try:
                    liste = list(anahtar)
                    x = liste.index(i)
                    file.write(alfabe[x])
                except ValueError:
                    pass
            if i in ozel_kar:
                file.write(i)
            if "ş" in i:
                sayi = i.split("ş")
                sayi_bol = sayi[0]
                sayi_degistir = int(sayi_bol)-3
                file.write(str(sayi_degistir))
            if i not in anahtar:
                try:
                    x = alfabe[int(i)]
                    file.write(str(x))
                except ValueError:
                    pass  
  
             
while True:
    print("""1-Encode
2-Decode
3-Encode with key
4-Decode with key
5-Create key
6-Exit""")
    try:
        menu = int(input("\n\nChoice: "))
    except ValueError:
        system("cls")
        print("Please enter integer, not string..")
        sleep(4)
        system("cls")
    if menu == 1:
        system("cls")
        encode()
        system("cls")
    elif menu == 2:
        system("cls")
        decode()
        system("cls")
    elif menu == 3:
        system("cls")
        anahtar_al = input("Please enter key: ")
        system("cls")
        anahtar_encode(anahtar_al)
        system("cls")
    elif menu == 4:
        system("cls")
        anahtar_al = input("Please enter key: ")
        system("cls")
        anahtar_decode(anahtar_al)
        system("cls")
    elif menu == 5:
        system("cls")
        anahtar()
        system("cls")
    elif menu == 6:
        break
    else:
        system("cls")
        print("Please enter valid input...")
        sleep(3)
        system("cls")
