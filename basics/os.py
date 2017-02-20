import os

'''for item in os.listdir("."):
    if os.path.isfile(item):
        print("{} jest plikiem".format(item))
    else:
        print("{} nie jest plikiem".format(item))

os.mkdir("pliki")
os.rename("test.py", "foo.py")
os.rmdir("pliki")'''



path = "pliki/01/dane.txt"
print(path)
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.abspath(path))

os.makedirs(os.path.dirname(path))
open(path, "w").close()