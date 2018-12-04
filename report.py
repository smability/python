import mysql.connector
import matplotlib
import matplotlib.pyplot as plt #import matplotlib library
import numpy as np #import numpy
import pandas as pd
#import folium
#import basemap
from datetime import datetime

#mysql connector
smability = mysql.connector.connect(user='', password='',
                                        host='',#cpanel host
                                        database='')
try:
    cursor = smability.cursor()
    #query = "SELECT readingtime, reading FROM temperature WHERE device_ID = 1"

    #location table contains timestamp,pm25,gps data
    #readingtime = timestamp
    #alarm = pm25
    #reading = gps

    query = "SELECT readingtime,reading FROM pm25 WHERE device_ID = 2 AND readingtime BETWEEN '2018-11-14' AND '2018-11-24' ORDER BY readingtime asc";
    cursor.execute(query)
    results = cursor.fetchall()#timestamp,pm25,gps stored in 3 rwos

    #print results[1]#print value of results[n]=timestamp,pm25,gps

except:
    print('Unable to perform query')

else:
    #list comprehension
    timestamp = [column[0] for column in results]#values column[0]=timestamp
    pm25 = [column[1] for column in results]#values column[1]=pm25
    #gpss = [column[2] for column in results]#values column[2]=gps

    #correction algorithm gps
    #for time in timestamp:
    #    print time

finally:
    smability.close()

#filter function

#avergae function

#exposure function


plt.plot(timestamp,pm25)
plt.grid()
plt.show()
