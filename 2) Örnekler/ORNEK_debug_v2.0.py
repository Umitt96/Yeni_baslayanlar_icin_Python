"""
@author: Ritalin
problem: Örnek uygulama: Debug v2.0
"""

def analyze_error(error_type):
    errors = {
        "SyntaxError": "Kodun yazımında bir hata var. Parantez, tırnak işaretleri veya iki nokta gibi sözdizim hatalarını kontrol edin",
        "IndentationError": "Girintileme hatası var. Kod bloklarının aynı seviyede girintilendiğinden emin olunuz",
        "TypeError": "Yanlış türde bir veri kullandınız. Örneğin, bir sayı ile bir metni toplamak gibi.",
        "NameError": "Tanımlanmamış bir değişken kullanıyorsunuz. Değişkenin adını doğru yazdığınızdan emin olun veya yoksa oluşturun.",
        "IndexError": "Bir dizinin geçerli sınırları dışında bir elemana erişmeye çalıştınız.",
        "KeyError": "Sözlükte olmayan bir anahtara erişmeye çalıştınız.",
        "ValueError": "Veri türü doğru, ancak içeriği uygun değil. Örneğin, bir metni sayıya çevirmeye çalışmak.",
        "AttributeError": "Bir nesnenin olmayan bir özelliğini kullanmaya çalıştınız.",
        "ZeroDivisionError": "Bir sayıyı sıfıra bölemezsiniz, işlemlerinizi kontrol edin."
        }
    
    explanation = errors.get(error_type, "Bilinmeyen bir hata türü girdiniz, küçük büyük harflere dikkat ediniz!")
    return f"Hata türü: {error_type}\nAçıklaması: {explanation}"

user_code = input("Karşılaştığınız hata kodunu yazınız:\n")
result = analyze_error(user_code)
print(result)