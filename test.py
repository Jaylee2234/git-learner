class FourCal:
    def __init__(self, first, second):
         self.first = first
         self.second = second  
    def setdata(self, first, second):
         self.first = first
         self.second = second
    def add(self):
         result = self.first + self.second
         return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.add())
print(a.second)

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


# a = MoreFourCal(4, 0)
# print(a.div())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

import this
print(this)

chars = '!@#$#%^%^&'
code_list1 = [ord(s) for s in chars if ord(s) >= 50]
print(code_list1)

comp_list = [x * 2 for x in range(10)]
print(comp_list)

num = [1, 2, 3, 4, 5, 6, 7]
str = ['A', 'B', 'C', 'D', 'E']
recap = [[n, s] for n in num for s in str]

print(recap)





dict_comp = {x:chr(65+x) for x in range(1, 11)}
print(dict_comp)

print(chr(65))

d = {}
d['a'] = 'alpha'
d['b'] = 'beta'
d['c'] = 'china'


print(d)

print(dir(d))

print(d.keys())








