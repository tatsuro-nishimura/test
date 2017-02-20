import decimal
import numpy as np

# make pi class
class Pi:
    def __init__(self, a, b, s, t):
        self.a = a
        self.b = b
        self.s = s
        self.t = t
    # define calculation of pi by Gauss-Legendre algorithm
    def calculate_pi_GL(self, epsilon):
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

    # define calculation of pi by montecarlo
    def calculate_pi_monte(self, number_monte):
        counter = 0
        for i in range(0, number_monte):
            x = np.random.rand(1000)
            y = np.random.rand(1000)
            counter += sum(x**2 + y**2 < 1)
        pi_monte = counter / (number_monte*250)
        return(pi_monte)

    # define calculation of pi by zeta(2) (or Basel problem)
    def calculate_pi_zeta(self, number_zeta):
        seq = np.cumsum(np.ones(number_zeta))
        pi_zeta = np.sqrt(6*sum(seq**(-2)))
        return(pi_zeta)

    # define calculation of pi by perimeter of regular polygon
    def calculate_pi_poly(self, number_poly):
        theta = np.pi/number_poly
        inner_perimeter = number_poly*np.sin(theta)
        outer_perimeter = number_poly*np.tan(theta)
        return((inner_perimeter + outer_perimeter) / 2)


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
    number_monte = 1000
    number_zeta = 1000000
    number_poly = 1000000
    Pi_c = Pi(a, b, s, t)
    # calculate pi by Gauss-Legendre method
    pi_calc = Pi_c.calculate_pi_GL(epsilon)
    print('Approximate value of Pi(Gauss-Legendre): {pi_calc[0]}'.format(**locals()))
    print('Number of iterations(Gauss-Legendre): {pi_calc[1]}'.format(**locals()))
    # calculate pi by montecarlo
    pi_calc = Pi_c.calculate_pi_monte(number_monte)
    print('Approximate value of Pi(montecarlo): {pi_calc}'.format(**locals()))
    # calculate pi by zeta
    pi_calc = Pi_c.calculate_pi_zeta(number_zeta)
    print('Approximate value of Pi(zeta(2)): {pi_calc}'.format(**locals()))
    # calculate pi by perimeter of regular polygon
    pi_calc = Pi_c.calculate_pi_poly(number_poly)
    print('Approximate value of Pi(polygon): {pi_calc}'.format(**locals()))


if __name__ == '__main__':
    main()
