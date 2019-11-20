import numpy as np 
import matplotlib.pyplot as plt  






# b = np.random.uniform(-2,2)

# rand_x_cord = b

# # 
# c = (np.cos(a))*b

 

# one = b + 5
# two = c + 5


def randomPositionInRadius(x_cord, y_cord):
    a = np.random.uniform(0, 6.28)                   #random angle
    b = np.random.uniform(-2,2)                      #random radius value
    c = (np.cos(a))*b
    x_cordinate = b + x_cord                         #coordinates of point
    y_cordinate = c + y_cord
    return [x_cordinate, y_cordinate]


# coordinates = randomPositionInRadius(5,5)
# print(coordinates[0])

# x = [5]
# y = [5]

# plt.scatter(x,y, marker='.')
# plt.scatter(coordinates[0], coordinates[1], marker='1')
# plt.show()


