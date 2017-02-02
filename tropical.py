# make tropical class
class tropical:
    def __init__(self, maxmin = 'max'):
        self.maxmin = maxmin
    def sum(self, a, b):
        if self.maxmin == 'max':
            return(max(a, b))
        elif self.maxmin == 'min':
            return(min(a, b))
        else:
            return('error')
    def prod(self, a, b):
        return(a + b)


def main():
    print(tropical().sum(3, 41))
    print(tropical('min').sum(3, 41))
    print(tropical().prod(3, 41))


if __name__ == '__main__':
    main()
