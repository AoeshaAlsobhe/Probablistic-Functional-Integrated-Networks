import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
# prepare data
data= pd.read_csv('EdgeWeightDistributionCorrolationHEL&&BIOGRID.txt', sep="\t")
##data[["LTPScore", "HELScore"]].corr()
corr, _ = pearsonr(data["HEL_LEL"], data["BIOGRID_LEL"])
print(corr)
# summarize
"""print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))"""
# plot
plt.scatter(data["HEL_LEL"], data["BIOGRID_LEL"])
plt.xlabel('HEL_LEL')
plt.ylabel('BIOGRID_LEL')
plt.xlim(-1, 176)
plt.ylim(-1, 176)


plt.show()
