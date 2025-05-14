# import threading
# import time
#
# shared_data = {'counter': 0}
#
# def increment_counter():
#     for _ in range(10_000_00):
#         val = shared_data['counter']
#         time.sleep(0)  # kontekst almashinish majburiy bo'ladi
#         shared_data['counter'] = val + 1
#     print(shared_data)
#
# threads = []
# for _ in range(4):
#     t = threading.Thread(target=increment_counter)
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()
#
# print(f"Counter's value: {shared_data['counter']}")


# import multiprocessing
# import time
#
# shared_data = {'counter': 0}
# def increment_counter():
#     for _ in range(1000_000):
#         shared_data['counter'] += 1
#     print(shared_data)
#
# start = time.time()
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