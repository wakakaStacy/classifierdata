import pandas as pd
import jieba
import re 

def normalize_corpus(corpus, tokenize=False):
    normalized_corpus = []
    for text in corpus:
        text = remove_stopwords(text)
        normalized_corpus.append(text)
        if tokenize:
            text = tokenize_text(text)
            normalized_corpus.append(text)
    return normalized_corpus

def tokenize_text(text):
    tokens = jieba.cut(text)
    tokens = [token.strip() for token in tokens]
    return tokens

def remove_stopwords(text):
    tokens = tokenize_text(text)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


with open("./src/stopwords/hit_stopwords.txt", encoding="utf8") as f:
    stopword_list = f.readlines()
    stopword_list = [i.strip() for i in stopword_list]
    # print(stopword_list)



jieba.load_userdict("./src/jiayan_dict.txt")
pdtxt = pd.DataFrame(columns = ["content","target"])
txt = pd.read_table("./src/classifier_content/poem_text.txt",header=None)
txt.columns = ["content"]
pdtxt["content"] = txt["content"]

#加上<start> <end>的标签
for index in pdtxt["content"].index:
    string_txt = ""
    for j in pdtxt["content"][index].split("。"):
        j = "<start>"+j+"<end>"
        string_txt = string_txt + j
    pdtxt["content"][index] = string_txt

pdtxt["target"] = "1" #在此设置target = 1 是词类 2是诗类

pdtxt["content"] = normalize_corpus(pdtxt["content"])
print(pdtxt)

pdtxt.to_csv("poem_new.csv",index=False,sep=',') #重新转了poem的cs