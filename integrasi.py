import serial
import time

ser = serial.Serial("", 9600)
ser.flush()

try:
	while True:
		if ser.in_waiting > 0:
			data = ser.readline()
			print(data.decode())
			time.sleep(1)
except KeyboardInterrupt:
	ser.close()
finally:
	ser.close()
