class User:
    name = "sam"
    family = "Azizi"
    age = 40

    def showFullName(self):
        return self.name +" " +self.family

    def __init__(self,name,family) : # گرفتن مقدار در هنگام ساهت نمونه
        self.name = name
        self.family = family


sam = User("mohame","ahmadi")
print(sam.family)
print(sam.showFullName())