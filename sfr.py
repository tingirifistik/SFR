from random import sample
from os import system
from time import sleep

alfabE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ozel_kar = ['`','~','!','@','#','$','%','^','&','*','_','-','+','=','{','[',']','}','}','|', ':',';','"','<',',','>','.','?','/',' ','\n',"(",")",r"'"]
sayi = ["0","1","2","3","4","5","6","7","8","9"]

def anahtar():
    input("".join(sample((alfabE), 52))+"\n")
    
def encode(text, fle):
    alfabe = list(alfabE)
    if fle == "fle":
        txt = ""
        r = text
        for i in r:
            if i in ozel_kar:
                txt += (i+"½")
            if i in sayi:
                sayi_degistir = int(i)+3
                txt += (str(sayi_degistir)+"ş"+"½")
            try:
                x = alfabe.index(i)
                txt += (str(x+1)+"½")
            except ValueError:
                pass
        return txt
    if text == "text":
        dosya = fle
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
        
def decode(text, fle):
    alfabe = list(alfabE)
    if fle == "fle":
        txt = ""
        r = text
        bol = r.split("½")
        for i in bol:
            if i in ozel_kar:
                txt += (i)
            if "ş" in i:
                sayi = i.split("ş")
                sayi_bol = sayi[0]
                sayi_degistir = int(sayi_bol)-3
                txt += (str(sayi_degistir))
            try:
                x = alfabe[int(i)-1]
                txt += (str(x))
            except ValueError:
                pass 
        return txt 
    if text == "text":
        dosya = fle
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

def anahtar_encode(anahtar, text , fle):
    alfabe = list(alfabE)
    if fle == "fle":
        txt = ""
        r = text
        for i in r:
            if i in anahtar:
                x = alfabe.index(i)
                liste = list(anahtar)
                txt += (liste[x]+"½")
            if i in ozel_kar:
                txt += (i+"½")
            if i in sayi:
                sayi_degistir = int(i)+3
                txt += (str(sayi_degistir)+"ş"+"½")
            if i not in anahtar:
                try:
                    x = alfabe.index(i)
                    txt += (str(x)+"½")
                except ValueError:
                    pass
        return txt
    if text == "text":
        dosya = fle
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
            
def anahtar_decode(anahtar, text , fle):
    alfabe = list(alfabE)
    if fle == "fle":
        txt = ""
        r = text
        bol = r.split("½")
        for i in bol:
            if i in anahtar:
                try:
                    liste = list(anahtar)
                    x = liste.index(i)
                    txt += (alfabe[x])
                except ValueError:
                    pass
            if i in ozel_kar:
                txt += (i)
            if "ş" in i:
                sayi = i.split("ş")
                sayi_bol = sayi[0]
                sayi_degistir = int(sayi_bol)-3
                txt += (str(sayi_degistir))
            if i not in anahtar:
                try:
                    x = alfabe[int(i)]
                    txt += (str(x))
                except ValueError:
                    pass 
        return txt 
    if text == "text":
        dosya = fle
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
    print(r"""
 ____  _____ ____  
/ ___||  ___|  _ \
\___ \| |_  | |_) |
 ___) |  _| |  _ <
|____/|_|   |_| \_\

1- Encrypt-Decrypt Text
2- Encrypt-Decrypt File
3- Create New Key
4- Exit""")
    try:
        menu1 = int(input("\n\nChoice: "))
    except ValueError:
        system("cls")
        print("Please enter integer, not string..")
        sleep(4)
        system("cls")
        continue
    if menu1 == 1:
        system("cls")
        print(r"""
 ____  _____ ____  
/ ___||  ___|  _ \
\___ \| |_  | |_) |
 ___) |  _| |  _ <
|____/|_|   |_| \_\
    
1- Encryption
2- Decryption 
3- Encryption with Key
4- Decryption with Key
5- Return to Main Menu""")
        try:
            menu2 = int(input("\n\nChoice: "))
        except ValueError:
            system("cls")
            print("Please enter integer, not string..")
            sleep(4)
            system("cls")
            continue
        if menu2 == 1:
            system("cls")
            text = input("Text: ")
            system("cls")
            input(encode(text, "fle")+"\n\n")
            system("cls")
        elif menu2 == 2:
            system("cls")
            text = input("Encrypted Text: ")
            system("cls")
            input(decode(text, "fle")+"\n\n")
            system("cls")
        elif menu2 == 3:
            system("cls")
            anahtar_al = input("Please enter key: ")
            system("cls")
            text = input("Text: ")
            system("cls")
            input(anahtar_encode(anahtar_al, text, "fle")+"\n\n")
            system("cls")
        elif menu2 == 4:
            system("cls")
            anahtar_al = input("Please enter key: ")
            system("cls")
            text = input("Encrypted Text: ")
            system("cls")
            input(anahtar_decode(anahtar_al, text, "fle")+"\n\n")
            system("cls")
        elif menu2 == 5:
            system("cls")
            continue
        else:
            system("cls")
            print("Please enter valid input...")
            sleep(3)
            system("cls")
    if menu1 == 2:
        system("cls")
        print(r"""
 ____  _____ ____  
/ ___||  ___|  _ \
\___ \| |_  | |_) |
 ___) |  _| |  _ <
|____/|_|   |_| \_\
    
1- Encryption
2- Decryption
3- Encryption with key
4- Decryption with key
5- Return to Main Menu""")
        try:
            menu3 = int(input("\n\nChoice: "))
        except ValueError:
            system("cls")
            print("Please enter integer, not string..")
            sleep(4)
            system("cls")
            continue
        if menu3 == 1:
            system("cls")
            path = input("Path: ")
            system("cls")
            encode("text", path)
        elif menu3 == 2:
            system("cls")
            path = input("Path: ")
            system("cls")
            decode("text", path)
        elif menu3 == 3:
            system("cls")
            anahtar_al = input("Please enter key: ")
            system("cls")
            path = input("Path: ")
            system("cls")
            anahtar_encode(anahtar_al, "text", path)
        elif menu3 == 4:
            system("cls")
            anahtar_al = input("Please enter key: ")
            system("cls")
            path = input("Path: ")
            system("cls")
            anahtar_decode(anahtar_al, "text", path)
        elif menu3 == 5:
            system("cls")
            continue
        else:
            system("cls")
            print("Please enter valid input...")
            sleep(3)
            system("cls")
    if menu1 == 3:
        system("cls")
        anahtar()
        system("cls")
    if menu1 == 4:
        break
