# Urdu_Word_Embedding 288 million tokens
This is a large scale urdu word embedding mode. The model is trained over 288 million tokens
# Download
The two Urdu word embedding models with high performance can be downloaded from [here](https://drive.google.com/drive/folders/1rUEjgWz1MpsOFtSQ027S2rcza9YeFgjx?usp=sharing)
# How to use
just download the model and put it in your project file. You can use model in .py file with following code.

from gensim.models import KeyedVectors

model = KeyedVectors.load("vectors/vector-500/model_urdu500-5.model", mmap='r')

print(model.most_similar("سندھ" ))

# Code
The code for training is made available. UrduWordEmbeddingModel.py can create a complete trained model

