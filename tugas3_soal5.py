import math
   
def volume():
    global vol
    d = r ** 3/6
    vol = d * 22/7

r = float(input("Diameter : "))
volume()
print("Volume : ", vol)