import numpy as np
import matplotlib.pyplot as plt
from RandomRadius import randomPositionInRadius 

# Random coordinates for location of colonies
coordinateList = []

for i in range(10):
    a = np.random.random()*10
    coordinateList.append(a)


#colony class

class colony():

    def __init__(self, x_loc, y_loc, colonyNumber, listOfBacteria = []):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colonyNumber = colonyNumber
        self.listOfBacteria = listOfBacteria
        
#bacteria class     
class bacteria():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos


bacteriaList1 = []

for i in range(100):
    bacteriaList1.append(bacteria((randomPositionInRadius(coordinateList[0], coordinateList[1])[0]), (randomPositionInRadius(coordinateList[0], coordinateList[1])[1])))

bacteriaList2 = []

for i in range(100):
    bacteriaList2.append(bacteria((randomPositionInRadius(coordinateList[2], coordinateList[3])[0]), (randomPositionInRadius(coordinateList[2], coordinateList[3])[1])))

bacteriaList3 = []

for i in range(100):
    bacteriaList3.append(bacteria((randomPositionInRadius(coordinateList[4], coordinateList[5])[0]), (randomPositionInRadius(coordinateList[4], coordinateList[5])[1])))

bacteriaList4 = []

for i in range(100):
    bacteriaList4.append(bacteria((randomPositionInRadius(coordinateList[6], coordinateList[7])[0]), (randomPositionInRadius(coordinateList[6], coordinateList[7])[1])))

bacteriaList5 = []

for i in range(100):
    bacteriaList5.append(bacteria((randomPositionInRadius(coordinateList[8], coordinateList[9])[0]), (randomPositionInRadius(coordinateList[8], coordinateList[9])[1])))
# print(bacteriaList[0].x_pos, bacteriaList[0].y_pos)
# for i in range(100):
#     print(bacteriaList[i].x_pos, bacteriaList[i].y_pos)
#     # print(len(bacteriaList))

colonyOne = colony(coordinateList[0], coordinateList[1], 1, bacteriaList1 )
colonyTwo = colony(coordinateList[2], coordinateList[3], 2, bacteriaList2)
colonyThree = colony(coordinateList[4], coordinateList[5], 3, bacteriaList3)
colonyFour = colony(coordinateList[6], coordinateList[7], 4, bacteriaList4)
colonyFive = colony(coordinateList[8], coordinateList[ 9], 5, bacteriaList5)


x = [colonyOne.x_loc, colonyTwo.x_loc, colonyThree.x_loc, colonyFour.x_loc, colonyFive.x_loc]
y = [colonyOne.y_loc, colonyTwo.y_loc, colonyThree.y_loc, colonyFour.y_loc, colonyFive.y_loc]


plt.scatter(a,b)
plt.show()
