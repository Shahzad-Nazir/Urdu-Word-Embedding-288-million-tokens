import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('wordSim353.csv')

W_1 = df.score # annotated score
W_2 = df["512-7"] # model score

#print(W_2)
print(pearsonr(W_1, W_2))