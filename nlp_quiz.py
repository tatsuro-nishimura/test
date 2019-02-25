# try to answer the problems in http://www.cl.ecei.tohoku.ac.jp/nlp100/
# sorry, under construction
import re
import random
import pandas as pd
import numpy as np
import gzip
import json


def reverse_str(str):
    return str[::-1]

def choose_odd_ch(str):
    return str[::2]

def a02(str0, str1):
    return ''.join([x + y for x, y in zip(str0, str1)])

def a03(str):
    return [len(x) for x in re.sub('[,.]', '', str).split(' ')]

def a04(str):
    list0 = str.replace('.','').split()
    list1 = [list0[i][0] if i in [0,4,5,6,7,8,14,15,18] else list0[i][0:2] for i in range(len(list0))]
    return dict([(list1[i], i+1) for i in range(len(list1))])

def a05(seq, n):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]

def a06(str0, str1):
    set0, set1 = set(a05(str0, 2)), set(a05(str1, 2))
    return set0|set1, set0&set1, set0-set1, {'se'}<=set0, {'se'}<=set1

def a07(x, y, z):
    return str(x)+'時の'+str(y)+'は'+str(z)

def cipher(str):
    return(''.join([chr(219 - ord(ch)) if ch.islower() else ch for ch in str]))

def shuffle_str(str):
    return ''.join(random.sample(str,len(str)))

def a09(sentence):
    return ' '.join([word[0]+shuffle_str(word[1:-1])+word[-1] if len(
        word)>4 else word for word in sentence.split()])

def a10_19(input, N):
    f = open(input)
    num_row = sum(1 for l in f)
    print(num_row)
    print('---' + '\n' + 'complete Q10! (except Linux com)' + '\n' + '---')
    f = open(input)
    list0 = [i.replace('\t', ' ').replace('\n','').split(' ') for i in f]
    print('---' + '\n' + 'complete Q11! (except Linux com)' + '\n' + '---')
    df = pd.DataFrame(list0).rename(
        columns={0:'prefecture', 1:'city', 2:'high_temprature', 3:'date'})
    cols = [col1, col2] = [df['prefecture'], df['city']]
    for i in range(1, 3):
        f = open('./col'+str(i)+'.txt', mode='w')
        f.write('\n'.join([x for x in cols[i-1]]))
    print('---' + '\n' + 'complete Q12! (except Linux com)' + '\n' + '---')
    f = open('./col1.txt'), open('./col2.txt')
    list = [f[0].readline().replace(
        '\n', '') +'\t'+ f[1].readline() for i in range(num_row)]
    f = open('./cols.txt', mode='w')
    f.write(''.join(list))
    f.close()
    print('---' + '\n' + 'complete Q13! (except Linux com)' + '\n' + '---')
    print(df.head(N).to_string(index=False, header=False))
    print(df.tail(N))
    print(np.array_split(list0, N))
    print(set(col1))
    df = df.sort_values(
        by=['high_temprature'], ascending=False).reset_index(drop=True)
    print(df)
    df_col1_size = pd.DataFrame(
        df.groupby('prefecture').size()).reset_index(
            ).rename(columns={0:'pref_count'})
    print(df_col1_size)
    #'left join' on pandas df
    df1 = pd.merge(df, df_col1_size, on='prefecture', how='left')
    #'order by -- desc' on pandas df
    df1 = df1.sort_values(
        by=['pref_count'], ascending=False).reset_index(drop=True)
    print(df1.drop('pref_count', axis=1))

def solve_chapter_one():
    print(reverse_str('stressed'))
    print(choose_odd_ch('パタトクカシーー'))
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
    print('---' + '\n' + 'complete chapter one!' + '\n' + '---')

def solve_chapter_two():
    a10_19('./hightemp.txt', 5)
    print('---' + '\n' + 'complete chapter two!(except linux com)' + '\n' + '---')

def solve_chapter_three():
    f = gzip.open('./jawiki-country.json.gz', 'rt')
    f1 = f.read()
    d1 = {}
    for l in f1.splitlines():
        d0 = json.loads(l)
        d1[d0['title']] = d0
    doc = d1['イギリス']['text']
    print(doc)
    doc_cat = '\n'.join([x for x in doc.splitlines() if '[[Category:' in x])
    print(doc_cat)
    cats = doc_cat.replace('[', '').replace(
        ']', '').replace('|*', '').replace('Category:', '')
    print(cats)
    list_sec = [x for x in doc.splitlines() if '==' in x]
    list_sec2 = [(x.replace('=',''), int(x.count('=')/2 - 1)) for x in list_sec]
    print(list_sec2)
    print('---' + '\n' + 'complete Q20-23!' + '\n' + '---')

def solve_chapter_four():
    # mecab neko.txt -o neko.txt.mecab
    f = open('neko.txt.mecab', 'r', encoding='utf8')
    num, dic = 0, {}
    for l in f:
        if l != 'EOS\n':
            dic[num] = l.replace('\t', ',').replace('\n','').split(',')
            num += 1
    num, dic_verb_surface = 0, {}
    for i in range(len(dic)):
        if dic[i][1] == '動詞':
            dic_verb_surface[num] = dic[i][0]
            num += 1
    num, dic_verb_base = 0, {}
    for i in range(len(dic)):
        if dic[i][1] == '動詞':
            dic_verb_base[num] = dic[i][7]
            num += 1
    print('---' + '\n' + 'complete Q30-32!' + '\n' + '---')

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def print(self):
        print([self.surface, self.base, self.pos, self.pos1])

class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def add_morph(self, morph):
        self.morphs += [morph]

    def get_chunk_and_dst(self):
        str = ''
        for morph in self.morphs:
            str += morph.surface
        return str, self.dst

class Doc:
    def __init__(self, doc):
        self.doc = doc

    def get_sentence_structure(self, num_sentence):
        list = []
        for chunk in self.doc[num_sentence].values():
            list += [chunk.get_chunk_and_dst()]
        return list

    def print_sentence(self, num_sentence):
        for chunk in self.doc[num_sentence].values():#answer to Q30
            for morph in chunk.morphs:
                morph.print()

    def print_sentence2(self, num_sentence):
        print(self.get_sentence_structure(num_sentence))#anster to Q31

    def print_sentence3(self, num_sentence):
        list = self.get_sentence_structure(num_sentence)
        for chunk in list:#anster to Q32
            if chunk[1] == -1:
                print(chunk[0])
            else:
                print(chunk[0]+'\t'+list[chunk[1]][0])

def add_scm_structure(f):
    num_sentence, num_chunk, doc = -1, -1, {}
    for l in f:
        if l[0:3] == '* 0':
            num_sentence += 1
            num_chunk = 0
            doc[num_sentence] = {}
            doc[num_sentence][num_chunk] = Chunk(
                int(l.split(' ')[2].replace('D', '')))
        elif l[0] == '*':
            num_chunk += 1
            doc[num_sentence][num_chunk] = Chunk(
                int(l.split(' ')[2].replace('D', '')))
        if l[0] != '*' and l != 'EOS\n':
            word = l.replace('\n', '').replace('\t', ',').split(',')
            doc[num_sentence][num_chunk].add_morph(
                Morph(word[0], word[7], word[1], word[2]))
        else:
            pass
    for num_sentence in range(len(doc)):
        for num_chunk in range(len(doc[num_sentence])):
            dst = doc[num_sentence][num_chunk].dst
            if dst != -1:
                doc[num_sentence][dst].srcs += [num_chunk]
    return doc

def solve_chapter_five():
    #cabocha -f1 neko.txt -o neko.txt.cabocha
    f = open('./neko.txt.cabocha')
    doc = Doc(add_scm_structure(f))
    doc.print_sentence(2)
    doc.print_sentence2(7)
    doc.print_sentence3(7)

def main():
    #solve_chapter_one()
    #solve_chapter_two()
    #solve_chapter_three()
    #solve_chapter_four()
    solve_chapter_five()

if __name__ == '__main__':
    main()
