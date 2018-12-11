#average filter algorithm 3.Dic.2018
import matplotlib.pyplot as plt

pm25 =[3,5,4,5,6,6,5,3,4,4]

def avgSig(sig,leng,ns):
    #pm25Avg array
    SigAvg =[]
    #range definition from 0 to 5, j=sample
    i=0
    ran = int(ns) #number of sample
    j=ran

    while(j<=leng): #why <=len?
        #reset 'sum' every loop iteration
        sum = 0.0
        k=i
        for i in range(i,j): #range definition 0 to 5, 5 to 9; if i is removed, range is 0 to 5 then 0 to 9
            sum = float(sum + sig[i])
        #average
        avg = sum/ns
        #fill in pm25Avg array; filtered signal
        for k in range(k,j):
            SigAvg.append(avg)
        i=j
        j+=ran
    #length of SigAvg
    lengthAvg = len(SigAvg)

    #resize SigAvg if needed
    if length == lengthAvg:
        pass
    else:
        #length difference between the two list
        diff = length - lengthAvg
        #append array length difference, with the last SignalAvg number, to SignalAvg
        last = SigAvg[-1] #last list number
        for l in range(diff): #l = 0; from 0 to diff
            SigAvg.append(last)

    return SigAvg


#array length
length = len(pm25)
#number of samples
numsample = length-7
#Signal Average array
SignalAvg = []
SignalAvg2 = []

#function avgSig() call
SignalAvg = avgSig(pm25,length,4)

SignalAvg2 = avgSig(SignalAvg,length,10)

print pm25
print SignalAvg
print SignalAvg2

#display raw PM2.5 and filtered PM2.5
plt.plot(pm25)
plt.plot(SignalAvg)
plt.plot(SignalAvg2)
plt.grid(True)
plt.show()
