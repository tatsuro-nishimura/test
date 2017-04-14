import numpy as np
import matplotlib.pyplot as plt


class DrawExplicitFunc2d:
    def __init__(self,
                 func=(lambda x: 0.1 * x + np.sin(x)),
                 x_first=np.arange(-np.pi, np.pi, 0.1),
                 x_speed=0.1):
        self.func = func
        self.x = x_first
        self.y = self.func(self.x)
        self.xspeed = x_speed

    def dynamic_plot(self):
        axis = plt.subplots(1, 1)[1]
        curve = axis.plot(self.x, self.y)[0]
        while True:
            self.x += self.x_speed
            self.y = self.func(self.x)
            curve.set_data(self.x, self.y)
            axis.set_xlim((self.x.min(), self.x.max()))
            axis.set_ylim((1.1 * self.y.min() - 0.1 * self.y.max(),
                           1.1 * self.y.max() - 0.1 * self.y.min()))
            plt.pause(.01)


def main():
    DrawExplicitFunc2d().dynamic_plot()


if __name__ == "__main__":
    main()
