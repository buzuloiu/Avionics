from collections import namedtuple
import threading
from Adafruit_I2C import Adafruit_I2C
import rocket_state
#import Adafruit_BBIO.UART as UART
import serial
i2c = Adafruit_I2C(0x53)
#we have a device on 0x53 and 0x68

print "start"

#set up sensor pins to be read
#UART.setup("UART1") #gps
#UART.setup("UART2") #accelerometer
#UART.setup("UART4") #pressure data
#def init(subscriber):
#    publisher = sensor_observer.publisher()
#    publisher.register(subscriber)
#publisher = sensor_observer.publisher()
#publisher.register(subscriber)


    #transmit data asynchronously to application after putting it in standard format
def poll_sensors():
    accel=get_accel() #get accelerometer data
    gps=get_gps()   #get gps data
    baro=get_baro()  #get pressure data
    state= rocket_state.parse(accel,gps,baro)
    #publisher.dispatch(state)
    return state

def get_gps():
    return 1#poll gps and return gps data

def get_accel():
    return i2c.readS16()#return
    #poll accelerometer and return acceleration value

def get_baro():
    return 4    #poll barometer and return pressure data



if __name__ == '__main__':
    poll_sensors()