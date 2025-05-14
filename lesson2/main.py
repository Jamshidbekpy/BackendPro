# Jamshidbek
# Homework
# 1)
# inherit Circular list
class CircularList(list):
    def __getitem__(self, index):
        if index is None:
            raise ValueError("Index bo'sh bo'lishi mumkin emas")
        index = index % len(self)
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if index is None:
            raise ValueError("Index bo'sh bo'lishi mumkin emas")
        if value is None:
            raise ValueError("Qiymat bo'sh bo'lishi mumkin emas")
        else:
            index = index % len(self)
            return super().__setitem__(index,value)

list1 = CircularList([1,2,3])
print(list1[55])
list1[55]=23
print(list1)
list2 = CircularList()
print(list2)












