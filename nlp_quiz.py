# try to answer the problems in http://www.cl.ecei.tohoku.ac.jp/nlp100/
# sorry, not completed
import re
import random


def a00(str):
    return str[::-1]

def a01(str):
    return str[::2]

def a02(str0, str1):
    return ''.join([x + y for (x, y) in zip(str0, str1)])

def a03(str):
    return [len(x) for x in re.sub('[,.]', '', str).split(' ')]

def a04(str):
    list0 = str.replace('.','').split()
    list1 = [list0[i][0] if i in [0,4,5,6,7,8,14,15,18] else list0[i][0:2] for i in range(0,len(list0))]
    return dict([(list1[i],i+1) for i in range(0,len(list1))])

def a05(seq, n):
    return [seq[i:i+n] for i in range(0,len(seq)-n+1)]

def a06(str0, str1):
    set0 = set(a05(str0, 2))
    set1 = set(a05(str1, 2))
    return set0|set1, set0&set1, set0-set1, set(['se'])<=set0, set(['se'])<=set1

def a07(x, y, z):
    return str(x)+'時の'+str(y)+'は'+str(z)

def cipher(str):
    return(''.join([chr(219 - ord(ch)) if ch.islower() else ch for ch in str]))

def str_shuffle(str):
    return ''.join(random.sample(str,len(str)))

def a09(sentence):
    return ' '.join([word[0]+str_shuffle(word[1:len(word)-1])+word[len(word)-1] if len(word)>4 else word for word in sentence.split()])

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
    print(cipher('I am an NLPer'))#this is for problem 08
    print(cipher(cipher('I am an NLPer')))
    print(a09('Carl Friedrich Gauss was a German mathematician and physicist who made significant contributions to many fields in mathematics and sciences'))

if __name__ == '__main__':
    main()
