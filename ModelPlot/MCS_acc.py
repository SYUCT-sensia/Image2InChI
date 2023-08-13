import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False


colors = ['#469EB4', '#87CFA4', '#CBE99D', '#CCFFCC', '#FEE89A', '#FDB96A', '#F57547', '#D6404E']


df = pd.read_csv('Model_MCS_acc.csv')


y1 = df['Imago']
y2 = df['MolVec']
y3 = df['OSRA']
y4 = df['DECIMER']
y5 = df['MolMiner']
y6 = df['MICER']
y7 = df['MolScribe']
y8 = df['Image2InChI']


width = 0.1
labels = ['BMS1000', 'JPO', 'CLEF', 'UOB']
x = np.arange(len(labels))

def to_percent(temp, position):
    return '%1.0f' % (100 * temp) + '%'

fig, ax = plt.subplots(figsize=(10, 6))

plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.ylim(0, 1)
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

rects1 = ax.bar(x-3*width, height=y1, width=width, label='Imago', color=colors[0], edgecolor='white')
rects2 = ax.bar(x-2*width, height=y2, width=width, label='MolVec', color=colors[1], edgecolor='white')
rects3 = ax.bar(x-width, height=y3, width=width, label='Osra', color=colors[2], edgecolor='white')
rects4 = ax.bar(x, height=y4, width=width, label='DECIMER', color=colors[3], edgecolor='white')
rects5 = ax.bar(x+width, height=y5, width=width, label='MolMiner', color=colors[4], edgecolor='white')
rects6 = ax.bar(x+2*width, height=y6, width=width, label='MICER', color=colors[5], edgecolor='white')
rects7 = ax.bar(x+3*width, height=y7, width=width, label='MolScribe', color=colors[6], edgecolor='white')
rects8 = ax.bar(x+4*width, height=y8, width=width, label='Image2InChI', color=colors[7], edgecolor='white')

ax.set_ylabel('MCS acc', fontsize=24)

ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.tick_params(labelsize=22)


ax.legend(fontsize=20, loc='lower center', bbox_to_anchor=(0.5, -0.35), ncol=4)

plt.savefig("./MCS acc V2.svg", bbox_inches='tight')
plt.savefig("./fig16(b).jpg", bbox_inches='tight')
plt.show()