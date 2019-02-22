# try to answer the problems in http://www.cl.ecei.tohoku.ac.jp/nlp100/
# sorry, not completed
import re
import random


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

def a06(str0, str1):
    set0 = set(a05(str0, 2))
    set1 = set(a05(str1, 2))
    return set0|set1, set0&set1, set0-set1, set(['se'])<=set0, set(['se'])<=set1

def a07(x, y, z):
    return str(x)+'時の'+str(y)+'は'+str(z)

def cipher(str0):#this is for problem 08
    return(''.join([chr(219 - ord(ch0)) if ch0.islower() else ch0 for ch0 in str0]))

def a09(sentence0):
    return ' '.join([word0[0]+''.join(random.sample(word0[1:len(word0)-1],len(word0)-2))+word0[len(word0)-1] if len(word0)>4 else word0 for word0 in sentence0.split()])

def main():
    print(a00('stressed'))
    print(a01('パタトクカシーー'))
    print(a02('パトカー', 'タクシー'))
    print(a03('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'))
    print(a04('Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'))
    print(a05('I am an NLPer'.split(), 2))
    print(a05('I am an NLPer', 2))
    print(a06('paraparaparadise', 'paragraph'))
    print(a07(12, '気温', 22.4))
    print(cipher('I am an NLPer'))
    print(cipher(cipher('I am an NLPer')))
    print(a09('Carl Friedrich Gauss was a German mathematician and physicist who made significant contributions to many fields in mathematics and sciences'))

if __name__ == '__main__':
    main()
