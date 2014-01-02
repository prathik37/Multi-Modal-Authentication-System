
import time
import datetime
import bbio
import os
import sys
from bbio import *
from datetime import timedelta

# To properly clock LCD I had to use exotic microsecond range sleep function
usleep = lambda x: time.sleep(x/100000.0) # Can go higher, but will eat up whole CPU on that. 
# IOMAP = [RS, CLK(E), B7, B6, B5, B4]
iomap = [GPIO1_12, GPIO0_26, GPIO1_5, GPIO1_31, GPIO2_1, GPIO1_14]

ticks = time.time()
i = 0

# LCD instruction mode
# For some reason my LCD takes longer to ACK that mode, hence longer delays. 
def lcdcommand( str ):
  digitalWrite(iomap[1], 1)
  usleep(500)
  digitalWrite(iomap[0], 0)
  iteration = 0
  for idr in str:
      digitalWrite(iomap[iteration+2], int(idr))
      iteration = iteration + 1
      if iteration == 4:
        iteration = 0
        usleep(100)
        digitalWrite(iomap[1], LOW)
        usleep(100)
        digitalWrite(iomap[1], HIGH)
        usleep(500)
  return

# LCD Data mode
def lcdprint( str ):
  for char in str:
    # Binary character value
    bitmap = bin(ord(char))[2:].zfill(8)
    digitalWrite(iomap[1], 1)
    usleep(20)
    digitalWrite(iomap[0], 1)
    iteration = 0
    for idr in bitmap:
      digitalWrite(iomap[iteration+2], int(idr))
      iteration = iteration + 1
      if iteration == 4:
        iteration = 0
        usleep(20)
        digitalWrite(iomap[1], LOW)
        usleep(20)
        digitalWrite(iomap[1], HIGH)
        usleep(20)
  return

  # Create a setup function:
def setup():

  sys.stdout.write("Python HD44780 LCD Driver REV 2")
  sys.stdout.write('\n')

  # Set BITMAP of outputs: 
  pinMode(iomap[1], OUTPUT)
  pinMode(iomap[0], OUTPUT)
  
  pinMode(iomap[2], OUTPUT)
  pinMode(iomap[3], OUTPUT)
  pinMode(iomap[4], OUTPUT)
  pinMode(iomap[5], OUTPUT)

  sys.stdout.write("Setting Up Screen")
  sys.stdout.write('\n')

  # lcdcommand('00000001')
  
  lcdcommand('0011') # \
  lcdcommand('0011') # | Initialization Sequence
  lcdcommand('0011') # /
  lcdcommand('0010') # 4BIT Mode
  
  # lcdcommand('00001111')
  
  lcdcommand('00000001') # Reset
  lcdcommand('00001100') # Dispaly On
  
  #lcdcommand('11000000') # Shift to 2nd Line
  # Shift Reference
  #10000000  Moves cursor to first address on the left of LINE 1
  #11000000  Moves cursor to first address on the left of LINE 2
  #10010100  Moves cursor to first address on the left of LINE 3
  #11010100  Moves cursor to first address on the left of LINE 4
    
  sys.stdout.write("Transferring LCD Control to main loop")
  sys.stdout.write('\n')
  
  sys.stdout.write("Process PID: ")
  sys.stdout.write(str(os.getpid()))
  sys.stdout.write('\n')
    
# Create a main function:
##def loop():
##
##  #with open('/proc/uptime', 'r') as f:
##   # uptime_seconds = float(f.readline().split()[0])
##   # uptime_string = str(datetime.timedelta(seconds = uptime_seconds))
##
##    
## # pid = str(os.getpid())
##
## # ticker1 = str(datetime.timedelta(seconds=round(time.time() - ticks, 0)))
## # ticker2 =  pid + " : " + str(round(time.time() - ticks, 3))
##  # Debug Options
##  #ticker1 = "    " + str(s)
##  #ticker2 = "    " + str(datetime.timedelta(seconds=round(s, 0)))
##  #ticker2 = "    " + str(datetime.timedelta(seconds=round(time.time() - ticks, 0)))
##
##  lcdprint("MultiModal Authe")
##  #lcdprint(ticker1)
## # lcdprint("B-Bone Uptime")
##  lcdcommand('11000000')
##  #lcdprint(ticker2)
##  lcdprint("ntication System")
## # lcdprint(uptime_string)
##  lcdcommand('10000000')
##  usleep(10000)
##  #usleep(100)



setup()
os.system("aplay /home/ubuntu/FYPAudio_Guide/introduction.wav")
lcdcommand('00000001') #lcd clear screen
lcdcommand('10000000') #cursor position set to 1st line
lcdprint("M. A. S")
usleep(50000)
lcdcommand('11000000')
lcdprint("Welcome User")
usleep(250000)



#wait for button press

lcdcommand('00000001')
lcdcommand('10000000')
lcdprint("Face Recognition")
usleep(50000)



