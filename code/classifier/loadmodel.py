import pickle
import jieba
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
sentence2pre = input("输入待测句子：").split()
# print(sentence2pre)
normalized = normalize_corpus(sentence2pre)
# print(normalized)
vector = pickle.load(open("code/classifier/vect.pkl",'rb'))
predict_features = vector.transform(normalized)
tfidf_mnb = open("code/classifier/model.pkl", "rb")
classifier = pickle.load(tfidf_mnb)
predict_result = classifier.predict(predict_features)[0]
 #1 是词类 2是诗类 3是期刊 4是新闻 5是文言文
if predict_result ==1 :
     print("是词类")
elif predict_result ==2 :
     print("是诗类")
elif predict_result ==3 :
     print("是期刊类") 
elif predict_result ==4 :
     print("是新闻类") 
elif predict_result ==5 :
     print("是文言文类") 