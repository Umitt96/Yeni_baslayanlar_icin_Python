"""
@author: Ritalin
problem: Haftanın 7 gününe özel bazı görevler atayıp bunları çağırabilmek
"""

import os

days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
file_name  = "haftalik.plan.txt"


def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as dosya:
            return eval(dosya.read())
    else:
        return {day: [] for day in days}
    
def save_tasks(plan):
    with open(file_name, "w", encoding="utf-8") as dosya:
        dosya.write(str(plan))
        
def add_task(plan):
    print("Hangi güne görev eklemek istersiniz?\n")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")
        
    try:
        choice = int(input("Gün numarası girin (1-7): ")) - 1
        if 0 <= choice < 7:
            task = input("Görev adı: ")
            plan[days[choice]].append(task)
            save_tasks(plan)
            print("✅ Görev eklendi!")
        else:
            print("🚫 Geçersiz gün!") 
    except ValueError:
        print("❗ Geçerli bir sayı giriniz")  
     
def list_the_tasks(plan):
    print("\n📅 Haftalık plan:")
    for day, tasks in plan.items():
        print(f"\n{day}:")
        
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f" {i}. {task}")
        else: 
            print(" (Burası bomboş!)")
            
def delete_task(plan):
    list_the_tasks(plan)
    day = input("Hangi günden görev silmek istersiniz?: ")
    if day in plan and plan[day]:
        try:
            num = int(input("Silmek istediğiniz görevin numarası: ")) - 1
            if 0 <= num < len(plan[day]):
                deleted = plan[day].pop(num)
                save_tasks(plan)
                print(f"❌ '{deleted}' görevi silindi!")
            else:
                print("🚫 Geçersiz görev numarası!")
        except ValueError:
            print("❗ Lütfen geçerli bir sayı girin!")
    else:
        print("🚫 Geçersiz gün veya o gün için görev yok!")

      
def menu():
    plan = load_tasks()
    while True:
        print("------ Haftalık Program ------")
        print("\n[1] Görevleri listele\n[2] Görev ekle\n[3] Görev silme\n[4] Programdan çıkış")
        
        choice = input("Seçiminiz: ")
        
        if choice == "1":
            list_the_tasks(plan)
        
        elif choice == "2":
            add_task(plan)
        
        elif choice == "3":
            delete_task(plan)
        
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim!")
            
menu()