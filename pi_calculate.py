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
        counter = 0
        while (self.a - self.b) > epsilon:
            counter += 1
            y = (self.a + self.b)/2
            c = self.a - y
            self.b = (self.a * self.b).sqrt()
            self.a = y
            self.s = self.s - self.t * c**2
            self.t = 2 * self.t
        return(self.a * self.b / self.s, counter)


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
    pi_calc = pi(a, b, s, t).calculate_pi(epsilon)
    print("Approximate value of Pi: {pi_calc[0]}".format(**locals()))
    print("Number of iterations: {pi_calc[1]}".format(**locals()))


if __name__ == '__main__':
    main()
