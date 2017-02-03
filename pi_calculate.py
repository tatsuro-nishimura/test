import decimal

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
            self.b = (self.a * self.b).sqrt()
            self.a = y
            self.s = self.s - self.t * c**2
            self.t = 2 * self.t
        return(self.a * self.b / self.s)


def main():
    D = decimal.Decimal
    # set decimal precision
    decimal.getcontext().prec = 1000
    # set allowable error
    epsilon = D(10)**(-300)
    # set parameters
    a = 1
    b = 1/D(2).sqrt()
    s = 1/D(4)
    t = 1
    # calculate pi
    pi_value = pi(a, b, s, t).calculate_pi(epsilon)
    print(pi_value)


if __name__ == '__main__':
    main()
