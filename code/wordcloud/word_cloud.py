
import json
import jieba
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt

"""功能：输入诗人姓名 和诗人作品种类  （plus 如果不输入朝代就需要进入author.json判断诗人朝代 进入指定文本文件查找 ）
eg. input：李白 唐诗   output：李白的诗词词云"""


def input_produce():
    list = input("请先后输入作者姓名和作品种类并用空格分隔开，如“李白 唐诗”:").split()
    print(list)
    
    if list[1]=="唐朝" or list[1]=="唐" or list[1]=="唐代" or list[1]=="唐诗":
        with open("./src/tang_peom_trans.json",encoding="utf-8") as f:
            generate_word_cloud(list[0],f)
    elif list[1]=="宋诗":
        with open("./src/song_peom_trans.json",encoding="utf-8") as f:
            generate_word_cloud(list[0],f)
    elif list[1]=="宋词":
        with open("./src/ci_trans.json",encoding="utf-8") as f:
            generate_word_cloud(list[0],f)
    else:
        print("您输入的朝代诗文数据未被本项目记录")

def generate_word_cloud(poest,f):
    peom = ""
    s = json.load(f)
    for item in s:
        if item["author"] == poest:
            peom += "".join(item["paragraphs"])
    text_cut = jieba.lcut(peom)
    text_cut = " ".join(text_cut)
    
    stop_words = open("./src/dict.txt",encoding="utf8").read().split("\n")
    wc = WordCloud(background_color='white',font_path='msyh.ttc',height=600,width=800,\
                    max_words=200,max_font_size=80,stopwords=stop_words)
    wordcloud = wc.generate(text_cut)
    plt.subplots(figsize=(12,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
            
    
if __name__ == "__main__":
    jieba.load_userdict("./src/dict.txt")
    input_produce()
    
    