# raise IndexError('throw index error')
# raise ValueError('invalid value')

def colorSize(text, color):
    if type(text) is not str:
        raise TypeError('this type is not valid')
    else:
        print(f"printed  {text} in {color}")

colorSize(2,'red')