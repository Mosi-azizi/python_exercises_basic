try:
    file=open("test3.py","r")
    file_content =file.read()
    print(file_content)
    file.close()

except FileNotFoundError:
    print("File not found error")
except IOError:
    print("Error reading the file ")

