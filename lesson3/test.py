# import threading
# import time
#
# def calc():
#     x = 0
#     for i in range(1000_000):
#         x+=i
#
# start_time = time.time()
# threads = []
# for _ in range(4):
#     t = threading.Thread(target=calc)
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()
#
# # for _ in range(4):
# #     calc()
#
# print(f'delta time:{time.time()-start_time}')

#
# import threading
# import requests
# import time

# def fetch_url(url):
#     print(f"Fatching url {url}")
#     response = requests.get(url)
#     print(f"Done fetching url..{response.status_code}")
#
# start_time = time.time()
# threads = []
# for _ in range(9):
#     url = 'https://github.com/'
#     t = threading.Thread(target=fetch_url(url))
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

# for _ in range(9):
#     url = 'https://github.com/'
#     fetch_url(url)

# print(f'delta time:{time.time()-start_time}')
#
# import requests
# import multiprocessing
# import time
#
# def calc():
#     x = 0
#     for i in range(1000_000):
#         x+=i
#
# def fetch_url(url):
#     print("Fatching url...")
#     requests.get(url)
#     print("Done task...")

# start_time = time.time()

# if __name__ == '__main__':
#
#     prosess = []
#     urls = ['https://example.com' for _ in range(8)]
#     for url in urls:
#         p = multiprocessing.Process(target=fetch_url, args=(url,))
#         p.start()
#         prosess.append(p)
#
#     for p in prosess:
#         p.join()

    # for _ in range(8):
    #     calc()
    # print(f"delta time:{time.time()-start_time}")

# import threading
# import time
#
# start = time.time()
#
# shared_data = {'counter': 0}
#
#
# def increment_counter():
#     for _ in range(1000_000_0):
#         shared_data['counter']+=1
#     print("shared data:", shared_data['counter'])

# for _ in range(4):
#     increment_counter()
#
# print(f"Counter's value equal to {shared_data['counter']}")


# threads = []
# for _ in range(4):
#     t = threading.Thread(target=increment_counter)
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()
#
# finish = time.time()
# print(finish-start)
# print(f"Counter's value equal to {shared_data['counter']}")


# import multiprocessing
# import time
#
#
# def increment_counter():
#     for _ in range(1000_000):
#         shared_data['counter'] += 1
#     print(shared_data)
#
# start = time.time()
# shared_data = {'counter': 0}
# if __name__ == '__main__':
#     prosesses = []
#     for _ in range(4):
#         m = multiprocessing.Process(target=increment_counter)
#         m.start()
#         prosesses.append(m)
#
#     for m in prosesses:
#         m.join()
#
#     print("shared data main:",shared_data['counter'])
# finish = time.time()
# print(finish-start)


# import multiprocessing

# def increment_counter(shared_data, lock):
#     for _ in range(1000):
#         with lock:
#             shared_data['counter'] += 1
#     print(shared_data)

# if __name__ == '__main__':
#     with multiprocessing.Manager() as manager:
#         shared_data = manager.dict({'counter': 0})
#         lock = multiprocessing.Lock()
#         processes = []

#         for _ in range(4):
#             p = multiprocessing.Process(target=increment_counter, args=(shared_data, lock))
#             p.start()
#             processes.append(p)

#         for p in processes:
#             p.join()

#         print("shared data main:", shared_data['counter'])

# import threading
# import queue

# task_queue = queue.Queue()

# for i in range(10):
#     task_queue.put(i)

# task_number = task_queue.qsize()

# for i in range(3):
#     task_queue.put(None)
    
# def process(task_queue):
#     while True:
#         item = task_queue.get()
#         if item is None:
#             break
#         print(f"processing task {item}")
#         task_queue.task_done()
        
# threads = []
# for _ in range(3):
#     t = threading.Thread(target=process, args=(task_queue,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# import aiohttp
# import asyncio

# urls = [
#     "https://httpbin.org/delay/1",
#     "https://httpbin.org/delay/2",
#     "https://httpbin.org/delay/3"
# ]

# async def fetch(session, url):
#     async with session.get(url) as response:
#         print(f"Fetched {url} with status {response.status}")
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session, url) for url in urls]
#         results = await asyncio.gather(*tasks)
#         print(results)  

# asyncio.run(main())



    

    
    

















