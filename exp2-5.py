import math
import numpy as np
import matplotlib.pyplot as plt

PART_REYNOLDS_NUMBER = False
PART_NUSSELT_NUMBER = False
PART_DRAW = True

Q_flow = [2.880, 3.305, 3.857] # as x
R = [0.5652, 0.5490, 0.5287] # as y

coefficients = np.polyfit(Q_flow, R, 1)

regression_x = np.array([min(Q_flow), max(Q_flow)])
regression_y = np.polyval(coefficients, regression_x)

plt.scatter(Q_flow, R, color='blue', marker='o')

plt.plot(regression_x, regression_y, color='red', linestyle='--')

plt.xlabel('Qw (cfm)')
plt.ylabel('R (°C/W)')
plt.title('air flow rate v.s. thermal resistance chart')

plt.legend()

plt.show()