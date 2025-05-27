import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from plotly.subplots import make_subplots as ms
import numpy as np
import plotly.express as ex


A = sns.load_dataset('tips')

#cleaning the database
print(A.isnull().sum())
A = A.dropna()
print(A.isnull().sum())


#make the text as capital
 
A['sex'] = A['sex'].str.strip().str.title()
A['smoker'] = A['smoker'].str.strip().str.title()
A['day'] = A['day'].str.strip().str.title()
A['time'] = A['time'].str.strip().str.title()

print(A.head())

#showing the max of the bill
Max_bill = A['total_bill'].max()
print(f'The max amount of the bill is {Max_bill}')

#showing the min of the bill

Min_bill = A['total_bill'].min()

print(f'The min amount of the bill is {Min_bill}')

#visualing the amount using by chart

sns.boxplot(data=A,x='sex',y='total_bill')

plt.show()

#visualing the amount using scatter plot and also color by smoker

X = 'total_bill'
Y = 'tip'

sns.scatterplot(data=A ,x=A[X],y=A[Y],hue='smoker')

plt.show()

#visualing the average tip by sex using bar chart

plt.bar(A['total_bill'],A['tip'])

plt.show()

#visulaing the tips using the violin chart

sns.violinplot(data=A,x='day',y='total_bill')
plt.ylabel('tips given by the customer')
plt.show()

