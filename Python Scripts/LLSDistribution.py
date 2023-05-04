import pandas as pd
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

data= pd.read_csv("LLSDistributionPPIGS.txt", delimiter = "\t")
print(data)
f, ax = plt.subplots()
print(data)
df_gb = data.groupby('NetworkName').count()
medians = data.groupby(['NetworkName'])['LLS'].median()
Average = data.groupby(['NetworkName'])['LLS'].mean()
minumim = data.groupby(['NetworkName'])['LLS'].max()
caps = data.groupby(['NetworkName'])['LLS'].min()
##ax.set_yscale("log")
y_values = data["LLS"].values
#data.boxplot(column='LLS', by='NetworkName', showmeans=True ,showfliers=True)
box_plot=sns.boxplot(x='NetworkName', y='LLS',data=data, order=["BIOGRID_LEL","BIOGRID_SCS","BIOGRID_SMA",
                                            "BIOGRID_EIS","Reactomepathway_LEL","Reactomepathway_SCS","Reactomepathway_SMA",
                                                                 "Reactomepathway_EIS","IntAct_LEL","IntAct_SCS","IntAct_SMA",
                                                                 "IntAct_EIS","HEL_LEL","MCS_SCS","SSA_SMA", "MGS_EIS"],showmeans=True,showfliers=True)

#print(medians)
print(Average)
print(minumim)

##ax = box_plot.axes
lines = ax.get_lines()
plt.xticks(rotation=75)
"""categories = ax.get_xticks()
for cat in categories:
    # every 4th line at the interval of 6 is median line
    # 0 -> p25 1 -> p75 2 -> lower whisker 3 -> upper whisker 4 -> p50 5 -> upper extreme value
    y = round(lines[4+cat*6].get_ydata()[0],1) 
    print(y)
    ax.text(
        cat, 
        y, 
        f'{y}', 
        ha='center', 
        va='center', 
        fontweight='bold', 
        size=5,
        color='white',
        bbox=dict(facecolor='#445A64'))"""
plt.xlabel('Gold Standard_Datasets')
plt.ylabel('Confidence Scores(LLS scores)')
##plt.title('Confidence scores (LLS scores)\n using different GS data')
##plt.savefig('LLSPPIGSs.png', dpi=300)
plt.tight_layout()
plt.savefig('LLSScoresCIBCB.jpg',bbox_inches='tight', bottom=19, dpi=300)
plt.tight_layout()
plt.show()

