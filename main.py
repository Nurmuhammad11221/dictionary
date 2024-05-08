# dictionary

# car = {"brand":"chervolet", "model": "Matiz", "color": "red"}
# print(car["brand"])
# print(car["color"])

# student = {"ism": "dohn doe", "yosh": 20, "t_yili": 2000}
# print(f"{student["ism"].title()},\
#  {student["t_yili"]}-yilda tugilgan, \
#  {student["yosh"]} yoshda")

# student['kurs'] = 4
# student["Fakutet"] = "IT"
# print(student["kurs "])


# otam = {'ismi':'John', 't_yil': 1954, 'shahri':'toshkent'}
# t_yil = otam['t_yil']
# shahar = otam['shahri']


# print(f"Mening otamnning ismi {otam['ismi'].title()}," \
#      f"{t_yil}-yilda, {shahar.title()} shahrida tuglgan   ")

# student_0 = {}

# student_0["ism"] = "humoyun qosimov"
# student_0["kurs"] = 3
# student_0["yosh"] = 20

# print(student_0)
# print(f"Talaba {student_0["ism"].title()}, {student_0["kurs"]}-kurs")

# student_0["kurs"] = 4
# print(f"Talaba {student_0["ism"].title()}, {student_0["kurs"]}-kurs")

# student_1 = {
#     "ismi":"humoyun",
#     "familya":"qosimov",
#     "kurs":"3",
#     "yosh": 20,
#     "fakultet":"IT"
# }

# print(student_1.itmes())

# for kalit, qiymat in student_1.itmes():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")

# telefonlar = {
#     "ali": "iphone",
#     "vali": "oppo",
#     "olim": "vivo",
# }

# for k, v in telefonlar.items():
#     print(f"{k.title()}ning telefoni {v}")


davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSH": "Washington D.C", 
    "Rossiya": "Moskva",
    "Tojikiston": "Dushanbe",
    "Qirg'iziston": "Bishkek",   
    "Qozog'iston": "Nursultan",
    "Malayziya": "Kuala-Lumpur",
    "Singapur": "Sungapur",
    "Italiya": "Rim"   
}
print("Dunyo davlatlari: ")

for davlat in sorted(davlatlar):
    print(davlat.upper())

print("Davlatlarning poytaxti: ")

for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())              