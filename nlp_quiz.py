# try to answer the problems in http://www.cl.ecei.tohoku.ac.jp/nlp100/
# sorry, not completed
import re


def a00(str0):
    return str0[::-1]

def a01(str0):
    return str0[::2]

def a02(str0, str1):
    return ''.join([x + y for (x, y) in zip(str0, str1)])

def a03(str0):
    return [len(x) for x in re.sub('[,.]', '', str0).split(' ')]

def a04(str0):
    list0 = str0.replace('.','').split()
    list1 = [list0[i][0] if i in [0,4,5,6,7,8,14,15,18] else list0[i][0:2] for i in range(0,len(list0))]
    return dict([(list1[i],i+1) for i in range(0,len(list1))])

def a05(seq0, n):
    return [seq0[i:i+n] for i in range(0,len(seq0)-n+1)]

def main():
    print(a00('stressed'))
    print(a01('パタトクカシーー'))
    print(a02('パトカー', 'タクシー'))
    print(a03('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'))
    print(a04('Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'))
    print(a05('I am an NLPer'.split(), 2))
    print(a05('I am an NLPer', 2))

if __name__ == '__main__':
    main()
