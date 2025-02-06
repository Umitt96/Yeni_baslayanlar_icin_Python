"""
@author: Ritalin
problem: Döngüler (Loops)
"""

## FOR DÖNGÜSÜ
#%%

# 1'den 10'a kadar sayıları yazdır
for i in range(1,11):
    print(i)
    

# 2'den 50'ye kadar sayıları 2'şer 2'şer yazdır
for i in range(2,51,2):
    print(i)

# Liste elemanları kadar X. deneme başarısız yazdırsın
my_list = [1,4,68,9,27,84]

for oge in my_list:
    print(f"{oge}. Deneme başarısız")
    
    

## WHILE DÖNGÜSÜ
#%%

# Kullanıcıdan pozitif olana kadar bir değer iste
number = -1

while number < 0:
    number = int(input("Pozitif bir sayı giriniz: "))
    print("Hatalı sayı girdiniz! Tekrar deneyin...")
print(f"Girdiğiniz sayı >> {number}")



## DÖNGÜLERDE BREAK VE CONTINUE
#%%

#BREAK 
#10'a kadar sayıları yazdır, ama 6'ya gelince döngü dursun

for i in range(1, 11):
    if i > 6:
        break
    print(i)
    

#CONTINUE 
#100'e kadar sayıları yazdır, ama 3'e bölünen sayıları gösterme
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)


#100'e kadar sayıları yazdır, 10'ar 10'ar git
for i in range(1, 101):
    if i % 10 != 0:
        continue
    print(i)


## İÇ İÇE DÖNGÜLER
#%%

# 5 i ve j değerini iç içe döngü olarak yazdır
for i in range (1,6):
    for j in range (1,6):
        print(f"i ve j değeri: {i} : {j}")
    
# Çarpım tablosu yapımı
for i in range(1,11):
    for j in range(1,11):
        print(f"|{i} * {j} = {i*j} |")
    print("|-------------|")




















