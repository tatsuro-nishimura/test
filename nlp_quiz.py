# try to answer the problems in http://www.cl.ecei.tohoku.ac.jp/nlp100/
# not completed
import re


def a00(str0):
    return str0[::-1]

def a01(str0):
    return str0[::2]

def a02(str0, str1):
    return ''.join([x + y for (x, y) in zip(str0, str1)])

def a03(str0):
    return [len(x) for x in re.sub('[,.]', '', str0).split(' ')]

def main():
    print(a00('stressed'))
    print(a01('パタトクカシーー'))
    print(a02('パトカー', 'タクシー'))
    print(a03('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'))

if __name__ == '__main__':
    main()
