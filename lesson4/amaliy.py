# Iterator
## 📝 **Mashqlar:**

### 1️⃣ `1` dan `n` gacha bo'lgan tub sonlarni chiqaradigan iterator yozing.

### 2️⃣ Berilgan `string`dagi faqat katta harflarni qaytaradigan iterator class yozing.

### 3️⃣ `Fibonacci` sonlarini beradigan iterator class yozing (faqat `n` ta qiymat qaytarsin).

# 1)

# class PrimeNumIterator:
#     def __init__(self, n):
#         self.num = 1
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     @staticmethod
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     def __next__(self):
#         while self.num < self.n:
#             number = self.num
#             self.num += 1
#             if self.is_prime(number):
#                 return number
#         raise StopIteration
#
#
#
#
# prime_iterator = PrimeNumIterator(100)
#
# for i in prime_iterator:
#     print(i)
# print(prime_iterator)
#
# # 2)
#
# class UpperLetter:
#     def __init__(self, s):
#         self.index = 0
#         self.s = s
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.s):
#             while self.s[self.index].isupper() == False:
#                 self.index += 1
#             letter = self.s[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
#
# upper_iterator = UpperLetter("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
#
# for i in upper_iterator:
#     print(i)
#
# # 3)
#
# class FibNums:
#     def __init__(self,n):
#         self.fib = 0
#         self.n = n
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#     @staticmethod
#     def is_fibonacci(n):
#         if n < 0:
#             return False
#
#         def is_perfect_square(x):
#             s = int(x ** 0.5)
#             return s * s == x
#
#         return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
#
#     def __next__(self):
#         if self.n > self.counter:
#             while self.is_fibonacci(self.fib) == False:
#                 self.fib += 1
#             self.fib += 1
#             self.counter += 1
#             return self.fib - 1
#         else:
#             raise StopIteration
#
#
# fib1 = FibNums(10)
# for i in fib1:
#     print(i)






# map(), filter(), zip(), iter() function
# ## 📝 **Mashqlar:**

# ### 1️⃣ `map()` yordamida berilgan sonlar ro'yxatini 3 ga ko'paytiring.

# ### 2️⃣ `filter()` yordamida matndagi faqat raqamlarni ajrating: `["a", "1", "b", "3", "5", "x"]`

# ### 3️⃣ Ikkita ro‘yxatni `zip()` bilan birlashtiring va `(ism, yosh)` ko‘rinishida chop eting.

# ### 4️⃣ `iter()` yordamida ro'yxat elementlarini `next()` bilan birma-bir chiqaradigan kod yozing.

# # 1)

# a = [1,2,3,4,5]
# b = map(lambda x:x*3,a)
# for i in b:
#     print(i)
    
# # 2)

# c = ["a", "1", "b", "3", "5", "x"]
# d = filter(lambda x:x.isdigit(),c)
# for i in d:
#     print(i)

# # 3)

# e = ["ism", "yosh"]
# f = ["ali", "20"]
# g = zip(e,f)
# for i in g:
#     print(i)

# # 4)

# h = [1,2,3,4,5,6,7,8]
# i = iter(h)
# for _ in range(len(h)):
#     print(i.__next__())




# # Generator
# ## 📝 **Mashqlar:**

# ### 1️⃣ `n` gacha bo‘lgan juft sonlarni beradigan generator yozing.

# ### 2️⃣ Matndagi faqat unli harflarni `yield` qiluvchi generator yozing.

# ### 3️⃣ `n` ta tub sonni ketma-ket beruvchi generator funksiyasini yozing.

# # 1)

# def generator(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
# a = 100
# for i in generator(a):
#     print(i)

# # 2)
# def vowel(text):
#     for letter in text:
#         if letter in "aeiouAEIOU":
#             yield letter
# vow = set([])
# for i in vowel("Mening ismim Jamshidbek"):
#     print(i)
#     vow.add(i)
# print(vow)

# # 3)
# def prime_generator(n):
#     num = 2
#     while n > 0:
#         if num > 1:
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     break
#             else:
#                 yield num
#                 n -= 1
#         num += 1
# for i in prime_generator(10):
#     print(i)
    




