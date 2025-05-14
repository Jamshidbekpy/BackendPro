# ## ⚡ CPU-bound mashqlar:

# # **1. Mashq (CPU-bound):**

# # 1 dan 10_000 gacha bo'lgan sonlar ichidan **armstrong sonlar** (sum of digits powered by the number of digits) ni topuvchi funksiya yoz.

# # > Maslahat:
# # > 
# # > 
# # > Armstrong son: 153 = 1³ + 5³ + 3³
# # > 

# # ---

# # **2. Mashq (CPU-bound):**

# # - 1 dan 100_000 gacha bo'lgan juft sonlar yig'indisini hisobla, ammo har bir sonni kvadratiga ko'paytirib yig'.

# # > Ya'ni, sum(x*x for x in range(1, 100001) if x % 2 == 0)
# # > 

# # ---

# # ## 🌐 I/O-bound mashqlar:

# # **3. Mashq (I/O-bound):**

# # - `https://jsonplaceholder.typicode.com/posts/1` va `posts/2`, `posts/3` sahifalariga **HTTP so‘rov** yuborib, har bir postning **title**'sini alohida chiqar.

# # > Maslahat:
# # > 
# # > 
# # > `requests` kutubxonasidan foydalan.
# # > 

# # ---

# # **4. Mashq (I/O-bound):**

# # - 10 ta `txt` fayl yarat. Har bir faylga 1000 ta "Salom dunyo" yoz.
    
# #     Fayllarni ketma-ket yozishga harakat qil.

# # 1.Armstrong sonlar:
# # 1 = 1^3
# # 153 = 1^3 + 5^3 + 3^3
# # 370 = 3^3 + 7^3 + 0^3
# # 371 = 3^3 + 7^3 + 1^3
# # 407 = 4^3 + 0^3 + 7^3

# def armstrongs(l,g):
#     list_armstrong = []
#     for number in range(l,g):
#         sum_digits = sum(int(digit)**3 for digit in str(number))
#         if number == sum_digits:
#             list_armstrong.append(number)
#     return list_armstrong

# print(armstrongs(1,10_000)) # [1, 153, 370, 371, 407]

# # 2. Yig'indisi 100_000 ga teng juft sonlar:

# print(sum(x*x for x in range(1, 100_001) if x % 2 == 0))

# # 3. JSONPlaceholder:

# import requests 
# for i in range(3):
#     url = f"https://jsonplaceholder.typicode.com/posts/{i+1}"
#     response  = requests.get(url)
#     print(response.json().get("title"))

# # 4. txt fayllar yaratish
# import os
# for i in range(10):
#     with open(f"file{i+1}.txt", "w") as file:
#         for _ in range(1000):
#             file.write("Salom dunyo\n")
#     os.remove(f"file{i+1}.txt")
    





# # Thread va GIL

# # 🧠 Mashq 1: Thread yaratish
# # 5 ta ip (thread) yarat va har biri ekranga Men ishga tushdim deb yozsin.

# # 🧠 Mashq 2: GIL ta’siri – hisoblash yuklamasi
# # 2 ta ip yarat. Har biri 1 dan 100_000_000 gacha bo‘lgan sonlarni qo‘shib chiqsin. Har bir ip oxirida Hisob tugadi deb yozsin. So‘ng yakuniy vaqtni o‘lchab ko‘r.

# # 🧠 Mashq 3: Thread bilan umumiy o‘zgaruvchi (race condition)
# # Global counter = 0. 10 ta ip counter += 1 ni 100_000 marta bajarsin. Oxirida counter qiymatini chop et.

# # 🧠 Mashq 4: Lock bilan xavfsiz ishlash
# # Yuqoridagi mashqni threading.Lock() bilan yoz. counter += 1 operatsiyasini lock bilan o‘rab xavfsiz qil.

# # 🧠 Mashq 5: time.sleep bilan I/O taqlid qilish
# # 5 ta ip yaratiladi. Har biri time.sleep(1) qiladi va Men tugadim deb yozadi. Threadlar parallel ishlayotganini kuzat.

# # 🧠 Mashq 6: Har bir threadga nom berish
# # 3 ta ip yarating, har biriga nom bering (Thread-A, Thread-B, Thread-C). Har biri o‘z nomini ekranga chiqarsin.

# # 🧠 Mashq 7: Thread.join() ishlatish
# # 3 ta ip 2 soniyadan uxlaydi (time.sleep(2)), lekin asosiy oqim join() bilan ularning tugashini kutadi. Tugaganda Barchasi tugadi deb yozadi.
    
# # 1)
# import threading   

# for _ in range(5):
#     t = threading.Thread(target=print, args=("Men ishga tushdim",))
#     t.start()
#     t.join()

# # 2)
# import threading
# import time

# def calc():
#     sum = 0
#     for i in range(1, 100_000_000):
#         sum += i
#     print("Hisob tugadi")

# # for _ in range(2):
# #     calc()
# start = time.time()

# threads = []

# for _ in range(2):
#     t = threading.Thread(target=calc)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print(f"Time: {time.time() - start}", threads)


# # 3)
# import threading

# counter = 0

# def increment():
#     global counter
#     for _ in range(100_000):
#         counter += 1

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=increment)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print(counter)

# # 4) 
# import threading

# counter = 0

# def increment(lock):
#     with lock:
#         global counter
#         for _ in range(100_000):
#             counter += 1

# threads = []

# for _ in range(10):
#     lock = threading.Lock()
#     t = threading.Thread(target=increment, args=(lock,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print(counter)

# # 5)

# import threading
# import time
# import requests

# def fetch_url(url):
#     print(f"Fatching url {url}")
#     response = requests.get(url)
#     print(f"Response status code: {response.status_code}")

# start = time.time() 
# threads = []

# for _ in range(5):
#     fetch_url("https://github.com")
#     # time.sleep(1)

# print(f"Time: {time.time() - start}")


# start = time.time()
# for _ in range(5):
#     url = "https://github.com"
#     t = threading.Thread(target=fetch_url, args=(url,))
#     t.start()
#     # time.sleep(1)
#     threads.append(t)

# for t in threads:
#     t.join()

# print(f"Time: {time.time() - start}")

# # 6)
# import threading

# def print_name(name):
#     print(name)

# threads = []

# thread1 = threading.Thread(target=print_name, args=("Thread-A",))
# thread2 = threading.Thread(target=print_name, args=("Thread-B",))
# thread3 = threading.Thread(target=print_name, args=("Thread-C",))

# thread1.start()
# thread2.start()
# thread3.start()

# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)


# for t in threads:
#     t.join()

# # 7)
# import threading
# import time

# def worker():
#     print(f"{threading.current_thread().name} started")
#     time.sleep(2)
#     print(f"{threading.current_thread().name} finished")

# threads = []
# for name in ["Thread-A", "Thread-B", "Thread-C"]:
#     t = threading.Thread(target=worker, name=name)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print("Barchasi tugadi ✅")






# ## 3) multiprocessing and CPU and I/O bound

# # ## 🧠 Amaliy Mashq

# # Quyidagi mashqlarni bajaring:

# # ### 🔧 CPU-bound mashq:

# # 1. Har bir process 1 dan 100 milliongacha bo‘lgan sonlar yig‘indisini hisoblasin.
# # 2. 4 ta alohida process yarating.

# # ### 🌐 I/O-bound mashq:

# # 1. 3 ta saytga `requests.get()` yuboring (`https://google.com`, `https://github.com`, `https://python.org`).
# # 2. Har biri alohida processda bo‘lsin.
# # 3. Har birining status code’sini chiqaring.

# # 1)
# import multiprocessing
# import time

# def calc():
#     sum = 0
#     for i in range(1, 100_000_000):
#         sum += i
#     print(sum)
 
# start = time.time()   
# # for _ in range(4):
# #     calc()

# if __name__ == "__main__":
#     processes = []
#     for _ in range(4):
#         p = multiprocessing.Process(target=calc)
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()
        
#     print(f"Time: {time.time() - start}")
    
# # print(f"Time: {time.time() - start}")
    
# # 2)
# import multiprocessing
# import requests

# def fetch_url(url):
#     print(f"Fatching url {url}")
#     response = requests.get(url)
#     print(f"Response status code: {response.status_code}")

# if __name__ == "__main__":
#     urls = ["https://google.com", "https://github.com", "https://python.org"]
#     processes = []

#     for url in urls:
#         p = multiprocessing.Process(target=fetch_url, args=(url,))
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()








# 4) shared_data in threading and multiprocessing | GIL
# shared memory in multiprocessing | Manager, Value
# race_condition

## 🧠 Amaliy mashqlar

### Mashq 1: Threading va race condition

# - 3 ta thread `counter += 1` qilishsin.
# - Lock bilan va locksiz variantlarini solishtiring.

# ### Mashq 2: Multiprocessing va Value

# - 4 ta process 0 dan 50_000 gacha bo‘lgan sonlarni jamlab, umumiy `Value`ga qo‘shib borishsin.

# ### Mashq 3: Manager orqali shared list

# - Har bir process `shared_list.append("done")` qilsin.
# - Oxirida listda nechta `"done"` bo‘lishini tekshiring.

# 1)
# import threading

# shared_data = {'counter': 0}

# def increment_counter(lock):
#     with lock:
#         for _ in range(10_000_000):
#             shared_data['counter'] += 1
#         print(shared_data)

# threads = []
# for _ in range(4):
#     lock = threading.Lock()
#     t = threading.Thread(target=increment_counter, args=(lock,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print(f"Counter's value equal to {shared_data['counter']}")

# 2)
# import multiprocessing
# shared_data = 0
# def calc(shared_data):
#     for i in range(50_000):
#         with shared_data.get_lock():  # Yagona kirishni ta'minlaydi
#             shared_data.value += i
#     # print(shared_data.value)
#
#
#
# if __name__ == '__main__':
#
#     processes = []
#     shared_data = multiprocessing.Value('i', 0)
#     for _ in range(4):
#         p = multiprocessing.Process(target=calc, args = (shared_data,))
#         p.start()
#         processes.append(p)
#
#     for p in processes:
#         p.join()
#
#     print(f"Natija:",shared_data.value)    # race_condition

# 3)