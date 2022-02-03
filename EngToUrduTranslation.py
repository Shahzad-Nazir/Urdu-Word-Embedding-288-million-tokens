import json
import os
import pandas
import io
import sys
import re
from googletrans import Translator
from gensim.models import KeyedVectors


#load file wordSim353.csv or simlex-999.csv
df = pandas.read_csv('wordSim353.csv')

#word pairs
W_1 = df.word1 #first column
W_2 = df.word2 #second column


translator = Translator()

k = 0
# for LexSim-999 set loop to 998 and for WordSim-353 set loop to 351
while(k<=998):

    #
    try:
        #word_1 = translator.translate(W_1[k] , dest="ur")
        word_2 = translator.translate(W_2[k], dest='ur')
  #  print(word_2.text)
        print(word_2.text)
    except:
        print(k)

    k = k + 1
