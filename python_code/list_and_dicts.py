# Lista letrehozasa
list1 = ["03 tesla", "01 toyota", "02 nissan"]
# vagy igy (az elso a gyorsabb)
list1 = list("03 tesla", "01 toyota", "02 nissan")

# Lista ertek atadasa
list2 = list1.copy()
# vagy
list2 = list1[:]
# vagy igy
list2 = list(list1)

# lista elem hozzaadaasa
list1.append('04 bmw')
# lista elem eltavolitasa index szerint
pop_elem = list1.pop(0)
# else egyezo lista elem torlese ertek szerint (ha nincs ilyen, hibat general)
list1.remove('04 bmw')
# lista kiterjesztese listaval
list2 = ['05 audi', '06 citroen']
list1.extend(list2)
# vagy igy:
list1 = list1 + list2

# rendezzuk a listat
list1.sort()
# visszafele rendezes
list1.reverse()

# Pelda a tananyagbol
box = [20, 45, 30]

# dictionary (szotar) letrehozasa
box = {"height": 20, "width": 45, "length": 30, "other": {"color": "black"}}
# vagy (az elso a gyorsabb):
box = dict(height=20, width=45, length=30)

# ertek megadasa
box['material'] = 'iron'
box['height'] = 21
print(box['other']['color'])
# uj dict letrehozasa

box2 = dict(box)
# box.copy()

# Peldak ertekek eleresere
print(f"Height: {box['height']} cm")
height = box.get('height1', 'Nincs ilyen kulcs')
del box['other']
box.pop('other', None)
# Kulcsok / ertekek egy listaba:
print(box.keys())
print(box.values())

for key, value in box.items():  # [('kulcs', 'ertek'), ('kulcs', 'ertek'), ...]
    print(f'key: {key}, value: {value}')

# print(box.items())

