"""
@author: Ritalin
problem: Metin tabanlı interaktif oyun projesi
"""

import random

class Karakter:
    def __init__(self, isim, karakter_tipi, saglik, guc, savunma):
        self.isim = isim
        self.karakter_tipi = karakter_tipi
        self.saglik = saglik
        self.guc = guc
        self.savunma = savunma
    
    def durumu_goster(self):
        print(f"{self.isim} ({self.karakter_tipi}) \n💔 Sağlık: {self.saglik},\n🗡️ Güç: {self.guc}, \n🛡️ Savunma: {self.savunma}\n")
        
    def hasar_al(self, hasar):
        self.saglik = max(self.saglik - max(hasar - self.savunma, 0), 0)
        
    def saldir(self):
        return random.randint(self.guc - 5, self.guc + 5)
    
def basla():
    print("🌟 Kaybolan Krallık'a hoş geldiniz! 🌟\n")
        
    def karakter_secimi():
        karakterler = {
            "1": ('Savaşçı', 120, 20, 10),
            "2": ('Büyücü' , 80, 30, 5),
            "3": ('Okçu'   , 25, 150, 25)
        }
        return karakterler
        
    karakterler = karakter_secimi()
    
    secim = input("1. 🗡️ Savaşçı, 2. 🔮 Büyücü, 3. 🏹 Okçu (1-3): ")
    if secim in karakterler:
        isim = input("🌐 Karakterinizin ismi: ")
        tip, saglik, guc, savunma = karakterler[secim]
        global oyuncu
        oyuncu = Karakter(isim, tip, saglik, guc, savunma)
        kasaba()
    else:
        print("❗ Geçersiz seçim, tekrar deneyin.")
        basla() 

def kasaba():
    print("🏠 Kasabaya vardınız. Maceraya hazır mısınız?\n")
    if input("✈️ Başlamak için 'Evet' yazın: ").lower() == "evet":
        gorev_1()
    else:
        kasaba()

def gorev_1():
    print("🐾 Ormanda bir canavarla karşılaştınız!\n")
    canavar_saglik, canavar_guc = 50, 12
    
    while oyuncu.saglik > 0 and canavar_saglik > 0:
        print(f"👿 Canavarın sağlığı: {canavar_saglik}\n")
        secim = input("🔪 Saldırmak için 'S' yazın: ").lower()

        if secim == 's':
            hasar = oyuncu.saldir()
            canavar_saglik -= hasar
            print(f"🌟 {oyuncu.isim}, canavara {hasar} hasar verdi!\n")

        if canavar_saglik > 0:
            canavar_hasari = random.randint(canavar_guc - 3, canavar_guc + 3)
            oyuncu.hasar_al(canavar_hasari)
            print(f"💥 Canavar {oyuncu.isim}'e {canavar_hasari} hasar verdi!\n")

        oyuncu.durumu_goster()    

    if oyuncu.saglik > 0:
        print("🎉 Canavarı yendiniz! Bir sonraki göreve hazır olun.\n")
        gorev_2()
    else:
        print("❌ Kaybettiniz. Macera burada sona erdi.\n")

def gorev_2():
    print("🔍 Ormanda ilerlerken yerde gizemli bir nesne fark ettiniz.\n")
    secim = input("💎 Nesneyi almak için 'A', görmezden gelmek için 'G' yazın: ").lower()
    
    if secim == "a":
        print("🌊 Gizemli bir tılsım buldunuz! Sağlığınız biraz yenilendi.\n")
        oyuncu.saglik += 50
        oyuncu.durumu_goster() 

    elif secim == "g":
        print("🌿 Nesneyi görmezden geldiniz ve size sinirlenip kalbinize kılıç sapladı!\n")
        print("💀 ÖLDÜNÜZ!")

    else:
        print("❗ Lütfen doğru bir seçim yapınız!")
        gorev_2() 

basla()