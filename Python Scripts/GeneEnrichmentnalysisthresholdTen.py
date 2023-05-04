import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv('SpecificityComparative.csv', sep=",")

#sns.boxplot(x="variable", y="value", data=pd.melt(df))
##plt.show()
print(df)
boxplot=df.boxplot(column=['UnweightedGGPFINs', 'WeightedGGPFINs'])
plt.ylabel('Cluster Specificity')
plt.show()


