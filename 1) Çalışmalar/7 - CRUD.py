"""
@author: Ritalin
problem: CRUD işlemleri
"""

data = []

#Create işlemi
def create(item):
    data.append(item)
    print(f"{item} ögesi eklendi!")
    
#Read işlemi
def read():
    print("Mevcut veri:\n")
    for i, item in enumerate(data,1):
        print(f"{i}. öge: {item}")
        
    
#Update işlemi
def update(index, new_item):
    index -= 1
    if 0 <= index < len(data):
        old_item = data[index]
        data[index] = new_item
        print(f"{old_item} ögesi güncellendi: {new_item}!")
    else:
        print("Bilinmeyen index")

#Delete işlemi
def delete(index):
    index -= 1
    if 0 <= index < len(data):
        removed_item = data.pop(index)
        print(f"{removed_item} ögesi silindi!")

    else:
        print("Bilinmeyen index")

create("merhaba")
create("selam")
create("ben")
create("Ümit")
print("---")

read()
update(4, "Ritalin")
read()
print("---")

delete(2)
read()
