# Imports
from math import pi, sin, sinh, sqrt
import numpy as np
import matplotlib.pyplot as plt

# Transmission Functions

# Transmission Equation 1
def T1(energy: float, beta: float, v0: float, dV : float, v1: float, v2 : float):

    E = energy*v0

    k2d = beta * sqrt(E/v0)

    sin_term = np.sin(k2d)**2

    above = dV**2 * sin_term

    below = 4 * (energy - v1) * (energy - v2) # V2 = V0
    
    return 1 / (1 + (above / below))

# Transmission Equation 2
def T2(energy: float, beta: float, v0: float, dV : float, v1: float, v2 : float):

    E = energy*v0

    k2d = beta * sqrt(E/v0)

    sin_term = np.sinh(k2d)**2

    above = dV**2 * sin_term

    below = 4 * (energy - v1) * (v2 - energy) # V2 = V0

    return 1 / (1 + (above / below))

def PlotFunction (v0: float):
     
    # Betas
    Beta1 = 4
    Beta2 = 10

    # Potentials
    v1 = 0
    v2 = v0
    v3 = 0
    dV = v2 - v1

    # Error Value
    delta = 10e-10

    Energy_v0 = np.linspace(0.01, 10, 1000000)

    y1 = []
    y2 = []

    # Populate the y Values
    for i in Energy_v0:

        if i > v0:
            y1.append(T1(i, Beta1, v0, dV, v1, v2))
            y2.append(T1(i, Beta2, v0, dV, v1, v2))
        else:
            y1.append(T2(i, Beta1, v0, dV, v1, v2))
            y2.append(T2(i, Beta2, v0, dV, v1, v2))


    

    # Plot everything
    plt.figure(figsize=(10, 6))

    # Create plot
    plt.plot(Energy_v0, y1, label='β = 4')

    plt.plot(Energy_v0, y2, label='β = 10')


    fileName = f"T vs E_V0 for β = 4 and β = 10 (V0 = {v0})"
    title = f"Transmission of a wave through a Potential Barrier where V0 = {v0} \n based on it's incoming Energy E/V0 for β = {Beta1} and β = {Beta2}"

    # Add title and labels
    plt.title(title)
    plt.xlabel("Energy of Wave over Potential Barrier (E/V0)")
    plt.ylabel("Transmission")
    plt.legend()
    plt.grid()

    # Show plot
    plt.savefig(fileName)

# Get Pi multiple Values

def GetPiMultiples (v0: float):
     # Betas
    Beta1 = 4
    Beta2 = 10

    # Potentials
    v1 = 0
    v2 = v0
    v3 = 0
    dV = v2 - v1

    # Error Value
    delta = 10e-10

    Energy_v0 = np.linspace(0.01, 10, 1000000)

    y1 = []
    y2 = []

    # Populate the y Values
    for i in Energy_v0:

        if i > v0:
            y1.append(T1(i, Beta1, v0, dV, v1, v2))
            y2.append(T1(i, Beta2, v0, dV, v1, v2))
        else:
            y1.append(T2(i, Beta1, v0, dV, v1, v2))
            y2.append(T2(i, Beta2, v0, dV, v1, v2))
    xPos1 = []
    xPos2 = []

    # Determine X values where T = 1 (we know it should be a multiple of pi so we calculate to see the value of the multiple)
    for i in range(len(y1)):

        E = Energy_v0[i]*v0

        if (abs(y1[i] - 1) <= delta):
            k2d = Beta1 * sqrt(E/v0)

            multiple = round(k2d/pi)
            if (multiple not in xPos1):
                xPos1.append(multiple)

        if (abs(y2[i] - 1) <= delta):
            k2d = Beta2 * sqrt(E/v0)
            multiple = round(k2d/pi)
            if (multiple not in xPos2):
                xPos2.append(multiple)

    print(f"Beta = {Beta1} Transmission = 1, k2d Pi Mutiples (V0 = {v0})")
    print (xPos1)

    print(f"Beta = {Beta2} Transmission = 1, k2d Pi Mutiples (V0 = {v0})")
    print(xPos2)

for v0 in range(-9,10):
    GetPiMultiples(v0)
    PlotFunction(-v0)
