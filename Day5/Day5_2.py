class Employee:
    def __init__(self, name, birthYear):
        self.__name = name
        self.__birthYear = birthYear
    def __str__(self):
        return self.__name + ':' + str(self.__birthYear)
    
    def getName(self):
        return self.__name

    def getBirtYear(self):
        return self.__birthYear

    def setName(self, name):
        self.__name = name

    def setBirtYear(self, birthYear):
        self.__birthYear = birthYear


em1 = Employee('Nam', 1990)
em2 = Employee('Viet', 1995)
em3 = Employee('Xuan', 1994)
em4 = Employee('Ha', 1996)
em5 = Employee('Thu', 1993)
em6 = Employee('Dong', 1998)

lst = [em1,em2,em3,em4,em5,em6]
lst.sort(key = lambda x: x.getName(), reverse = False)
for l in lst:
    print(l.__str__())