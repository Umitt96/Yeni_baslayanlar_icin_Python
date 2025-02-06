import os
import random
import time
import psutil

def greet_user():
    print("Merhaba! Benim adım RitAsistan, sana nasıl yardımıc olabilirim?")
    
def get_time():
    return time.strftime("%H:%M:%S", time.localtime())

def tell_joke():
    jokes = [
        "Neden bilgisayar soğuk? Çünkü pencereler açık!",
        "Afrika'daki eczaneler neden iş yapmaz? Çünkü aç karnına hap atamazsın :D",
        "Python neden üzgün? Çünkü Elif gelmemişti"
    ]
    print(f"\n{random.choice(jokes)}") 
    
def calculator():
    print("\n🧮 Bir hesaplama yapalım!")
    num1 = float(input("1️⃣ Birinci sayıyı girin: "))
    num2 = float(input("2️⃣ İkinci sayıyı girin: "))
    operation = input("Hangi işlemi yapmak istersiniz (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("⚠️ Sıfıra bölme hatası!")
            return
    else:
        print("❌ Geçersiz işlem!")
        return

    print(f"✅ Sonuç: {result}")  

def open_calculator():
    print("Hesap makinesi açılıyor...")
    os.system("calc")
    
def open_explorer():
    print("Dosya gezgini açılıyor...")
    os.system("explorer")
    
def check_system_status():
    print("Bilgisayarın durumu kontrol ediliyor...")
    memory = psutil.virtual_memory()
    
    print(f"\n🔋 Toplam Bellek: {memory.total / (1024 ** 3):.2f} GB")
    print(f"⚡ Kullanılabilir Bellek: {memory.available / (1024 ** 3):.2f} GB")
    print(f"📊 Bellek Kullanımı: {memory.percent}%")
    
def shutdown_pc():
    print("Bilgisayar 3 saniye sonra kapanacak!")
    os.system("shutdown /s /f /t 3")
    
def main():
    greet_user()
    
    while True:
        print("""
🔍 Yapmak istediğiniz işlemi seçin:
|1 Saat söyle     |2️ Şaka yap      |3️ Hesaplama yap
|4️ Hesap makinesi |5️ Dosya gezgini |6️ Sistem durumu
|7️ Sistemi kapat  |8️ Çıkış""")
        
        choice = int(input("\n👉 Seçiminizi yapın (1-8): "))
        
        if choice == 1:
            print(f"⏰ Şu anki saat: {get_time()}\n")
        elif choice == 2:
            tell_joke()
        elif choice == 3:
            calculator()
        elif choice == 4:
            open_calculator()
        elif choice == 5:
            open_explorer()
        elif choice == 6:
            check_system_status()
        elif choice == 7:
            shutdown_pc()
            break
        elif choice == 8:
            print("👋 Görüşmek üzere!")
            break
        else:
            print("🚫 Geçersiz seçim. Lütfen tekrar deneyin!")

main()