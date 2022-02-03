import json
import os
import pandas
import io
import sys
import re
from googletrans import Translator
from gensim.models import KeyedVectors
import xlrd



df = pandas.read_csv('simlex-999.csv')


W_1 = df.P1
W_2 = df.P2



translator = Translator()
model = KeyedVectors.load("vectors/vector-512/model_urdu512-7.model", mmap='r')
k = 0
count_no = 0
count_yes=0
while(k<=806):
    try:
        print(model.similarity(W_1[k],W_2[k] ))
        count_yes = count_yes + 1
        #print(W_1,W_2)
    except:
        print("the pair is not contained by vocabulary", k)
        count_no = count_no + 1
    k = k + 1
#
print(count_no)
print(count_yes)
#
#

#
