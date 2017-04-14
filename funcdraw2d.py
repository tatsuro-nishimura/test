import numpy as np
import matplotlib.pyplot as plt


class DrawExplicitFunc2d:
    def __init__(self,
                 func=(lambda x: 0.1 * x + np.sin(x)),
                 xinterval_first=np.arange(-np.pi, np.pi, 0.1),
                 xspeed=0.1):
        self.func = func
        self.x = xinterval_first
        self.xspeed = xspeed

    def dynamic_plot(self):
        axis = plt.subplots(1, 1)[1]
        x = self.x
        y = self.func(x)
        curve = axis.plot(x, y)[0]
        while True:
            x += self.xspeed
            y = self.func(x)
            curve.set_data(x, y)
            axis.set_xlim((x.min(), x.max()))
            axis.set_ylim((1.1 * y.min() - 0.1 * y.max(),
                           1.1 * y.max() - 0.1 * y.min()))
            plt.pause(.01)


def main():
    DrawExplicitFunc2d().dynamic_plot()


if __name__ == "__main__":
    main()
