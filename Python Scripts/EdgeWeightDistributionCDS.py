import pandas as pd
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

data= pd.read_csv("EdgeWeightDistributionCDS.txt", delimiter = "\t")
f, ax = plt.subplots()
print(data)
df_gb = data.groupby('Probabilistic Integrated Networks').count()
medians = data.groupby(['Probabilistic Integrated Networks'])['Integrated score'].median()
Average = data.groupby(['Probabilistic Integrated Networks'])['Integrated score'].mean()
minumim = data.groupby(['Probabilistic Integrated Networks'])['Integrated score'].max()
caps = data.groupby(['Probabilistic Integrated Networks'])['Integrated score'].min()
##ax.set_yscale("log")
y_values = data["Integrated score"].values
##data.boxplot(column='Size', by='Threshold', showmeans=True ,showfliers=True)
box_plot=sns.boxplot(data=data, x='Probabilistic Integrated Networks', y='Integrated score', order=["BIOGRID_CDS", "Reactomepathways_CDS", "IntAct_CDS", "UNIPROT_CDS", "OMIM_CDS"],showmeans=True,showfliers=True)

#print(medians)
print(Average)
#print(minumim)

ax = box_plot.axes
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
plt.xlabel('Probabilistic Functional Integrated Networks')
plt.ylabel('Edge Weight (Integrated Scores)')
##plt.title('Confidence scores (LLS scores)\n using different GS data')

##plt.savefig('LLSPPIGSs.png', dpi=300)
plt.tight_layout()
plt.savefig('EdgeWeightEval.jpg',bbox_inches='tight', bottom=19, dpi=600)
plt.tight_layout()
plt.show()


