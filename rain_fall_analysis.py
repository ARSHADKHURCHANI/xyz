import pandas as pd
df1=pd.read_csv("district.csv")
df2=pd.read_csv("india.csv")
print(df1)
print(df2)
# Q1" average, maximum, minimum rain fall
x_mean=df1.groupby("STATE_UT_NAME")["ANNUAL"].mean()
x_max=df1.groupby("STATE_UT_NAME")["ANNUAL"].max()
x_min=df1.groupby("STATE_UT_NAME")["ANNUAL"].min()
q1=pd.DataFrame([x_mean,x_max,x_min])
q2=q1.T


z=df1.columns
z=list(z)
for i in range(2,19):
    x_mean=df1.groupby("STATE_UT_NAME")[z[i]].mean()
    x_max=df1.groupby("STATE_UT_NAME")[z[i]].max()
    x_min=df1.groupby("STATE_UT_NAME")[z[i]].min()
    
    

import matplotlib.pyplot as plt
q2.plot(kind='line', color=['red','blue','brown'])
plt.grid()
plt.title("Rain fall Data Statewise")
plt.xlabel("Sate/UT Name")
plt.ylabel("Rain fall in mm")
plt.show()
import numpy as np
z=np.arange(1,36)
z1=pd.Series(z)
plt.plot(z1,x_mean)
plt.title("Average Rain Fall Statewise")
plt.xlabel("Sate/Ut row index")
plt.ylabel("rain fall in mm")
plt.grid()
plt.show()
# Barplot
q2.plot(kind='bar',color=['red','yellow','purple'],edgecolor='Green')
plt.title("Rain fall Data Statewise")
plt.xlabel("Sate/UT Name")
plt.ylabel("Rain fall in mm")
plt.grid()
plt.show()

#  Histogram:
q1.plot(kind='hist')
plt.show()

# Scatter plot
#q2.plot(kind="scatter",x=df2.JAN,y=df2.FEB)
#plt.show()

# box plot
q1.plot(kind="box")
plt.show()

# pie chart
x_mean.plot(kind='pie',y='JAN')
plt.show()

