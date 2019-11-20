#imports
import numpy as np
import matplotlib.pyplot as plt
from RandomRadius import randomPositionInRadius 

coordinateList = []

for i in range(10):
    a = np.random.random()*10
    coordinateList.append(a)






class bacteria():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

for i in range(10):
    a = randomPositionInRadius(coordinateList[0], coordinateList[1])[0]
    b = randomPositionInRadius(coordinateList[0], coordinateList[1])[1]
    print(a,b)
