import pandas as pd
import jieba
import re 

def normalize_corpus(corpus, tokenize=False):
    normalized_corpus = []
    for text in corpus:
        text = ''.join(text.split(" "))
        # print(text)
        text = remove_stopwords(text)
        normalized_corpus.append(text)
        if tokenize:
            text = tokenize_text(text)
            normalized_corpus.append(text)
    return normalized_corpus

def tokenize_text(text):
    text = text.strip()
    # print(txt)
    tokens = jieba.cut(text)
    # tokens = [token for token in tokens]
    # print(tokens)
    return tokens

def remove_stopwords(text):
    tokens = tokenize_text(text)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_text = filtered_tokens
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


with open("./src/stopwords/hit_stopwords.txt", encoding="utf8") as f:
    stopword_list = f.readlines()
    stopword_list = [i.strip() for i in stopword_list]
    stopword_list.append("\n")
    stopword_list.append("\r")
    stopword_list.append(" ")
    stopword_list.append("　")
    stopword_list.append(u"\u3000")
    # print(stopword_list)



# jieba.load_userdict("./src/jiayan_dict.txt")
pdtxt = pd.DataFrame(columns = ["content","target"])
txt = pd.read_table("./src/classifier_content/期刊论文文本.txt",header=None,sep = "\n")
txt.columns = ["content"]
# print(txt)
pdtxt["content"] = txt["content"]
pdtxt["target"] = "3" #在此设置target = 1 是词类 2是诗类 3是期刊 4是新闻 5是文言文

pdtxt["content"] = normalize_corpus(pdtxt["content"])
print(pdtxt)

pdtxt.to_csv("paper.csv",index=False,sep=',')