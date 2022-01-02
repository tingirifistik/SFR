import platform
from random import sample
from os import system
from time import sleep

os = platform.system()
if os == "Windows":
    clear = "cls"
else:
    clear = "clear"

alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sayi = ["0","1","2","3","4","5","6","7","8","9"]

def anahtar():
    input("".join(sample((alfabe), 52))+"\n")
    
def encode(text, fle):
    if fle == "fle":
        txt = ""
        for i in text:
            if i not in sayi and i not in alfabe:
                txt += i+"≡"
            if i in sayi:
                txt += str(int(i)+3)+"≬"+"≡"
            try:
                txt += str(alfabe.index(i)+1)+"≡"
            except ValueError:
                pass
        return txt
    
    if text == "text":
        with open(fle,"r", encoding="utf-8") as f:
            read = f.read()
        uzanti = fle.split(".")[1]
        with open(f"encoded-{uzanti}.txt", "a", encoding="utf-8") as file:
            for i in read:
                if i not in sayi and i not in alfabe:
                    file.write(i+"≡")
                if i in sayi:
                    file.write(str(int(i)+3)+"≬"+"≡")
                try:
                    file.write(str(alfabe.index(i)+1)+"≡")
                except ValueError:
                    pass
        

def decode(text, fle):
    if fle == "fle":
        txt = ""
        bol = text.split("≡")
        for i in bol:
            if "≬" in i:
                txt += str(int(i.split("≬")[0])-3)
            elif i not in sayi and i not in alfabe:
                try:
                    if int(i) < 10:
                        pass
                except ValueError:
                    txt += i
            try:
                txt += str(alfabe[int(i)-1])
            except ValueError:
                pass
        return txt 
    
    if text == "text":
        with open(fle,"r", encoding="utf-8") as f:
            r = f.read()
        uzanti = ((fle.split(".")[0]).split("-")[1])
        with open(f"decoded.{uzanti}", "a", encoding="utf-8") as file:
            bol = r.split("≡")
            for i in bol:
                if "≬" in i:
                    file.write(str(int(i.split("≬")[0])-3))
                elif i not in sayi and i not in alfabe:
                    try:
                        if int(i) < 10:
                            pass
                    except ValueError:
                        file.write(i)
                try:
                    file.write(str(alfabe[int(i)-1]))
                except ValueError:
                    pass  


def anahtar_encode(anahtar, text , fle):
    if fle == "fle":
        txt = ""
        for i in text:
            if i in anahtar:
                txt += list(anahtar)[alfabe.index(i)]+"≡"
            if i not in sayi and i not in alfabe:
                txt += i+"≡"
            if i in sayi:
                txt += str(int(i)+3)+"≬"+"≡"
            if i not in anahtar:
                try:
                    txt += (str(alfabe.index(i))+"≡")
                except ValueError:
                    pass
        return txt
    
    if text == "text":
        with open(fle,"r", encoding="utf-8") as f:
            r = f.read()
        uzanti = fle.split(".")[1]
        with open(f"encoded-{uzanti}.txt", "a+", encoding="utf-8") as file:
            for i in r:
                if i in anahtar:
                    file.write(list(anahtar)[alfabe.index(i)]+"≡")
                if i not in sayi and i not in alfabe:
                    file.write(i+"≡")
                if i in sayi:
                    file.write(str(int(i)+3)+"≬"+"≡")
                if i not in anahtar:
                    try:
                        file.write(str(alfabe.index(i))+"≡")
                    except ValueError:
                        pass
            

def anahtar_decode(anahtar, text , fle):
    if fle == "fle":
        txt = ""
        bol = text.split("≡")
        print(bol)
        for i in bol:
            if i in anahtar:
                try:
                    txt += alfabe[list(anahtar).index(i)]
                except ValueError:
                    pass
            if "≬" in i:
                txt += str(int(i.split("≬")[0])-3)
            elif i not in sayi and i not in alfabe:
                try:
                    if int(i) < 10:
                        pass
                except ValueError:
                    txt += i
            if i not in anahtar:
                try:
                    txt += str(alfabe[int(i)])
                except ValueError:
                    pass 
        return txt 
    
    if text == "text":
        with open(fle,"r", encoding="utf-8") as f:
            r = f.read()
        uzanti = ((fle.split(".")[0]).split("-")[1])
        with open(f"decoded.{uzanti}", "a+", encoding="utf-8") as file:
            bol = r.split("≡")
            for i in bol:
                if i in anahtar:
                    try:
                        file.write(alfabe[list(anahtar).index(i)])
                    except ValueError:
                        pass
                if "≬" in i:
                    file.write(str(int(i.split("≬")[0])-3))
                elif i not in sayi and i not in alfabe:
                    try:
                        if int(i) < 10:
                            pass
                    except ValueError:
                        file.write(i)
                if i not in anahtar:
                    try:
                        file.write(str(alfabe[int(i)]))
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
        system(clear)
        print("Please enter integer, not string..")
        sleep(3)
        system(clear)
        continue
    
    if menu1 == 1:
        system(clear)
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
            system(clear)
            print("Please enter integer, not string..")
            sleep(3)
            system(clear)
            continue
        if menu2 == 1:
            system(clear)
            text = input("Text: ")
            system(clear)
            input(encode(text, "fle")+"\n\n")
            system(clear)
        elif menu2 == 2:
            system(clear)
            text = input("Encrypted Text: ")
            system(clear)
            input(decode(text, "fle")+"\n\n")
            system(clear)
        elif menu2 == 3:
            system(clear)
            anahtar_al = input("Please enter key: ")
            system(clear)
            text = input("Text: ")
            system(clear)
            input(anahtar_encode(anahtar_al, text, "fle")+"\n\n")
            system(clear)
        elif menu2 == 4:
            system(clear)
            anahtar_al = input("Please enter key: ")
            system(clear)
            text = input("Encrypted Text: ")
            system(clear)
            input(anahtar_decode(anahtar_al, text, "fle")+"\n\n")
            system(clear)
        elif menu2 == 5:
            system(clear)
            continue
        else:
            system(clear)
            print("Please enter valid input...")
            sleep(3)
            system(clear)
    
    if menu1 == 2:
        system(clear)
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
            system(clear)
            print("Please enter integer, not string..")
            sleep(3)
            system(clear)
            continue
        if menu3 == 1:
            system(clear)
            path = input("Path: ")
            system(clear)
            encode("text", path)
        elif menu3 == 2:
            system(clear)
            path = input("Path: ")
            system(clear)
            decode("text", path)
        elif menu3 == 3:
            system(clear)
            anahtar_al = input("Please enter key: ")
            system(clear)
            path = input("Path: ")
            system(clear)
            anahtar_encode(anahtar_al, "text", path)
        elif menu3 == 4:
            system(clear)
            anahtar_al = input("Please enter key: ")
            system(clear)
            path = input("Path: ")
            system(clear)
            anahtar_decode(anahtar_al, "text", path)
        elif menu3 == 5:
            system(clear)
            continue
        else:
            system(clear)
            print("Please enter valid input...")
            sleep(3)
            system(clear)
    if menu1 == 3:
        system(clear)
        anahtar()
        system(clear)
    if menu1 == 4:
        break
