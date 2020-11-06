import json
from langconv import *

k = open("C:/Users/12493/Desktop/python/文本/zh_classifier/src/classifier_content/文言文.txt", 'w+', encoding='utf-8')
with open("C:/Users/12493/Desktop/python/文本/zh_classifier/src/classifier_content/文言文数据.txt", encoding='utf-8') as f:
    for line in f:
        sentence = Converter('zh-hans').convert(line)   # 繁体转简体
        k.write(sentence)
    k.close()
    print("merge finished!")
