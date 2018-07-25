import jieba
from wordcloud import WordCloud
from matplotlib import pyplot

from searchserver.parserHtml import parser
from searchserver.postAndDowload import post


def search(keyword):
    content = post(keyword)
    data = parser(content)
    wordlist = jieba.cut(data, cut_all=True)
    wordlist_split = ''.join(wordlist)
    wordcloud = WordCloud().generate(wordlist_split)
    print(wordcloud)
    img = pyplot.imshow(wordcloud)
    pyplot.axis('off')
    pyplot.show()
    return img



