#
# class CustomIterator:
#     def __init__(self,data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
# for i in CustomIterator([1,2,3,4]):
#     print(i)
#
#
# a = [1,2,3,4,5]
# b = [6,7,8,9,0]
#
# list_map = map(lambda x:x**2,a)
# for i in list_map:
#     print(i)
#
# list_filter = filter(lambda x:x%2==0,b)
# for i in list_filter:
#     print(i)
#
# list_zip = zip(a,b)
# for i in list_zip:
#     print(i)
#
# list_iter = iter(b)
# print(list_iter)


# def custom_generator():
#     print(f"Generator1")
#     yield 1

#     print(f"Generator2")
#     yield 2

#     print(f"Generator3")
#     yield 3

# for value in custom_generator():
#     print(value)

# def decarator_example(func):
#     def wrapper(x,y):
#         print("before")
#         result = func(x,y)
#         print("after")
#         return result
#     return wrapper

# @decarator_example
# def example(x,y):
#     print("example")
#     return x+y

# print(example(1,2))

# class MyDecarator:
    
#     def great(self):
#         return "Salom"
#     def __call__(self, *args, **kwargs):
#         print(self.great())
#         return "Men"
 
# obj = MyDecarator()   
# # print(obj.great())
# print(obj())
# print(obj.__dict__)
        
