from ast import In
from asyncore import read
from tkinter import PIESLICE


person = {
    'name': 'mohammad',
    'family': 'ordookhani'
}

# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return "no key fourn"
#     except IndexError:
#         return "index error"

# print(get(person,"name"))
def get(d,key):
    try:
        return d[key]
    except KeyError:
        return "no key found"
    except IndexError:
        return "not found index"
    except TypeError as err:
        print(err)

print(get(person,"age"))


try:
    file=open("test2.py", "r")
    file_content = file.read()
except FileNotFoundError:
   print("sssssssssssssdd")
except IOError:
   print("ssssssssssss")
finally:
    file.close()