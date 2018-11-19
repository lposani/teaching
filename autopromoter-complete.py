# skills:   - define a function of a function
#           - numerical solution to find the roots of a function
#           - numerical integration of a differential equation
#           - scipy <fsolve> and <odeint> to perform these operations with scipy modules
#           - systematic analysis of the autopromoter system [cfr prof. Hakim's lecture]
##########


import numpy as np
import matplotlib.pyplot as plt


def euler_integrate(f, times, y0):  # f is the derivative function, times equally-spaced time bins, y0 initial conditions
    dt = times[1] - times[0]  # define the timebin
    sol = np.zeros(len(times))  # initialize the solution array
    sol[0] = y0  # initial conditions

    for t in range(1, len(times)):  # iteration
        sol[t] = sol[t-1] + dt * f(sol[t-1])

    return sol


# parameters of our problem
h = 4.0
delta_A = 1.0
A0 = 1.0
r0 = 0.3
r1 = 2


def dAdt(A):  # define the RHS of the ODE
    dadt = (r0 + r1 * (A/A0)**h) / (1 + (A/A0)**h) - delta_A * A
    return dadt

# let's try it for one specific initial condition
A0_1 = 0.7
A0_2 = 0.9
times = np.linspace(0,20,1000)  # time range of integration

sol1 = euler_integrate(dAdt, times, y0 = A0_1)  # solution for the first initial condition
sol2 = euler_integrate(dAdt, times, y0 = A0_2)  # solution for the second initial condition

plt.plot(times, sol1, label='A_0 = %.2f' % A0_1)
plt.plot(times, sol2, label='A_0 = %.2f' % A0_2)

plt.xlim([0, times[-1]])
plt.xlabel('time (t)')
plt.ylabel('A(t)')
plt.title('auto-promoter solved with Euler method, two initial conditions')
plt.legend()
plt.show()

### [RUN HERE]

# predict the boundaries of the basins of attraction for the solutions = roots of the derivative function

def find_root_in_interval(f, interval, niter = 10):  # bisection method
    for i in range(niter):
        midpoint = (interval[0] + interval[1]) / 2.0  # compute the midpoint between low and high values
        if f(interval[0]) * f(midpoint) > 0: # if they have the same sign, take the midpoint as low value
            interval[0] = midpoint
        else: # else the other condition is true, the high value has the same sign of the midpoint
            interval[1] = midpoint  # use the midpoint as the high value
        return midpoint

# we can use a method to identify the intervals

def find_sign_changes_intervals(f, xs):
    intervals = []  # empty list of found sign-change intervals

    for i in range(len(xs) -1):  # cycle on the input xs
        if f(xs[i]) * f(xs[i+1]) < 0: # there is a sign change between f(x_t) and f(x_t+1)
            intervals.append([xs[i], xs[i+1]])

    return intervals


# check intervals by hand by plotting the function
a0s = np.linspace(0,3, 1000)  # the range of initial conditions that we will analyze

intervals = find_sign_changes_intervals(dAdt, a0s)  # find the input intervals for the bisection methods

zeros = []
for interval in intervals:  # use the found intervals to retrieve an estimation of the fixed points
    zeros.append(find_root_in_interval(dAdt, interval))

plt.plot(a0s, dAdt(a0s))  # visualize the RHS of the differential equation

for z in zeros:  # and plot the zeros as black dots
    plt.plot([z],[0], linestyle='none', color='k', marker='o')

plt.xlabel('A')
plt.ylabel('$\\frac{dA}{dt}$')
plt.axhline([0], color='k', linestyle='--')
plt.title('finding the stable points of the dynamics')
plt.show()

### [RUN HERE]


### finally we can put all the efforts together in a single figure ###

plt.figure(figsize=(9,4))

plt.subplot(121)
plt.plot(a0s, dAdt(a0s))
for z in zeros:
    plt.plot([z],[0], 'ko')
plt.xlabel('A')
plt.ylabel('$\\frac{dA}{dt}$')
plt.axhline([0], color='k', linestyle='--')

cm = plt.get_cmap('jet')

plt.subplot(122)
for i, a0 in enumerate(a0s):
    sol = euler_integrate(dAdt, times, a0)
    plt.plot(times, sol, c=cm(i/float(len(a0s))))

for z in zeros:
    plt.axhline([z], color='k', linestyle='--')

plt.xlim([0, times[-1]])
plt.xlabel('time (t)')
plt.ylabel('A(t)')
plt.title('autopromoter: dependence on initial condition')

plt.tight_layout()

plt.show()

### [RUN HERE]

# exercise: now that you are familiar with these numerical methods, reproduce the
#           same analysis with the optimized scipy functions <fsolve> and <odeint>
#           then repeat the analysis for the regimes of ONE and ZERO stable points
##########
