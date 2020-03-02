import serial
import time

ser=serial.Serial("COM1",9600,timeout=5)
print("串口=%s，波特率=9600"%(ser.name))
string='[SENT %s]Hello World!\n'%(time.asctime(time.localtime(time.time())))
print(string)
ser.write(string.encode())
ser.close()
