# class Employee():
#     org_name = 'Capgemini Consulting Services'
#     def __init__(self, eno, name, address, salary):
#         self.__eno = eno # eno is Private member variable & you can able to access eno with in the class
#         self.name = name #Public member variable
#         self.address = address # Public member variable
#         self._salary = salary# Salary is Protected member variable & you can access Salary with in the class and from Child classes
#     def getEmpInfo(self):
#         print('Employee Number:', self.__eno)
#         print('Employee Name:', self.name)
#         print('Employee address:', self.address)
#         if (self.__eno == 1001):
#             print('Employee Salary:', self._salary)
#     def x(self):
#         self.__getEmpInfo()
#     @classmethod
#     def getOrgInfo(cls):
#         print('Organization Name::', cls.org_name)
#     @staticmethod
#     def calculateSal(x, y):
#         print(x+y)
# t = Employee(1002, 'Jagdeesh', 'BLR', 1000000)
# t.getEmpInfo()

'''
from copy import copy,deepcopy
list_1 = [1, 2, [3, 5], 4]
# shallow Copy
list_2 = copy(list_1)
list_2[3] = 10
list_2[2].append(6)
list_3 = deepcopy(list_1)
print(list_3)
print(list_2)
print(list_1)
'''

'''
class A:
    def __init__(self,name):
        self.name = name
class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
class C(B):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def c_finding(self):
        print('Hello My name is',self.name)
        print('Hello My age is',self.age)
        print('Hello My salary is',self.salary)
obj = C('vijay',25,55000)
obj.c_finding()
'''





