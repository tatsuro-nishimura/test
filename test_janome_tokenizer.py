from janome.tokenizer import Tokenizer
from collections import Counter

def count_noun(sentence):
    t = Tokenizer()
    list_noun = [token.surface for token in t.tokenize(sentence) if token.part_of_speech.startswith('名詞')]
    return Counter(list_noun).most_common()

def main():
    c = count_noun('なんというベストタイミング魔法使いによって頭を爬虫類の姿に変えられたカイマンが、本来の姿を取り戻すため、友達のニカイドウと共に、魔法使い狩りに立ち上がる！')
    print(c)


if __name__ == '__main__':
    main()
