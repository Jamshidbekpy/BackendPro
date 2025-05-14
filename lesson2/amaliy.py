
# 1)Strategy pattern and Dependency injection
## 🧪 AMALIY TOPSHIRIQ: **ATM DASTURI**

# Endi ikkala patternni bitta real loyiha — **ATM dasturi**da ishlatamiz. Bu qismni quyidagi tartibda beraman:

# 1. 🔧 Talablar (nima qilish kerak)
# 2. 🔗 Classlar tuzilishi
# 3. 🔎 Kod (Strategy + DI ishlatilgan)
# 4. 📌 Har bir qismni izohlayman
#
# ---
#
# ### 🔧 1. Talablar:
#
# ATM foydalanuvchiga:
#
# - Har xil **to‘lov usullari (strategy)** bilan pul yechish
# - Har bir operatsiyani **Logger** orqali yozib borish (dependency injection)
# - Harakatlar: `withdraw_money(amount)`, `set_strategy(strategy)`
#
# ---
#
# ### 🔗 2. Classlar:
#
# - `PaymentStrategy (ABC)` → `CardPayment`, `UzumPayPayment`
# - `Logger`
# - `ATM` (context)

# from abc import ABC, abstractmethod
# class PaymentStrategy:
#     @abstractmethod
#     def pay(self,amount,*args):
#         pass
#
#
# class PlasticCard(PaymentStrategy):
#     def pay(self, amount, card_number, parol):
#         print(f"{amount} so‘m plastik karta orqali to‘landi  (card: ****{str(card_number)[-4:]})")
#
#
# class Cash(PaymentStrategy):
#     def pay(self,amount):
#         print("Oddiy naqt to'landi")
#
# class Logger:
#     def log(self,msg):
#         print(msg)
#
# class ATM:
#     def __init__(self,strategy:PaymentStrategy,logger:Logger):
#         self.strategy = strategy
#         self.logger = logger
#
#     def set_strategy(self,strategy):
#         self.strategy = strategy
#         self.logger.log("PaymentStrategy O'zgardi")
#
#     def withdraw_money(self,amount,*args):
#         self.logger.log(f"Hisobdan pul yechamiz....")
#         self.strategy.pay(amount,*args)
#         self.logger.log("Hisobdan pul yechdik")
#
# card1 = PlasticCard()
# log = Logger()
#
# atm1 = ATM(card1,log)
# atm1.withdraw_money(200,232323,1212)



# 2) class | Inheritance
## 🛠️ Amaliy topshiriq: Mashinalar klassi

### 🎯 VAZIFA:

# - `Vehicle` nomli **asosiy (parent) klass** yarat.
# - Undan `Car` va `Bike` nomli **ikki farzand klass** meros olsin.
# - Har bir klassda umumiy va o‘ziga xos metodlar bo‘lsin.
# - Klasslardan obyektlar yaratib, metodlarini chaqir.

# class Vehicle:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def way(self,amount):
#         print(f"{amount} km yurgan")
#     def __str__(self):
#         return f"{self.name} and {self.color}"
#
#
# class Bike(Vehicle):
#     def __init__(self,name,color,company_name):
#         super().__init__(name,color)
#         self.company_name = company_name
#
#     def __str__(self):
#             return f"{self.name} and {self.color} bike"
# class Car(Vehicle):
#     def __init__(self, name, color, model):
#         super().__init__(name, color)
#         self.model = model
#     def __str__(self):
#         return f"{self.name} and {self.color} car"
#
#
# # Sinov
# bike = Bike("Mountain Bike", "Red", "Giant")
# car = Car("Tesla", "Black", "Model S")
#
# print(bike)  # Mountain Bike and Red bike - Giant
# print(car)   # Tesla and Black car - Model S
#
# bike.way(15)  # 15 km yurgan
# car.way(100)  # 100 km yurgan



# 3) Parent class atributes
## 🎯 Amaliy topshiriq (tayyor):

# > 🚀 Vehicle nomli ota klass yarat:
# >
# - `brand`, `year` atributlari bo‘lsin.
#
# > 🚗 Car nomli farzand klass yarat:
# >
# - `model` qo‘shimcha atributi bo‘lsin.
#
# > Obyekt yaratib, ham parent, ham child atributlarini chop et.

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#
# class Car(Vehicle):
#     def __init__(self, brand, year, model):
#         super().__init__(brand, year)
#         self.model = model
#
# vehicle = Vehicle("Chevrolet",2004)
# print(vehicle.brand,vehicle.year)
# car = Car("Daewoo",2005,"DAMAS")
# print(car.brand,car.year,car.model)




# 4) class copy() and deepcopy()
## 🎯 Amaliy topshiriq

# > Person klassida name va contacts (ro‘yhat) atributlari bo‘lsin.
# >
# -
#     1. Avval `copy.copy()` bilan nusxa oling, `contacts`ni o‘zgartiring va farqni ko‘ring.
# -
#     1. So‘ng `copy.deepcopy()` qilib, yangisiga alohida contact qo‘shing.

# import copy
# class Person:
#     def __init__(self, name, contacts):
#         self.name = name
#         self.contacts = contacts
# person1 = Person("Jamshidbek",["Alimurod", "Umidjon", "Bahrom","O'tkir"])
# person2 = copy.copy(person1)
# print(person1.contacts,person2.contacts)
# person2.contacts.append("Ulug'bek")
# print(person1.contacts,person2.contacts)
# person3 = Person("Jamshidbek",["Alimurod", "Umidjon", "Bahrom","O'tkir"])
# person4 = copy.deepcopy(person3)
# print(person3.contacts,person4.contacts)
# person4.contacts.append("Ulug'bek")
# print(person3.contacts,person4.contacts)




# 5)method | classmethod, staticmethod,property and others
# > BankAccount klassi yarat:
# >
# - `balance` atributi
# - `deposit()` va `withdraw()` metodlari
# - `@classmethod` bilan jami hisoblar soni
# - `@staticmethod` bilan karta raqami validatsiyasi
# - `@property` bilan `balance`ni o‘qish va o‘zgartirish

# class BankAccount:
#     __accounts_count = 0  # private class attribute
#
#     def __init__(self, card_number, balance=0):
#         if self.validate_card(card_number):
#             self.card_number = card_number
#         else:
#             raise ValueError("Noto'g'ri karta raqami!")
#         self.__balance = balance  # private instance attribute
#         BankAccount.__accounts_count += 1  # account sonini oshirish
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise ValueError("Balans manfiy bo'lishi mumkin emas!")
#         self.__balance = amount
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount}$ hisobga qo'shildi. Yangi balans: {self.__balance}$")
#         else:
#             print("Deposit miqdori musbat bo'lishi kerak!")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Pul yechish miqdori musbat bo'lishi kerak!")
#         elif amount > self.__balance:
#             print("Hisobda yetarli mablag' yo'q!")
#         else:
#             self.__balance -= amount
#             print(f"{amount}$ hisobdan yechildi. Yangi balans: {self.__balance}$")
#
#     @classmethod
#     def get_accounts_count(cls):
#         return cls.__accounts_count
#
#     @staticmethod
#     def validate_card(card_number):
#         return isinstance(card_number, str) and len(card_number) == 16 and card_number.isdigit()
#
# # --- TEST ---
#
# acc1 = BankAccount("1234567890123456", 100)
# acc2 = BankAccount("1111222233334444", 200)
#
# acc1.deposit(50)
# acc1.withdraw(120)
# acc2.withdraw(500)
#
# print(acc1.balance)  # 30
#
# print(BankAccount.get_accounts_count())  # 2





# 6) Encapsulation
### 🛠️ **Amaliy Topshiriq: Inkapsulatsiya**

# 🎯 **Vazifa:**
#
# 1. **Student** nomli asosiy (parent) klassini yarat. Ushbu klassda talabalar uchun umumiy ma'lumotlar bo'lsin: ism, yosh, va baho.
# 2. `age` va `grade` atributlarini **private** qilib belgilash. Faqat getter va setter metodlari orqali bu atributlarga kirish mumkin bo'lsin.
# 3. Talaba ismini o'zgartirish uchun **public** metod yaratilsin (boshqa atributlar faqat getter va setter metodlari orqali o'zgartirilishi kerak).
# 4. Shuningdek, **age** atributi faqat ijobiy qiymatlarni qabul qilishi kerak va **grade** atributi faqat 0 va 100 orasidagi qiymatlarni qabul qilishi kerak.
# 5. Talaba haqida ma'lumotlarni chiqaruvchi metodlar va bu metodlarni sinovdan o'tkazish uchun bir nechta obyektlar yaratilsin.


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.__age = age
#         self.__grade = grade
#     def get_age(self):
#         return self.__age
#     def set_age(self,new_age):
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             print("age atributi 0 dan katta qiymat qabul qiladi")
#
#     def get_grade(self):
#         return self.__grade
#
#     def set_grade(self, new_grade):
#         if new_grade >= 0 and new_grade <= 100:
#             self.__grade = new_grade
#         else:
#             print("grade atributi 0 va 100 oralig'ida qiymat qabul qiladi")
#
#     def set_name(self,new_name):
#         self.name = new_name
#
# # ======= TEST =========
# student1 = Student("Jamshidbek", 21, 95)
# # ======= Qo'shimcha ========
# # print(student1.__dict__)
# # print(student1._Student__grade)
# # ================================
# print(student1.get_age())
# student1.set_age(23)
# print(student1.get_age())
#
# print(student1.get_grade())
# student1.set_age(85)
# print(student1.get_grade())
#
# print(student1.name)
# student1.set_name("Ali")
# print(student1.name)





# 7) Property and Descriptor

### 🛠️ **Amaliy Topshiriq:**

# 🎯 **Vazifa:**
#
# 1. **Product** nomli klass yaratilsin. Klassda `name`, `price`, va `quantity` atributlari bo'lsin.
# 2. `price` va `quantity` atributlari uchun **property** va **descriptor** ishlatilgan getter va setter metodlarini yozilsin.
# 3. `price` faqat musbat son bo'lishi kerak va `quantity` faqat 0 yoki undan katta butun son bo'lishi kerak.
# 4. `Product` obyektlari yaratib, metodlar orqali qiymatlar o'zgartirilsin va chiqarilsin.

# class Descriptor:
#     def __init__(self, atribute ):
#         self.atribute = atribute
#     def __get__(self, instance, owner):
#         print(f"Get.....{instance.__dict__[self.atribute]}")
#         return instance.__dict__.get(self.atribute)
#     def __set__(self, instance, value):
#         print(f"Set...{instance.__dict__.get(self.atribute)}")
#         instance.__dict__[self.atribute] = value
#     def __delete__(self, instance):
#         print("Del...")
#         del instance.__dict__[self.atribute]
#
#
# class Product:
#     name = Descriptor("name")
#     price = Descriptor("price")
#     quantity = Descriptor("quantity")
#     def __init__(self, name, price, quantity):
#         self.name = name
#         if price > 0:
#             self.price = price
#         else:
#             self.price = 1
#         if quantity >= 0:
#             self.quantity = quantity
#         else:
#             self.quantity = 0
#
#     # @property
#     # def name(self):
#     #     return self.name
#     # @name.setter
#     # def name(self,new_name):
#     #     self.name = new_name
#     #
#     # @property
#     # def price(self):
#     #     return self.price
#     #
#     # @price.setter
#     # def price(self, new_price):
#     #     if new_price > 0:
#     #         self.price = new_price
#     #     else:
#     #         print("price atributi 0 dan katta qiymat qabul qiladi")
#     #
#     # @property
#     # def quantity(self):
#     #     return self.quantity
#     #
#     # @quantity.setter
#     # def quantity(self, new_quantity):
#     #     if new_quantity >= 0:
#     #         self.quantity = new_quantity
#     #     else:
#     #         print("price atributi 0 dan katta qiymat qabul qiladi")
#
# product1 = Product("Kiyim", 1200, 300)
# print(product1.name)
# product1.quantity = 1
# print(product1.quantity)


# Qo'shimcha
# type() bilan class yaratish
### Amaliy topshiriq:
#
# **Vazifa**: Quyidagi amallarni bajarish uchun `type()` yordamida klass yarating.
#
# 1. `Animal` nomli klass yarating, unda `speak` metodini yaratib, "Animal speaks" deb chiqarsin.
# 2. `Dog` nomli subclass yarating, bu klass `Animal` klassidan meros olsin va `speak` metodini o'zgartirib, "Woof! Woof!" deb chiqarsin.
# 3. `Cat` nomli subclass yarating, bu klass ham `Animal` klassidan meros olsin va `speak` metodini o'zgartirib, "Meow!" deb chiqarsin.
# 4. `Animal`, `Dog` va `Cat` klasslaridan obyektlar yarating va har birining `speak` metodini chaqiring.

# Animal = type("Animal",(),{
#     'speak':lambda self: "Animal speaks"
# })
# Dog = type("Dog",(Animal,),{
#     'speak':lambda self: "Woof! Woof!"
# })
# Cat = type("Cat",(Animal,),{
#     'speak':lambda self: "Meow!"
# })
# animal1 = Animal()
# dog1 = Dog()
# cat1 = Cat()
# print(animal1.speak())
# print(dog1.speak())
# print(cat1.speak())






# 8)__new, __init, singltone class
### 🛠️ **Amaliy Topshiriq**

# 🎯 **Vazifa:**
#
# 1. **DatabaseConnection** nomli klass yaratilsin. Bu klass bir nechta `DatabaseConnection` obyektlarini yaratishga imkon bermasligi kerak (Singleton pattern).
# 2. **`__new__`** va **`__init__` metodlaridan foydalaning. Agar obyekt bir marta yaratilgan bo'lsa, undan keyin boshqa obyekt yaratish imkoniyati bo'lmasin.
# 3. `DatabaseConnection` sinfi `host`, `user`, `password` kabi atributlar bilan boshlansin va foydalanuvchi faqat bitta obyektdan foydalansin.
# 4. Dasturda `DatabaseConnection` klassidan ikki marta obyekt yaratishga urinish qiling va natijani tekshirib ko'ring.

# def connection_new(cls,*args,**kwargs):
#     if not cls._instance:
#         print("Creating the Singleton instance")
#         cls._instance = object.__new__(cls)
#     return cls._instance
# def connection_init(self,host,user,password):
#     if not hasattr(self, 'initialized'):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.initialized = True
#
# DatabaseCon = type("DatabaseCon", (),{
#     '_instance':None,
#     '__new__':connection_new,
#     '__init__':connection_init
# })
#
# # ============================================
#
# class DatabaseCon:
#     _instance = None
#     def __new__(cls, *args):
#         if not cls._instance:
#             print("Creating object!")
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self, host, user, password):
#         if not hasattr(self, "initialized"):
#             self.host = host
#             self.user = user
#             self.password = password
#             self.initialized = True
# object1 = DatabaseCon(2121, "Jamshid", "6767ghgh")
# print(id(object1))
# print(object1.host, object1.user, object1.password)
# object2 = DatabaseCon(212, "Jamshi", "6767ghh")
# print(id(object2))
# print(object2.host, object2.user, object2.password)

# Qo'shimcha
## 🎯 Mashq 1:

# **Multiple Inheritance** (bir nechta ota classdan meros olish):
#
# > 3 ta class bo'lsin: Logger, Database, Application.

# > `Logger` da `log()` metodi bo‘lsin.
# >
# > `Database` da `connect()` metodi bo‘lsin.
# >
# > `Application` `Logger` va `Database`dan meros olsin va `run()` metodini yoz.
# >
#
# **Talablar:**
#
# - Har bir metod ichida `super()` dan foydalan!
# - `Application` klassida `super()` orqali ham `log()`, ham `connect()` chaqirilsin.
# - `Application` obyektini yaratib, `run()` metodini chaqirganda har bir bosqich to'g'ri ishlasin.

# class Logger:
#     def log(self):
#         print("log yozildi")
# class Database:
#     def connect(self):
#         print("connect yozildi")
# class Application(Logger,Database):
#     def run(self):
#         super().log()
#         super().connect()
#         print("Application run")
# app = Application()
# app.run()

## 🎯 Mashq 2:

# **Custom new va init bilan Singleton Pattern:**
#
# > Config degan klass yozing.
# >
# >
# > Faqat **bitta obyekt** yaratilishi kerak (singleton).
# >
# > `__new__` va `__init__` metodlarini to‘g‘ri ishlating.
# >
# > `super()` orqali obyektni yarating.
# >
#
# **Talablar:**
#
# - `__new__` da obyekt yaratish.
# - `__init__` da atributlar (masalan: `env`, `version`) belgilash.
# - `Config("prod", "1.0")` va `Config("dev", "2.0")` yaratsangiz, **faqat birinchi yaratilgan obyekt** ishlasin.

# def singltone_new(cls,*args,**kwargs):
#     if not cls._instance:
#         cls._instance = super(type(cls),cls).__new__(cls)
#     return cls._instance
# def singltone_init(self, env, version):
#     if not hasattr(self,"initialized"):
#         self.env = env
#         self.version = version
#         self.initialized = True
# Config = type("Config",(),{
#     '_instance':None,
#     '__new__':singltone_new,
#     '__init__':singltone_init
# })
#
# object1 = Config("prod","1.0")
# print(object1.env)
# object2 = Config("dev","2.0")
# print(object2.env)

## 🎯 Mashq 3:

# **Ota classdagi propertyni super() orqali chaqirish:**
#
# > Person klassi bo‘lsin va unda name propertysi (getter, setter, deleter) bilan ishlasin.
# >
# >
# > `Employee` klassi `Person`dan meros olsin va `name`ni boshqacharoq o'zgartirib bersin (masalan, har doim "Employee: {name}" ko‘rsinsin).
# >
#
# **Talablar:**
#
# - `Employee` klassida `name` property'sining `getter`, `setter` va `deleter` larini `super()` orqali chaqirib qayta yoz.
# - `super()`dan foydalanmasangiz xato deb hisoblayman.

# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
#     @name.deleter
#     def name(self):
#         del self._name
#
#
# class Employee(Person):
#
#     @property
#     def name(self):
#         return f"Employee: {super().name}"
#
#     @name.setter
#     def name(self,new_name):
#         super(Employee,self.__class__).name.__set__(self,new_name)
#     @name.deleter
#     def name(self):
#         super(Employee, self.__class__).name.__delete__(self)
#
# emp = Employee("John")
# print(emp.name)
# emp.name = "Mike"
# print(emp.name)
# del emp.name





# 9) mro(),super()
### **Amaliy topshiriq**:

# 🎯 **Vazifa**: Quyidagi amaliy topshiriqni bajarib, **MRO** va **`super()`** metodini o'rganing.
#
# 1. **Animal** nomli parent klass yarating va `speak()` metodini aniqlang.
# 2. **Dog** va **Cat** nomli ikki child klassni yaratib, `speak()` metodini **`super()`** yordamida chaqiring.
# 3. **HybridAnimal** klassini yarating va unda `speak()` metodini chaqirish orqali **MRO**ning qanday ishlashini ko'rsating.

# class Animal:
#     def speak(self):
#         print("Animal speak...")
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print(f"Animal speak...dog")
# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print(f"Animal speak...cat")
# class HybridAnimal(Dog,Cat):
#     def speak(self):
#         super().speak()
#         print("Hb")
#
# hb1 = HybridAnimal()
# hb1.speak()
# print(HybridAnimal.mro())





# 10)@dataclass and __slots__
### **Amaliy topshiriq**

# 🎯 **Vazifa**: **`@dataclass`** va **`__slots__`**ni qo'llash.
#
# 1. **Student** nomli **dataclass** yarating, unda quyidagi atributlar bo'lsin: `name`, `age`, `grade`.
# 2. `Student` klassiga **`__slots__`** yordamida faqat `name`, `age`, va `grade` atributlariga ruxsat berilsin.
# 3. Obyektlarni yaratib, ularni chop eting va yangi atribut qo'shishga harakat qiling.

# from dataclasses import dataclass
# @dataclass
# class Student:
#     __slots__ = ['name','age','grade']
#     name:str
#     age:int
#     grade:float
#
# obj1 = Student("Jamshidbek",21, 3.2)
# obj2 = Student("Jamshidbek", 21, 3.2)
# obj3 = Student("Jamshidbek", 22, 3.2)
# print(obj1.__repr__())
# print(obj1 == obj2)
# print(obj2 == obj3)
# obj1.city = "Toshkent"

# 11)Dunder methods
# 1. **CustomClass** nomli klass yaratib, uning ustiga yuqorida keltirilgan **dunder methods**ni qo'shing (masalan, **`__add__`, `__eq__`, `__str__`, `__getitem__`, va h.k.**).
# 2. Keyin bu klassni sinab ko'ring, obyektlar yaratib, ular bilan amaliyotlar bajaring.

# class CustomClass:
#     def __init__(self, data):
#         self.data = data
#
#     def __add__(self, other):
#         if isinstance(other, CustomClass):
#             return CustomClass(self.data + other.data)
#         return NotImplemented
#
#     def __eq__(self, other):
#         if isinstance(other, CustomClass):
#             return self.data == other.data
#         return False
#
#     def __str__(self):
#         return f"CustomClass({self.data})"
#
#     def __getitem__(self, index):
#         return self.data[index]
#
#     def __setitem__(self, index, value):
#         self.data[index] = value
#
#     def __delitem__(self, index):
#         del self.data[index]
#
#     def __contains__(self, item):
#         return item in self.data
#
# obj1 = CustomClass([1, 2, 3])
# obj2 = CustomClass([4, 5, 6])
#
# print(obj1)
#
# obj3 = obj1 + obj2
# print(obj3)
#
# print(obj1 == obj2)
# print(obj1 == CustomClass([1, 2, 3]))
#
# print(obj1[0])
#
# obj1[0] = 10
# print(obj1)
#
# del obj1[1]
# print(obj1)
#
# print(10 in obj1)
# print(5 in obj1)
#
#
















