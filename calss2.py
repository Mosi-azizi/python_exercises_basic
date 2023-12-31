from importlib.util import set_loader


class CarInfo:

    def __init__(self,model,color) :
        self.model = model
        self.color = color
    
    def showFullModel(self):
        return f"{self.model}  {self.color}"

benz = CarInfo("benz","red")
print(benz.color)
bmw = CarInfo("bmw","black")
print(bmw.showFullModel())