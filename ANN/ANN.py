import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Library used to normalise the data
import sklearn
from sklearn import preprocessing

#Library to create boxplot
import seaborn as sns

data = pd.read_csv('Task3 - dataset - HIV RVG.csv')

#Splitting the data into 5 arrays
#Identifier(?)
i1 = data['Image number'].values
i2 = data['Bifurcation number'].values
i3 = data['Artery (1)/ Vein (2)'].values
i4 = data['Participant Condition'].values

#Features
f1 = data['Alpha'].values
f2 = data['Beta'].values
f3 = data['Lambda'].values
f4 = data['Lambda1'].values
f5 = data['Lambda2'].values


def compute_averages(dataset):
	print('Mean:', dataset.mean())
	print('SD:', dataset.std())
	print('Min value:', dataset.min())
	print('Max value:', dataset.max())


#Normalising (Can not use)
nf1 = sklearn.preprocessing.minmax_scale(f1, feature_range=(0, 1), axis=0, copy=True)
nf2 = sklearn.preprocessing.minmax_scale(f1, feature_range=(0, 1), axis=0, copy=True)

##Box Plots##
sns.boxplot(data['Participant Condition'], data['Alpha'])
sns.boxplot(i4, nf1)
plt.show()

#sns.set_style('whitegrid')
#sns.kdeplot(data['Beta'],  bw=0.5)
#plt.show()

#patient = data.loc[data['Participant Condition']=='Patient'].values
#control = data.loc[data['Participant Condition']=='Control'].values

#data_wide = data.pivot(columns='Participant Condition',
#                     values='Beta') #change back to beta

#data_wide.plot.density(figsize = (7, 7),
#                       linewidth = 4)
  
#plt.xlabel("Participant Condition")
#plt.show()



