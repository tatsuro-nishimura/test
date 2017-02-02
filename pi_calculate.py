import numpy as np

# make pi class
class pi:
    def __init__(self, a, b, s, t):
        self.a = a
        self.b = b
        self.s = s
        self.t = t
    # define calculation of pi by Gauss-Legendre algorithm
    def calculate_pi(self, epsilon):
        while (self.a - self.b) > epsilon:
            y = (self.a + self.b)/2
            c = self.a - y
            self.b = np.sqrt(self.a * self.b)
            self.a = y
            self.s = self.s - self.t * c**2
            self.t = 2 * self.t
        return(self.a * self.b / self.s)


# set parameters
a = 1.0
b = np.sqrt(2)/2
s = 0.25
t = 1.0
# set allowable error
epsilon = 10**(-5)

# calculate pi
pi_value = pi(a, b, s, t).calculate_pi(epsilon)
print(format(pi_value, '.20g'))
