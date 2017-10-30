import os
from random import shuffle
import pandas as pd

file1 = "./data/sac_3.csv"
file2 = "./data/sac_4.csv"

content1 = pd.read_csv(file1)
content2 = pd.read_csv(file2)
columns = content1.columns
ctrain_indep = [c for c in columns if '<$' not in c]
ctrain_dep = [c for c in columns if '<$' in c]
content1 = content1.sort(ctrain_dep)

x = []
y1 = []
y2 = []
for i,c in content1.iterrows():
    x.append(','.join(map(str, c[ctrain_indep].tolist())))
    y1.append(c[ctrain_dep].tolist()[-1])

vals = {}
columns = content2.columns
ctrain_indep = [c for c in columns if '<$' not in c]
ctrain_dep = [c for c in columns if '<$' in c]
for i, c in content2.iterrows():
    key = ','.join(map(str, c[ctrain_indep].tolist()))
    vals[key] = c[ctrain_dep].tolist()[-1]

    
for xx in x:
    y2.append(vals[xx])

import matplotlib.pyplot as plt
plt.plot(range(len(y1)), y1, color='b', label='sac_3')
plt.plot(range(len(y2)), y2, color='r', label='sac_4')
plt.xlabel('Configurations')
plt.ylabel('Performance Measure')
plt.legend()
plt.savefig('Figures/sac_2.png')
plt.cla()
