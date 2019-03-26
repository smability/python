import csv
import matplotlib
import matplotlib.pyplot as plt
import time
import numpy as np
from datetime import datetime



#empty lists
timestamp0=[]
timestamp1=[]
time_data_hr=[]
time_data_date=[]

timeT=[]
timeR=[]
time24hr=[]

pm25=[]
pm10=[]
pm25_data=[]
pm10_data=[]


#AMEXCID_Merced_15Nov18_21Nov18.csv Not OK, missing data

#Period 1
#CasaClima_BJU_6Dic18_12Dic18.csv Not OK, data is missing
#CasaClima_BJU_10Dic18_16Dic18.csv Not OK, data is missing
#Period 2
#CasaClima_BJU_28Dic18_10Ene19.csv Not OK, data is missing

#CasaClima_BJU_19Nov18_25Nov18.csv OK

#Energia_BJU_17Dic18_23Dic18.csv OK
#Energia_BJU_31Dic18_6Ene19.csv OK

#Biodiversidad_CCA_14Ene19_20Ene19.csv OK
#Biodiversidad_CCA_21Ene19_27Ene19.csv OK
#AMEXCID_HG_15Nov18_21Nov18.csv OK
#AGM_BJU_3Dic18_9Dic18.csv OK, data is missing

with open('SEDEMA PM25/CasaClima_BJU_19Nov18_16Dic18.csv','r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')

    for row in reader:
        timestamp0.append(row[0])
        timestamp1.append(row[1])
        pm25.append(row[8])
        pm10.append(row[7])

csvFile.close()

#print pm25

#append data except the headers: 'hora' and 'pm25'
for i in range(1,len(pm25)):
    time_data_date.append(timestamp0[i])
    time_data_hr.append(timestamp1[i])
    pm25_data.append(pm25[i])
    pm10_data.append(pm10[i])

#convert string to int,
pm25_data = [int(i) for i in pm25_data]
pm10_data = [int(i) for i in pm10_data]
time_data_hr = [int(i)-1 for i in time_data_hr]

#print len(pm25_data)
#print len(pm10_data)
#correlation PM2.5 vs PM10
b = [25,35]
a = [42.5,59.5] 
#np.corrcoef(x, y)
print np.corrcoef(a, b)
#plt.scatter(x, y)
plt.scatter(a,b)
plt.show()
#seconds to hrs and time format in hrs
for j in range(0,len(timestamp1)-1):
    time24hr.append(time.strftime('%H:%M:%S', time.gmtime(time_data_hr[j]*3600)))
#time concatenation date+hr
for k in range(0,len(timestamp1)-1):
    timeT.append(time_data_date[k] +' '+ time24hr[k])
#time format in date+hrs
for l in range(0,len(timestamp1)-1):
        timeR.append(datetime.strptime(timeT[l],'%Y-%m-%d %H:%M:%S'))

plt.plot(timeR,pm25_data)
plt.plot(timeR,pm10_data)
plt.grid(True)
plt.show()
