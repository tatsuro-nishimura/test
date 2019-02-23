from janome.tokenizer import Tokenizer
from collections import Counter

def main():
    t = Tokenizer()
    s = 'なんというベストタイミング魔法使いによって頭を爬虫類の姿に変えられたカイマンが、本来の姿を取り戻すため、友達のニカイドウと共に、魔法使い狩りに立ち上がる！'
    list_noun = [token.surface for token in t.tokenize(s) if token.part_of_speech.startswith('名詞')]
    print(Counter(list_noun).most_common())


if __name__ == '__main__':
    main()
