import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParms['figure.figsize']=(12.0,9.0)

#preprocessing Input data
data = pd.read_csv('CasaClima_BJU_19Nov18_16Dic18 PM25PM10.csv')

X = data.iloc[:,0]#all the rows from the first column
Y = data.iloc[:,1]

plt.scatter(X,Y)
plt.show()

#building the model
X_mean = np.mean(X)
Y_mean = mp.mean(Y)

num = 0
den = 0

#simulate sigma function
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i]-Y_mean)
    den += (X[i]-X_mean)**2

m = num / den
c = Y_mean - m*X_mean

print (m,c) #subsitute the result in eq. y = mx+c

#making the predictions
Y_pred = m*X + c

#PM10_pred = m*PM25 + c

plt.scatter(X,Y)#actual
#plt.scatter(X,Y_pred, color='red')#predicted
plt.plot([min(X),max(X)],[min(Y_pred),max(Y_pred)],color='red')#regretion line
plot.show()
