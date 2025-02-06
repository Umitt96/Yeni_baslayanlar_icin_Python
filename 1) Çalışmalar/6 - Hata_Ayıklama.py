"""
@author: Ritalin
problem: hata ayıklama örnek uygulaması
"""

try:
    # Hata oluşturabilecek kod
    sayi = int(input("100'ü bölmek için bir sayı giriniz:\n"))
    sayi = 100/ sayi
    print(f"Sonuç: {sayi}")
    
    
# "bir" yazmak
except ValueError:
    print("Lütfen sadece sayı giriniz!")


# 0 yazmak
except ZeroDivisionError:
    print("Sıfıra bölme yapamazsınız!")
    
    
finally:
    print("İşlem tamamlandı")

# 1-99 arasında sayılar girmek