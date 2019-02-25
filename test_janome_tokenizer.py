from janome.tokenizer import Tokenizer
from collections import Counter

def count_noun(doc):
    t = Tokenizer()
    list_noun = [token.surface for token in t.tokenize(doc) if token.part_of_speech.startswith('名詞')]
    return Counter(list_noun).most_common()

def main():
    d0 = '''
    春は、あけぼの。やうやう白くなりゆく山ぎは　少し明りて紫だちたる雲の細くたなびきたる。
    夏は、夜。月の頃はさらなり。闇もなほ。螢の多く飛び違ひたる。また、ただ一つ二つなど、
    ほのかにうち光りて行くもをかし。雨など降るもをかし。
    秋は、夕暮。夕日のさして、山の端いと近うなりたるに、烏の寝どころへ行くとて、三つ四つ、
    二つ三つなど、飛び急ぐさへあはれなり。まいて雁などの列ねたるがいと小さく見ゆるは、
    いとをかし。日入り果てて、風の音、虫の音など、はたいふべきにあらず。
    冬は、つとめて。雪の降りたるはいふべきにもあらず。霜のいと白きも、またさらでも、
    いと寒きに、火など急ぎ熾して、炭もて渡るも、いとつきづきし。昼になりて、
    ぬるくゆるびもていけば、火桶の火も、白き灰がちになりて、わろし。
    '''
    print(count_noun(d0))


if __name__ == '__main__':
    main()
