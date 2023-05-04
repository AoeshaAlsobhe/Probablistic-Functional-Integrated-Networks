import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data1 = pd.read_csv('LELdatasetsLLS.txt', sep="\t")

print(data1)


##plt.hist(data1["Weight"], label="Weight", log=True)
data1.boxplot(column='LLS',showmeans=True,showfliers=False);
plt.xlabel('LLS score')
plt.ylabel('Frequency')
plt.show();
