#!/usr/bin/env python3
import sacn
import time
import numpy
import numberMatrices as mat
from datetime import datetime as dt
from pyowm import OWM


now = dt.now()
now = now.strftime("%H%M")
print(now)
nowstr = str(now)


sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
sender.start()  # start the sending thread
#sender.activate_output(1)
#sender[1].destination = "192.168.7.2"
univ = 64
chan = 32
row = []

rows = [row]*univ
blankPage = mat.blankPage
zeroTenHour = mat.zeroHour
tenHour = mat.tenHour
zeroHour = mat.zeroHour
oneHour = mat.oneHour
twoHour = mat.twoHour
threeHour = mat.threeHour
fourHour = mat.fourHour
fiveHour = mat.fiveHour
sixHour = mat.sixHour
sevenHour = mat.sevenHour
eightHour = mat.eightHour
nineHour = mat.nineHour
hourColon = mat.hourColon
oneTenMin = mat.oneTenMin
twoTenMin = mat.twoTenMin
threeTenMin = mat.threeTenMin
fourTenMin = mat.fourTenMin
fiveTenMin = mat.fiveTenMin
zeroTenMin = mat.zeroTenMin
oneMin = mat.oneMin
twoMin = mat.twoMin
threeMin = mat.threeMin
fourMin = mat.fourMin
fiveMin = mat.fiveMin
sixMin = mat.sixMin
sevenMin = mat.sevenMin
eightMin = mat.eightMin
nineMin = mat.nineMin
zeroMin = mat.zeroMin

pm = mat.pm
am = mat.am
matrix = blankPage
matrixToShow = [blankPage,hourColon,tenHour,twoHour,twoTenMin,oneMin,pm]
for i in range(1,len(matrixToShow)):
  matrix = numpy.bitwise_and(matrix,matrixToShow[i])

 

while(1):
    for u in range(1,univ+1):
            sender.activate_output(u)  # start sending out data in the 1st universe
            sender[u].destination = "192.168.7.2"  # or provide unicast information
            row=[]
            for i in range(0,chan):
                #print("U: "+str(u)+" I: "+str(i))
                if(matrix[u][i] == 0):

                    row.append(0)
                    row.append(0)
                    row.append(255)
                else:
                    row.append(0)
                    row.append(0)
                    row.append(0)

            rows[u-1] = row
            
            sender[u].dmx_data = rows[u-1]  # some test DMX data
            time.sleep(.001)
    time.sleep(10)
sender.stop()  # do not forget to stop the sender