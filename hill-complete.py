# skills:   - define a function
#           - use numpy arrays to compute the function output for multiple inputs
#           - visualize the function with matplotlib
#           - analyze how the function output depends on a parameter
#########

import numpy as np  # module that provides array functions and many scientific tools
import matplotlib.pyplot as plt  # module for data visualization

# one possibility is to first set "global" parameters and then define a function of the concentration
h = 2.0
A0 = 10.0


def hill(A):  # define a function of a single variable, the concentration A
    theta = A**h / (A0**h + A**h)  # body of the function: define variables and perform computations
    return theta  # return the computed value


# let's see how the function looks with the given parameters
print "Hill function of concentration 1 = %.3f" % hill(1)  # write a string and paste a numeric value inside with '%'
print "Hill function of concentration 100 = ", hill(2)  # alteratively, print in sequence the string and the value

# [RUN HERE]

# fine, let's now compute this function for many points and visualize it

concentrations = np.linspace(0, 100, 1000)  # define an array of 1000 values equally spaced between 0 and 100
thetas = hill(concentrations)  # arrays support mathematical operations: I can use them as input for the function!
# thanks to numpy array we can avoid slow 'for' loops !

plt.figure()  # open a figure to visualize the results of the function
plt.plot(concentrations, thetas)  # plots x = concentrations, y = thetas
plt.xlabel('concentration A')
plt.ylabel('$\\theta$')  # ! LaTeX in python !
plt.axhline([0], color='black', linestyle='--')  # plot boundary lines
plt.axhline([1], color='black', linestyle='--')
plt.title('my first Hill function plot')
plt.show()  # show me the figure!

# [RUN HERE]

# at what concentration A_t does the Hill function reach \theta = 0.75 with these parameters?
best_index = np.argmin(np.abs(thetas - 0.75))  # find the index of the closest theta to 0.75 in the array
A_t = concentrations[best_index]  # and the corresponding concentration
print "with parameters A_t = %.1f, h = %.1f, theta reaches 0.75 for A = %.1f" % (A0, h, A_t)
# this is how to paste multiple values in a string

# [RUN HERE]

# [exercise] define a function that takes theta_0 as an input (here: 0.75) and
#            outputs the concentration A_t - call the function find_A_t(theta_0)
# ---- 5 minutes

# let's put this into a function, shall we?

def find_A_t(theta_0):
    concentrations = np.linspace(0, 100, 1000)  # copy-paste these lines
    thetas = hill(concentrations)
    best_index = np.argmin(np.abs(thetas - theta_0))
    A_t = concentrations[best_index]
    return A_t


print "with parameters A_0 = %.1f, h = %.1f, theta reaches 0.75 for A = %.1f" % (A0, h, find_A_t(0.75))

# [RUN HERE]

# exercise: extend the function hill and find_A_t to take A0 and h as inputs, and draw
#           a plot to show how the concentration A_t changes when the hill parameter is
#           changed in the range [1, 10] - A0 stays at the value 10.0


def hill_2(A, A0, h):  # it now takes the parameters A0, h as input
    theta = A ** h / (A0 ** h + A ** h)  # the rest is the same
    return theta


def find_A_t_2(theta_0, A0, h):  # now find_A_t has to take the parameters as well to pass them downstream
    concentrations = np.linspace(0, 100, 1000)
    thetas = hill_2(concentrations, A0, h)  # watch out! the new hill function, the rest can be copy-pasted
    best_index = np.argmin(np.abs(thetas - theta_0))
    A_t = concentrations[best_index]
    return A_t


hs = np.linspace(1, 10, 10)

# let's visualize how the function shape changes when the Hill coefficient is varied

concentrations = np.linspace(0, 100, 1000)  # the x values of the function, as above
plt.figure(figsize=(9,4))
ax1 = plt.subplot(121)  # we will put two plots in this figures
plt.axhline([0.75], color = 'k', linestyle='--')

for i in range(len(hs)):
    h = hs[i]
    plt.plot(concentrations, hill_2(concentrations, 10, h), label='h = %.1f' % h)  # labels to recognize the plots!

plt.xlabel('concentration A')
plt.ylabel('$\\theta$')
plt.legend()  # visualize the labels

# on a second plot we plot how A_t depends on the hill function

plt.subplot(122)

A_ts = [find_A_t_2(theta_0=0.75, A0=10.0, h=h) for h in hs]  # alteratively: A_ts = [] then for loop and A_ts.append()
plt.plot(hs, A_ts)
plt.xlabel('Hill coefficient h')
plt.ylabel('A_t ($\\theta_0 = 0.75$)')

plt.tight_layout()
plt.show()
