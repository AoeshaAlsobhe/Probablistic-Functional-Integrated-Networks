import pandas as pd
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

data= pd.read_csv("EdgeWeightDistributionThreshold Genetic.txt", delimiter = "\t")
Index=data["ThresholdWeight"].tolist()
h=Index.sort()
df = pd.DataFrame({"Total Unique Interactions":data["Interactions"].tolist(),
                   "Total Unique Genes":data["Genes"].tolist()}, index=Index)
ax=df.plot.bar(log = True)
print(Index)


plt.xlabel('Edge Weight Threshold')

plt.legend(loc='upper center', bbox_to_anchor=(0.77, 1.00)),

plt.xticks((range(len(data["ThresholdWeight"]))),Index, rotation=320, size=8)
plt.show()
