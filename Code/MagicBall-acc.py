import BMP085p3 as BMP085
import lsm_chp

lsm = lsm_chp.Adafruit_LSM303()
bmp = BMP085.BMP085()

acc = lsm.read()
a_x = acc[0][0] # accel readings
a_y = acc [0][1]
a_z = acc[0][2]
altitude = bmp.read_altitude()
temp = bmp.read_temperature()
pres = bmp.read_pressure()
print(altitude)
print(temp)
