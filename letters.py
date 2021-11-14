#!/usr/bin/env python3
import sacn
import time
import numpy
import numberMatrices as mat
from datetime import datetime as dt

sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
sender.start()  # start the sending thread
#sender.activate_output(1)
#sender[1].destination = "192.168.7.2"
univ = 64
chan = 32
row = []
rows = [row]*univ
matrix = mat.blankPage
zeroTenHour = mat.zeroHour
tenHour = mat.tenHour
zeroHour = mat.zeroHour
oneHour = mat.oneHour
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

things = [matrix,oneHour,hourColon,threeTenMin,threeMin]
#print(oneHour)
for i in range(1,len(things)):
  matrix = numpy.bitwise_and(matrix,things[i])



#matrix = hourColon
#matrix = oneHour
#print(matrix)
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
          time.sleep(.01)
sender.stop()  # do not forget to stop the sender
