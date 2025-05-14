# [-5;256]

# Vazifa 1: int, float, bool, str bilan ishlash

# 1)int, float, bool, str turlarini ishlatib, ularning qiymatlari o‘zgartirilganda yangi ob'ekt yaratishini ko‘rsating.
# butun = 4
# kasr = 4.4
# mantiqiy = True
# soz = "Jamshidbek"
# print(f"{id(butun)} {id(kasr)} {id(mantiqiy)} {id(soz)}")
# print(f"{id(butun)} {id(kasr)} {id(mantiqiy)} {id(soz)}")
# butun = 5
# kasr = 4.5
# mantiqiy = False
# soz = "Alimurod"
# print(f"{id(butun)} {id(kasr)} {id(mantiqiy)} {id(soz)}")

# 2) x = 7 bo‘lsa, x qiymatini o‘zgartiring va eski x ning manzilini va yangi x ning manzilini chiqarib ko‘rsating.
# x = 7
# print(id(x))
# x = 8
# print(id(x))

# Vazifa 2: `tuple`, `frozenset` bilan ishlash

# 1) `tuple` va `frozenset` ob'ektlarini o‘zgartirishga urining. Python nima deydi?
# a = (1,2)
# b = frozenset({1,2,4,5})
# print(a[1])
# a[1] = 3
# b.add(4)

# 2) Ularning immutability (o‘zgartirilmaslik) xususiyatlarini tekshiring.
# a = (1,2)
# b = frozenset({1,2,4,5})
# try:
#     a[1] = 3
# except:
#     print("a immutable")
# try:
#     b.add(4)
# except:
#     print("b immutable")

# Vazifa 3: `list`, `set`, `dict` bilan ishlash

# 1) `list`, `set`, va `dict` turlarining elementlarini o‘zgartiring (masalan, element qo‘shing yoki o‘chiring).
# a = [1,2,3]
# b = {1,2,3}
# c = {1:3,2:4,4:5}
# a.append(4)
# b.remove(1)
# c[1] = 5
# print(a,b,c)

# 2) Har bir operatsiya oldidan va keyin ob'ektning ID sini chiqarib ko‘rsating. Bu turlar mutable ekanligini ko‘rishingiz mumkin.
# a = [1,2,3]
# b = {1,2,3}
# c = {1:3,2:4,4:5}
# print(id(a),id(b),id(c))
# a.append(4)
# b.remove(1)
# c[1] = 5
# print(id(a),id(b),id(c))





