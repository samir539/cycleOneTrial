import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import main
from tqdm import trange, tqdm
import sys
from strip import strip
from scipy.interpolate import interp2d
from scipy.misc import derivative
from scipy.interpolate import InterpolatedUnivariateSpline




def analysis(n_step, n_colony, n_bacteria, n_food,                                          
            x_low, x_high, y_low, y_high, radius,                                          
            eat_distance, k_die_0, k_duplicate, k_move, mu, std, born_radius,
            N_size, d_size, increment,
            relationship='Synergistic'):
    """

    """

    # Set the recrusion limit
    sys.setrecursionlimit(3000)

    # Give the coated and uncoated regions on the playground
    vertices_y = strip(N_size, d_size, y_high, increment)

    # Dataframe for T_1/2 storage
    col_N = np.asarray([[vertices_y[0][i][0]] for i in np.arange(len(vertices_y[0]))])
    col_d = np.asarray([[vertices_y[0][i][1]] for i in np.arange(len(vertices_y[0]))])
    col_d2 = np.asarray([[vertices_y[0][i][2]] for i in np.arange(len(vertices_y[0]))])
    info = np.hstack([col_N, col_d, col_d2, np.zeros(((N_size * d_size), 1))])
    half_life_df = pd.DataFrame(info, columns=['N', 'd', 'd2', 'Inner_step_T_1_2'])

    # One N, d and d2 combination for the simulation
    for strips in tqdm(range(4), desc='Strip', unit='strip'):   # strips: a list containing y coordinates of strip vertices

        # Simulation function
        step = main(n_step, n_colony, n_bacteria, n_food,                                          
                    x_low, x_high, y_low, y_high, radius,                                          
                    eat_distance, k_die_0, k_duplicate, k_move, mu, std, born_radius,
                    N_size, d_size, increment, vertices_y, strips,
                    relationship)

        # Add half life to the dataframe
        half_life_df.Inner_step_T_1_2[strips] = step

        # Generate figure
        # if step 

    

    return half_life_df




data = analysis(2, 2, 100, 2000,
                0, 10, 0, 10, 2, 
                1, 5, 5, 50, 0, 1, 0.001,
                10, 10, 0.1,
                'Competitive')

#interpolate data
x_given = np.array([475,376,338,433,444,435,364,454,479,434])
y_given = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
z_given = np.array([1,1,1,1,1,1,1,1,1,1])

z_i = np.linspace(0,10,10)
y_i = np.linspace(0,1,10)
function_linear =  interp2d( x_given, y_given, z_given, kind='linear')

print(data)
b = np.array([data.iloc[:,3]])
# print(data.iloc[:,3])
cr_pts = function_linear.roots()
cr_pts = np.append(cr_pts, (x_axis[0], x_axis[-1]))  # also check the endpoints of the interval
cr_vals = function_linear(cr_pts)
min_index = np.argmin(cr_vals)
max_index = np.argmax(cr_vals)
print("Maximum value {} at {}\nMinimum value {} at {}".format(cr_vals[max_index], cr_pts[max_index], cr_vals[min_index], cr_pts[min_index]))


if step%200 != 0:

    convexPlot()

    def stepReport():   
        for index in colonies_keys_1:
            hull[index] = ConvexHull(colonies[index].points)
            convex_hull_plot_2d(hull[index]).savefig('hull[step]')
            points_data_bacteria = colonies[index].points
            points_data.csv(#path)
            # points_data_food = colonies[index] food
            #element symbols









# data.to_csv(r'D:\Imperial College London\Year 2\201\Coding\bacteria\Data.csv', index=False)