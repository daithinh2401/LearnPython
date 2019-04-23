import os

# def dirs(path):
#     def mySort(path):
#         return os.path.getsize(path)
#     os.chdir(path)
#     files = os.listdir(path)
#     files = list(files)
#     files.sort(key = mySort, reverse = False)
#     for f in files:
#         print(f, os.path.getsize(path+"\\"+f))

# dirs("C:\\Users\\TTC\\Desktop\\Day5")

# "." is the current directory
# dirs(".")

# lst = [23,565,23,2,4,6,43]
# lst.sort(key = lambda x: x, reverse = True)
# print(lst)

# lst = ["Hello", "World", "goodbye", "ok"]
# lst.sort(key = lambda x: x.lower(), reverse = False)
# print(lst)

#list of tuple
lst = [(5,"A"),(4,"D"),(3,"E"),(2,"C"),(1,"B")]

print('Sort by KEY')
lst.sort(key = lambda x: x[0], reverse = False)
print(lst)
print('')
print('Sort by VALUE')
lst.sort(key = lambda x: x[1], reverse = False)
print(lst)