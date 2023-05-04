import os
import pandas as pd
import csv
import sklearn.metrics as metrics
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import *
colours=["blue", "red", "gold", "green", "darkviolet",'cyan','blue','magenta', "coral", "darkgoldenrod", "crimson", "blueviolet","purple","olive","pink",'yellow','brown', 'orange','gray', 'magenta']
counter=0
Average=0
entries = os.listdir('/Users/aoeshaalsobhe/Documents/LasMGG')
entries = sorted(entries)
print(entries)
order2=['BIOGRID.txt', 'MGScoredNetworkPredictingMG.txt', 'OMIMScoredNetworkPredictingMG.txt', 'ReactomePathway.txt']
order=['BIOGRIDScoredNetworkPredictMG.txt', 'MGScoredNetworkPredictingMG.txt', 'OMIMScoredNetworkPredictingMG.txt', 'ReactomePathwayScoredNetworkPredictMG.txt']
for i in order:
    #print(counter)
    X=i.split(".")
    #print(type(X))
    #print(i)
    fpr1_i=[]
    tpr1_i=[]

    with open (i, "r",encoding='utf-8',errors='ignore') as f:
         reader = csv.reader(f, delimiter = "\t")
         next(f)
         for j in reader:
            tpr1_i.append((float(j[0])))
            fpr1_i.append((1.0-float(j[1])))
    
    
    auc1_i = metrics.auc(fpr1_i,tpr1_i)
    print(i)
    print(auc1_i)
    plt.plot(fpr1_i,tpr1_i,label= X[0]+" =%0.9f"% auc1_i,color=colours[counter], linewidth=3)
    
    counter+=1
    Average+=auc1_i
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.0])
plt.ylabel('True Positive Rate : Sensitivity' )
plt.xlabel('False Positive Rate: 1-Specificity')
plt.legend(loc='center left', bbox_to_anchor=(0.99, 0.5))
#plt.title('Receiver Operating Characteristic')
    
    
plt.plot([0,1],[0,1],'r--',label='random')
#plt.plot(fpr1_i,tpr1_i,label= "Average =%0.2f"% 0.66,color=colours[counter], linewidth=3)
print("Average")
print(Average/10)
#plt.tight_layout()
plt.savefig('AUCLinkPrediction5Networks.jpg',bbox_inches='tight', dpi=300)
#plt.tight_layout()
plt.show()

