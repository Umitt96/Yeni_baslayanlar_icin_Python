"""
@author: Ritalin
problem: if else kullanarak Hesap makinesi uygulaması
"""

# kullanıcıdan iki sayı alma
num_1 = float(input("Birinci sayıyı giriniz;\n"))
num_2 = float(input("İkinci sayıyı giriniz;\n"))

# kullanıcıdan işlem isteme
print("İşlem seçiniz: + - * /")
operation = input()

# hesap makinesi işlevini yapma
if operation == "+":
    result = num_1 + num_2
    print(f"Sonuç: {result}")

elif operation == "-":
    result = num_1 - num_2
    print(f"Sonuç: {result}")

elif operation == "*":
    result = num_1 * num_2
    print(f"Sonuç: {result}")
    
elif operation == "/":
    if num_2 == 0:
        print("Sıfıra bölme yapamazsınız!")
    else:
        result = num_1 / num_2
        print(f"Sonuç: {result}")
        
else:
    print("Geçersiz işlem yaptınız!")
    