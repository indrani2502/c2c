import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import socket
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO
TRIG2 = 27                                 #Associate pin 5 to TRIG
ECHO2 = 22                                  #Associate pin 6 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(TRIG2,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO2,GPIO.IN)                   #Set pin as GPIO in

s = socket.socket()
host = '192.168.43.234'
port = 12345
s.bind((host, port))

s.listen(5)

while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print "Waitng For Sensor 1 To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG2, False)                 #Set TRIG2 as LOW
  print "Waing For Sensor 2To Settle"
  time.sleep(2)                            #Delay of 2 seconds
  
  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  
  GPIO.output(TRIG2, True)                  #Set TRIG2 as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG2, False)                 #Set TRIG2 as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse
  while GPIO.input(ECHO2)==0:               #Check whether the ECHO2 is LOW
    pulse_start2 = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse
    
  while GPIO.input(ECHO2)==1:               #Check whether the ECHO2 is HIGH
    pulse_end2 = time.time()                #Saves the last known time of HIGH pulse   

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
  pulse_duration2 = pulse_end2 - pulse_start2 #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points
  distance2 = pulse_duration2 * 17150        #Multiply pulse duration by 17150 to get distance
  distance2 = round(distance2, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
  else:
    print "Out Of Range1"                   #display out of range
    
  
  if distance2 > 2 and distance2 < 400:      #Check whether the distance is within range
    print "Distance2:",distance2 - 0.5,"cm"  #Print distance with 0.5 cm calibration
  else:
    print "Out Of Range2"                   #display out of range
  
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send(Distance,Distance2)
  
  c.close()  