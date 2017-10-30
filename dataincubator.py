import os
from random import shuffle
import pandas as pd

systems = [ 'spear', 'sqlite', 'x264', 'sac',]

data_folder = './data/'

files = {}
for system in systems:
    for f in os.listdir(data_folder):
        if system not in files.keys():
            files[system] = []
        files[system].append(data_folder + f)

for system in systems:
    # Randomly choose scenarios
    t_files = files[system]
    shuffle(t_files)
    files1 = t_files[0]
    files2 = t_files[1]

    content1 = pd.read_csv(files1)

    columns = content1.columns
    ctrain_indep = [c for c in columns if '<$' not in c]
    ctrain_dep = [c for c in columns if '<$' in c]
    content1 = content1.sort(ctrain_dep)

    x = []
    y1 = []
    for i,c in content1.iterrows():
        x.append(','.join(map(str, c[ctrain_indep].tolist())))
        y1.append(c[ctrain_dep].tolist()[-1])


    import matplotlib.pyplot as plt
    plt.plot(range(len(y1)), y1, color='b')
    plt.xlabel('Configurations')
    plt.ylabel('Performance Measure')

    plt.savefig('Figures/' + system + ".png")
    plt.cla()