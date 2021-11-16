#!/usr/bin/env python3
import sacn
import time
import numpy
import numberMatrices as mat
from datetime import datetime as dt
from pyowm import OWM

owm = OWM('YOUR_API_KEY')
mgr = owm.weather_manager()

obs = mgr.weather_at_place('Terre Haute,US')
w = obs.weather
print(w.temperature('fahrenheit'))
#print(w.status)
#print(w.rain)
temp = str(int(w.temperature('fahrenheit')["temp"]))


#print("TEMP: "+str(temp))
now = dt.now()
now = now.strftime("%H%M")
#print(now)
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

roseLogo = mat.roseLogo

pm = mat.pm
am = mat.am
matrix = blankPage

matrixToShow = [blankPage]
hourTens = int(now[0])
hourOnes = int(now[1])
minTens = int(now[2])
minOnes = int(now[3])



#matrix = hourColon
#matrix = oneHour
##print(matrix)

""" matrix = blankPage
for i in range(1,len(things)):
  matrix = numpy.bitwise_and(matrix,things[i]) """
oldtime = dt.now()
oldtime = oldtime.strftime("%H%M")
oldtime = int(oldtime)
checkTempThisHour = False
while(1):
  sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
  sender.start()  # start the sending thread
  tenTemp = int(str(temp[0]))
  oneTemp = int(str(temp[1]))
  print("TEMP: "+str(temp))
  now = dt.now()
  now = now.strftime("%H%M")
  nowstr = now
  now = int(now)
  print(now)
  if (now != oldtime):
    matrix = blankPage
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
    oldtime = now

  matrixToShow = [blankPage]
  hourTens = int(nowstr[0])
  hourOnes = int(nowstr[1])
  minTens = int(nowstr[2])
  minOnes = int(nowstr[3])
  
  

  if((hourTens ==  0  and hourOnes ==  0 ) or (hourTens == 1 and hourOnes == 2)):
  
    matrixToShow.append(tenHour)
    matrixToShow.append(twoHour)
  elif((hourTens ==  0  and hourOnes ==  1 ) or (hourTens == 1 and hourOnes == 3)):
    
    matrixToShow.append(oneHour)
  elif((hourTens ==  0  and hourOnes ==  2 ) or (hourTens == 1 and hourOnes == 4)):
    
    matrixToShow.append(twoHour)
  elif((hourTens ==  0  and hourOnes ==  3 ) or (hourTens == 1 and hourOnes == 5)):
  
    matrixToShow.append(threeHour)
  elif((hourTens ==  0  and hourOnes ==  4 ) or (hourTens == 1 and hourOnes == 6)):
    
    matrixToShow.append(fourHour)
  elif((hourTens ==  0  and hourOnes ==  5 ) or (hourTens == 1 and hourOnes == 7)):
    
    matrixToShow.append(fiveHour)
  elif((hourTens ==  0  and hourOnes ==  6 ) or (hourTens == 1 and hourOnes == 8)):
    
    matrixToShow.append(sixHour)
  elif((hourTens ==  0  and hourOnes ==  7 ) or (hourTens == 1 and hourOnes == 9)):
    
    matrixToShow.append(sevenHour) 
  elif((hourTens ==  0  and hourOnes ==  8 ) or (hourTens == 2 and hourOnes == 0)):
    
    matrixToShow.append(eightHour)
  elif((hourTens ==  0  and hourOnes ==  9 ) or (hourTens == 2 and hourOnes == 1)):
    
    matrixToShow.append(nineHour)
  elif((hourTens ==  1  and hourOnes ==  0 ) or (hourTens == 2 and hourOnes == 2)):
    
    matrixToShow.append(tenHour)
    matrixToShow.append(zeroHour)
  else:
    matrixToShow.append(tenHour)
    matrixToShow.append(oneHour)

  matrixToShow.append(hourColon)

  if(minTens == 0):
    matrixToShow.append(zeroTenMin)
  elif(minTens == 1):
    matrixToShow.append(oneTenMin)
  elif(minTens == 2):
    matrixToShow.append(twoTenMin)
  elif(minTens == 3):
    matrixToShow.append(threeTenMin)
  elif(minTens == 4):
    matrixToShow.append(fourTenMin)
  else:
    matrixToShow.append(fiveTenMin)

  if(minOnes == 0):
    matrixToShow.append(zeroMin)
  elif(minOnes == 1):
    matrixToShow.append(oneMin)
  elif(minOnes == 2):
    matrixToShow.append(twoMin)
  elif(minOnes == 3):
    matrixToShow.append(threeMin)
  elif(minOnes == 4):
    matrixToShow.append(fourMin)
  elif(minOnes == 5):
    matrixToShow.append(fiveMin)
  elif(minOnes == 6):
    matrixToShow.append(sixMin)
  elif(minOnes == 7):
    matrixToShow.append(sevenMin)
  elif(minOnes == 8):
    matrixToShow.append(eightMin)
  else:
    matrixToShow.append(nineMin)
  hours = (hourTens*10) + hourOnes
  mins = (minTens * 10) + minOnes
  if(hours >= 12):
    matrixToShow.append(pm)
  else:
    matrixToShow.append(am)
  #print(str(mins))
  #print(checkTempThisHour)
  if( mins == 0):
    if(checkTempThisHour == False):
      print("CHECK TEMP")
      obs = mgr.weather_at_place('Terre Haute,US')
      w = obs.weather
      
      temp = int(w.temperature('fahrenheit')["temp"])
      
      #print(temp)
      checkTempThisHour = True
  elif(mins == 59):
    #print("need to check temp")
    checkTempThisHour = False  

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

  matrixToShow.append(degSym)
  matrixToShow.append(fSym)
  matrixToShow.append(roseLogo)


  for i in range(1,len(matrixToShow)):
    matrix = numpy.bitwise_and(matrix,matrixToShow[i])


  for u in range(1,univ+1):
          sender.activate_output(u)  # start sending out data in the 1st universe
          sender[u].destination = "192.168.7.2"  # or provide unicast information
          row=[]
          for i in range(0,chan):
              #print("U: "+str(u)+" I: "+str(i))
              if(matrix[u][i] == 0):
                if(i < 10):
                  row.append(200)
                  row.append(200)
                  row.append(200)
                elif(i > 10 and u > 16 and u < 50):
                  if(int(temp) > 50):
                    row.append(0)
                    row.append(100)
                    row.append(0)
                  elif(int(temp) > 75):
                    row.append(100)
                    row.append(0)
                    row.append(0)
                  else:
                    row.append(0)
                    row.append(0)
                    row.append(255)
                else:
                  row.append(255)
                  row.append(0)
                  row.append(0)
              else:
                  row.append(0)
                  row.append(0)
                  row.append(0)

          rows[u-1] = row
          
          sender[u].dmx_data = rows[u-1]  # some test DMX data
          time.sleep(.01)
  #time.sleep(10)
  sender.stop()  # do not forget to stop the sender
