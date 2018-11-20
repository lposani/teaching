import numpy as np
import matplotlib.pyplot as plt


def gaussian_fitness(x, y, theta):
    sigma_x = 2.
    sigma_y = 1.
    a = np.cos(theta) ** 2 / (2 * sigma_x ** 2) + np.sin(-theta) ** 2 / (2 * sigma_y ** 2)
    b = - np.sin(2 * -theta) / (4 * sigma_x ** 2) + np.sin(-2 * theta) / (4 * sigma_y ** 2)
    c = np.sin(-theta) ** 2 / (2 * sigma_x ** 2) + np.cos(theta) ** 2 / (2 * sigma_y ** 2)
    M = [[a,b], [b,c]]
    return np.exp(-(a * x ** 2. + 2. * b * x * y + c * y ** 2.)) / (2 * np.pi * sigma_x * sigma_y)


xs = np.linspace(-5,5,100) # define the x values with xrange
ys = np.linspace(-5,5,100) # define the y values

x,y = np.meshgrid(xs, ys, indexing='ij')  # create a grid of values for x and y [check <meshgrid> documentation online!]


theta = np.pi/16.  # define the twisting angle

plt.contourf(x, y, gaussian_fitness(x,y,theta))  # plot with color code for z axis and level curves
# try also plt.contour()

plt.colorbar()  # color scale
plt.xlabel('x')
plt.ylabel('y')
plt.title('twisted Gaussian $\\theta=%.1f$ rad' % theta)
plt.show()