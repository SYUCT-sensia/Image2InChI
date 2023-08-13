import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


my_palette = sns.color_palette(['#77C4D3', '#E5E059', '#f3a598', '#000000'])

sns.set(style="whitegrid")
plt.rcParams["font.sans-serif"] = ["SimHei"]

df = pd.read_csv('Violin_all.csv', encoding='GBK')


df1 = df.iloc[:, :3]  # JPO
df2 = df.iloc[:, 3:6]  # CLEF
df3 = df.iloc[:, 6:9]  # UOB
df4 = df.iloc[:, 9:12]  # BMS1000


title_fontsize = 24
label_fontsize = 24


f, axes = plt.subplots(1, 4, figsize=(20, 11), sharey=True, gridspec_kw={'wspace': 0.04})

for i, (title, df_group) in enumerate(zip(['JPO', 'CLEF', 'UOB', 'BMS1000'], [df1, df2, df3, df4])):
    ax = axes[i]
    sns.violinplot(data=df_group, ax=ax, bw=.3, cut=1, linewidth=1.5, palette=my_palette, inner="box", positions=[0, 1], width=0.7)
    sns.boxplot(data=df_group, ax=ax, color='white', width=0.15, boxprops=dict(edgecolor=my_palette[3], linewidth=0.3),
                whiskerprops=dict(color=my_palette[3], linewidth=1.5), medianprops=dict(color=my_palette[3], linewidth=1.5))
    ax.set_xticklabels('')
    if i == 0:
        ax.set_ylabel('Accuracy of LCS', fontsize=label_fontsize)
    else:
        ax.set_ylabel('')
    ax.set(ylim=(0, 1))
    ax.tick_params(axis='y', labelsize=label_fontsize)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xlabel(title, fontsize=label_fontsize)
    # ax.set_title(title, fontsize=title_fontsize)


legend_handles = [plt.Rectangle((0,0),1,1, color=color) for  color in my_palette]
f.legend(legend_handles, ['DECIMER', 'Imago', 'Image2InChI'], loc='lower center', ncol=4, frameon=False,fontsize=title_fontsize)


# f.suptitle('Comparison of LCS accuracy on four datasets', fontsize=title_fontsize+4)
# f.text(0.5, -0.05, 'Datasets', fontsize=label_fontsize)
# f.text(-0.05, 0.5, 'LCS Accuracy', va='center', rotation='vertical', fontsize=label_fontsize)


plt.savefig('violin.jpg', dpi=1200, bbox_inches='tight')
plt.savefig('violin.svg', dpi=1200, bbox_inches='tight')
plt.show()
