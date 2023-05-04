import pandas as pd
import matplotlib.pyplot as plt
data1 = pd.read_csv('ClusterAverageAllNetwork.txt', sep="\t")
#inflation=[1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5,7.0, 7.5]
network=['UNIPROT_IES', 'OMIM_IES', 'SSA_SMA', 'MCS_SCS', 'MGS_IES', 'HEL_LEL','BIOGRID_IES', 'Reactomepathways_IES', 'IntAct_IES' ]
marker=["o", "*", "P", "d", "p", "v", "<", ">", "h", "x",".", ",", "4", "3"] 
counter=0


colours=["red", "blue", "pink", "green", "black", "brown", "orange", "purple", "darkcyan", "yellow","darkgreen","magenta","darkred"]
for i in network:
   plt.plot(data1['Threshold'], data1[i],color=colours[counter], marker=marker[counter],label = i)
   counter+=1
##   plt.plot(data1['cluster'], data1['Average2'], color='blue', marker='o',label = "line 2")
#plt.title('The cohesiveness of the network clusters with different inflation value', fontsize=10)
plt.xlabel('Threshold Value', fontsize=10)
plt.ylabel('Cluster Average Cohesiveness', fontsize=10)
plt.grid(True)
plt.legend(loc = "lower right",bbox_to_anchor = (1.5, -0.01))

plt.savefig('ClusterAverage.png',dpi=300, bbox_inches='tight')
