import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
# prepare data
data= pd.read_csv('ALLDGAScore.txt', sep="\t")
##data[["LTPScore", "HELScore"]].corr()
##corr, _ = pearsonr(data["LLSOMIMGS"], data["UniProtLLS"])
##print(data.corr())
# summarize
####print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
# plot




sns.heatmap(data[["LTP_GS", "HEL_GS", "MG_GS","OMIM_GS", "UniProt_GS", "MC_GS"]].corr(), annot = True, fmt='.2g',cmap= 'coolwarm',vmin=0, vmax=1)
"""plt.legend(loc = "upper center",bbox_to_anchor = (1.23,0.21))
plt.xlabel('LLS MC_GS, LLS HEL_GS, LLS LTP_GS')
plt.ylabel('LLS MG_GS, LLS HEL_GS, LLS LTP_GS')"""
plt.show()

