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

degSym = mat.degSym
fSym = mat.fSym
oneDeg = mat.oneDeg
twoDeg = mat.twoDeg
threeDeg = mat.threeDeg
fourDeg = mat.fourDeg
fiveDeg = mat.fiveDeg
sixDeg = mat.sixDeg
sevenDeg = mat.sevenDeg
eightDeg = mat.eightDeg
nineDeg = mat.nineDeg
zeroDeg = mat.zeroDeg
oneTenDeg = mat.oneTenDeg
twoTenDeg = mat.twoTenDeg
threeTenDeg = mat.threeTenDeg
fourTenDeg = mat.fourTenDeg
fiveTenDeg = mat.fiveTenDeg
sixTenDeg = mat.sixTenDeg
sevenTenDeg = mat.sevenTenDeg
eightTenDeg = mat.eightTenDeg
nineTenDeg = mat.nineTenDeg

pm = mat.pm
am = mat.am
matrix = blankPage

matrixToShow = [blankPage,hourColon,tenHour,twoHour,twoTenMin,oneMin,pm,degSym,fSym]

temp = "36"
tenTemp = int(temp[0])
oneTemp = int(temp[1])

if(tenTemp == 1):
    matrixToShow.append(oneTenDeg)
elif(tenTemp == 2):
    matrixToShow.append(twoTenDeg)
elif(tenTemp == 3):
    matrixToShow.append(threeTenDeg)
elif(tenTemp == 4):
    matrixToShow.append(fourTenDeg)
elif(tenTemp == 5):
    matrixToShow.append(fiveTenDeg)
elif(tenTemp == 6):
    matrixToShow.append(sixTenDeg)
elif(tenTemp == 7):
    matrixToShow.append(sevenTenDeg)
elif(tenTemp == 8):
    matrixToShow.append(eightTenDeg)
elif(tenTemp == 9):
    matrixToShow.append(nineTenDeg)

if(oneTemp == 1):
    matrixToShow.append(oneDeg)
elif(oneTemp == 2):
    matrixToShow.append(twoDeg)
elif(oneTemp == 3):
    matrixToShow.append(threeDeg)
elif(oneTemp == 4):
    matrixToShow.append(fourDeg)
elif(oneTemp == 5):
    matrixToShow.append(fiveDeg)
elif(oneTemp == 6):
    matrixToShow.append(sixDeg)
elif(oneTemp == 7):
    matrixToShow.append(sevenDeg)
elif(oneTemp == 8):
    matrixToShow.append(eightDeg)
elif(oneTemp == 9):
    matrixToShow.append(nineDeg)



for i in range(1,len(matrixToShow)):
  matrix = numpy.bitwise_and(matrix,matrixToShow[i])

 

#while(1):
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
time.sleep(1)
sender.stop()  # do not forget to stop the sender