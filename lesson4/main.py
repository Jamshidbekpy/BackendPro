# Maqsad: I/O va CPU-bound vazifalarini parallel ravishda bajarish uchun threading va multiprocessing yordamida ko'p vazifali tizimni amalga oshirish.
# Vazifaning tavsifi:
# Asosiy vazifa - threading va multiprocessing modullaridan foydalanib, I/O va CPU-bound vazifalarini parallel tarzda ishlashni ta'minlashdir. Bu tizimda har bir vazifa ikkita turga bo'linadi: I/O va CPU-bound. I/O vazifalari tizimga murojaat qilib, vaqtincha kutishni talab qiladi (masalan, tarmoq yoki fayl bilan ishlash), CPU-bound vazifalari esa matematik hisob-kitoblarni talab qiladi (masalan, faktorial hisoblash). Tizimda vazifalar Queue yordamida almashiniladi va sinxronizatsiya muammolari (data race) oldini olish uchun zarur choralar ko'riladi.

# 1. Asosiy oqim (Main Thread):
# Vazifalar ro'yxatini yaratish: Asosiy oqim bir nechta vazifalarni yaratadi va ularni ikkita turga (I/O va CPU-bound) ajratadi.

# Vazifalar qo'shish: Har bir vazifa asosiy navbatga (main queue) qo'shiladi.

# 2. Birinchi Oqim (Thread 1):
# Asosiy navbatdan vazifalarni oladi.

# Vazifalarni I/O va CPU bound vazifalariga ajratadi va mos ravishda alohida navbatlarga (I/O va CPU navbatlari) qo'yadi.

# 3. Ikkinchi Oqim (Thread 2) - I/O vazifalari bilan ishlash:
# I/O vazifalarini I/O navbatidan oladi va ularni bajaradi.

# I/O vazifalarini bajarish uchun time.sleep() yoki boshqa simulyatsiyalar ishlatiladi (masalan, fayl tizimi yoki tarmoq so'rovlarini emulyatsiya qilish).

# 4. Uchinchi Oqim (Thread 3) - CPU vazifalari bilan ishlash:
# CPU vazifalarini CPU navbatidan oladi va intensiv hisob-kitoblar, masalan, faktorial yoki katta sonlar bilan ishlaydi.

# 5. Multiprocessing yordamida ko'p vazifali ish (Multiprocessing Worker):
# Bir nechta jarayonlarni yaratish, ayniqsa CPU-bound vazifalarni ko'proq ishlash uchun.

# Multiprocessing yordamida CPU vazifalarini yanada tezroq bajarish.

# 6. Vazifalar o'rtasidagi ma'lumot almashinuvi:
# I/O va CPU vazifalarini ajratish uchun ikkita alohida navbatlar yaratiladi (I/O va CPU navbatlari).

# Queue moduli orqali vazifalar bir oqimdan boshqa oqimga va jarayonlarga uzatiladi.

# Manager va Value yordamida umumiy xotirani boshqarish.

# 7. Gonka ma'lumotlarini boshqarish (Race Conditions):
# Navbatlarda vazifalar almashinuvida sinxronizatsiya usullaridan foydalanish.

# Threading va Multiprocessing bilan ishlashda ma'lumotlarning to'g'ri uzatilishini ta'minlash.


# import queue
# import random
# import requests
# import threading
# import multiprocessing

# base_queue = queue.Queue()
# io_queue = queue.Queue()
# cpu_queue = queue.Queue()
 

# def cpu_task(x):
#     x = 0
#     for i in range(1000_000):
#         x += i
        
# def io_task(url):
#     response = requests.get(url)
    
# def create_task():
#     urls = [
#     "https://tuit.uz/",
#     "https://www.google.com/",
#     "https://www.example.com/",
#     "https://www.github.com/",
#     "https://www.python.org/"
#     ]
#     task_type = random.choice(("cpu","io"))
#     if task_type == "cpu":
#         base_queue.put(("cpu", random.randint(1000_000,10_000_000)))
#         print("Create task cpu.......")
#     else:
#         base_queue.put(("io", random.choice(urls)))
#         print(" Create task io....... ")

# for i in range(20):
#     create_task()
    
    
    
# thread = threading.Thread()
    
    
        
        
# threads = []
# for i in range(2):
#     thread = threading.Thread(target=io_task,args=(url,))
    
        
