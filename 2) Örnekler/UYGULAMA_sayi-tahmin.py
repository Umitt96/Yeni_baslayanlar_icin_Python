"""
@author: Ritalin
problem: PC bir sayı oluşturacak ve kullanıcı da bunu bulmaya çalışacak
"""

import random

def guess_number_game():
    print("Sayı tahmin oyununa hoş geldiniz!")
    print("1 ve 100 arasında bir sayı tahmin ediniz;\n")
    
    right_number = random.randint(1,100)
    guess_count = 0
    
    while True:
        predict = int(input("Tahminini giriniz: "))
        guess_count += 1
        
        if predict < right_number:
            print("Tahmin düşük, daha yüksek bir sayı deneyiniz\n")
    
        elif predict > right_number:
            print("Tahmin yüksek, daha düşük bir sayı deneyiniz\n")
        else:
            print(f"Tebrikler! {guess_count}. tahminde doğru sayıyı (yani {right_number}) buldunuz!")
            break

guess_number_game()