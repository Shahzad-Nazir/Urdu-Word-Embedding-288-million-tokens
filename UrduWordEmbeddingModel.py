from __future__ import print_function



import pandas as pd

import pickle
import gensim
# -------------------------------save/load--------------------------------------


def save(obj, filename):
    print("saving {} ..".format(filename))
    with open(filename, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load(filename):
    print("loading {} ..".format(filename))
    with open(filename, 'rb') as handle:
        return pickle.load(handle)

reviews_csv ="urdu-news-dataset-1M.csv"
reviews = pd.read_csv(reviews_csv)
documents = reviews["News Text"]
summary = reviews["Headline"]

print("done loading data")

News_tokens = []
print("Document appending started for News Text")

for doc in documents:
    News_tokens.append(str(doc).split())

print("Document appending ended for News Text")
print("Sving ...")
save(News_tokens , "clean_documents_ketab.pkl")
print("News Text Saved..")

summary_tokens = []
print("loading summaries...")
for doc in summary:
    summary_tokens.append(str(doc).split())

save(summary_tokens , "clean_summary_ketab.pkl")
print("successfully appended")


complete_tokens = News_tokens + summary_tokens
print("starting training")

# we can change the size of vector and window sizes
model_urdu_vec = gensim.models.Word2Vec(
    complete_tokens,
        size=100,
        window=3,
        min_count=10,
        workers=4)
model_urdu_vec.train(complete_tokens, total_examples=len(complete_tokens), epochs=10)
model_urdu_vec.wv.save("model_urdu100-3.model")
print("done training and saving")