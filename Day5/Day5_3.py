import os

# def giaiThua(n):
#     if n == 1:
#         return 1
#     else:
#         return n*giaiThua(n-1)

# print(giaiThua(5))

# def dirs(path):
#     files = os.listdir(path)
#     files = list(files)
#     for f in files:
#         print(f)

# dirs(".")

# def inDeQuy(path,n):
#     files = os.listdir(path)
#     if n < len(files):
#         if os.path.isdir(path + "\\" + files[n]):
#             newPath = path + "\\" + files[n]
#             inDeQuy(newPath, n+1)
#         else:
#             print(files[n])
#             inDeQuy(path, n+1)

def inDeQuy(path,n):
    files = os.listdir(path)
    if n < len(files):
        if os.path.isdir(path + "\\" + files[n]):
            print(path + "\\" + files[n])
            inDeQuy(path + "\\" + files[n], 0)
        else:
            print(path + "\\" + files[n])

        inDeQuy(path, n+1)

inDeQuy("C:\\Users\\TTC\\Desktop\\Day5", 0)