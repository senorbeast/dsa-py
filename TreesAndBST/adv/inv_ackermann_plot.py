import numpy as np
import matplotlib.pyplot as plt
import math


# def inverse_ackermann(x):
#     if x < 3:
#         return 0
#     return math.log(x, 2)


# x_vals = np.linspace(1, 100, 1000)
# y_vals = [inverse_ackermann(t) for t in x_vals]


# plt.plot(x_vals, y_vals)
# plt.xlabel("x")
# plt.ylabel("Inverse Ackermann(x)")
# plt.title("Plot of Inverse Ackermann Function")
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt


def inverse_ackermann_tarjan(x):
    alpha = 0.5
    beta = 0.5
    k = 0
    while x > 1:
        x = max(int(x**alpha), 2)
        k += 1
    for _ in range(k):
        x = max(int(x**beta), 2)
    return k


x_vals = np.linspace(1, 100, 1000)
y_vals = [inverse_ackermann_tarjan(x) for x in x_vals]

plt.plot(x_vals, y_vals)
plt.xlabel("x")
plt.ylabel("Inverse Ackermann(x)")
plt.title("Plot of Inverse Ackermann Function (Tarjan)")
plt.grid(True)
plt.show()
