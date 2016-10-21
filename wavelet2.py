import pandas as pd
import numpy as np
import math
import datetime as dt
import matplotlib.pyplot as plt
import htalib
import hfalib
import pywt
import htalib

#prepare the price time serie
position=1
nav=[1]
hs300data=pd.read_csv("/Users/Howard/Documents/zendai/14to16/hs300wt.csv",parse_dates=['date'])
hs300=hs300data['close'].tolist()
t=range(500,len(hs300))
n=1
for i in t:
    tmp=((hs300[i]/hs300[i-1]-1)*position+1)*nav[-1]
    nav.append(tmp)
    x=hs300[0:i]
    [a,d]=htalib.wta(serie=x)
    if a[-1]-a[-2]>0:
        position=-1
    elif a[-1]-a[-2]<0:
        position=+1
    else:
        position=0
days=range(1,len(nav)+1)
plt.figure()
plt.plot(days,nav,'r-',label='nav')
plt.legend()
plt.show()



'''
#wavelet transfer
[cA5, cD3, cD2, cD1] = pywt.wavedec(x, 'dmey',mode='sp1',level=3)
#remove the high frequency wave
rcA5=np.zeros(len(cA5))
#rcD5=np.zeros(len(cD5))
#rcD4=np.zeros(len(cD4))
rcD3=np.zeros(len(cD3))
rcD2=np.zeros(len(cD2))
rcD1=np.zeros(len(cD1))
#print cA5
#re-build the coeffs
l_coeffs=[cA5,  rcD3, rcD2, rcD1]
h_coeffs=[rcA5, cD3, rcD2, rcD1]
#recover the low frequency wave time serie
l_y=pywt.waverec(l_coeffs, 'dmey')
h_y=pywt.waverec(h_coeffs, 'dmey')
t=range(1,len(x)+1)
#check the length
print len(x)
print len(l_y)
print len(h_y)
print len(t)
#compute the MA time serie
ma5=htalib.MA(x,5)
ma10=htalib.MA(x,10)
ma20=htalib.MA(x,20)
ma30=htalib.MA(x,30)
ma60=htalib.MA(x,60)
#plot for comparision
plt.figure(figsize=(16,8))
p1=plt.subplot(411)
p1.plot(t,x,'r-',label='original')
p1.legend(loc=4)
p4=plt.subplot(412)
p4.plot(t,data_po,'r-',label='oo_original')
p4.legend(loc=4)
p2=plt.subplot(413)
p2.plot(t,l_y,'b-',label='low_freq')
p2.legend(loc=4)
p3=plt.subplot(414)
p3.plot(t,h_y,'c-',label='high_freq')
p3.legend(loc=4)
#plt.plot(t,ma5,'g-',label='ma5')
#plt.plot(t,ma10,'k-',label='ma10')
#plt.plot(t,ma30,'c-',label='ma30')
#plt.plot(t,ma60,'y-',label='ma60')
plt.show()
'''