import serial
import time

baud=48
ser=serial.Serial("COM2",baud,timeout=5)
print("串口=%s，波特率=%d"%(ser.name,baud))
print("RECV from COM2: "+ser.readline().decode())
ser.close()
