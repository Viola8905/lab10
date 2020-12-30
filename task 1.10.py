import math




class Number:

    def __init__(self, number, number_lenth):
        '''Поля класу'''
        self.number = list(str(number))
        self.number_lenth = number_lenth

    '''Методи класу'''

    def task_1(self, number):
        # введення
        self.number = list(str(number))

    def print(self):
        print("число=", "".join(self.number))

    def amount(self, data):
        return self.number.count(str(data))

    def sum (self):
        return sum([int (x) for x in self.number])

    def compare (self,other):
        if self.number_lenth < other.number_lenth:
            print("довжина першого менша")
        elif self.number_lenth > other.number_lenth:
            print("довжина першого більша")
        else:
            print("рівні")
'''--------------------------------------------------------------------------------------------'''





number=int(input("give me a number"))
number_2=int(input("give me second number "))

a = Number(number,len(str(number)))
a.print()
print(f"К-ть входження цифри 3: {a.amount(3)}")
print(f"Сума: {a.sum()}")

b= Number(number_2,len(str(number_2)))
a.compare(b)
