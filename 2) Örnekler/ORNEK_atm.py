"""
@author: Ritalin
problem: Öğrendiklerinizi kullanarak bir ATM örneği yapınız
"""

def menu():
    print("\n--- ATM MENÜSÜ ---")
    print("[1] Bakiye sorgulama")
    print("[2] Para yatırma")
    print("[3] Para çekme")
    print("[4] Çıkış")
    print()
    
def bakiye_sorgu(bakiye):
    print(f"Mevcut bakiyeniz: {bakiye} TL")
    
def para_yatir(bakiye):
    miktar = float(input("Ne kadar para yatırmak istiyorsunuz?\n"))
    if miktar > 0:
        bakiye += miktar
        print(f"{miktar} TL hesabınıza yatırıldı")
    else:
        print("Geçersiz miktar girdiniz!")
    return bakiye

def para_cek(bakiye):
    miktar = float(input("Ne kadar para çekmek istiyorsunuz?\n"))
    if miktar > 0 and miktar <= bakiye:
        bakiye -= miktar
        print(f"{miktar} TL hesabınızdan çekildi")
        
    elif miktar > bakiye:
        print("Yetersiz bakiye")
        
    else:
        print("Geçersiz miktar girdiniz!")
    return bakiye

def main():
    bakiye = 1000
    while True:
        menu()
        secim = int(input("Bir işlem seçiniz: "))
        
        if secim == 1:
            bakiye_sorgu(bakiye)
        elif secim == 2:
            bakiye = para_yatir(bakiye)
        elif secim == 3:
            bakiye = para_cek(bakiye)
        elif secim == 4:
            print("Programdan çıkılıyor..")
            break
        else:
            print("Geçersiz seçenek!")
        
        
main()
        
        
        
        
        
        
        