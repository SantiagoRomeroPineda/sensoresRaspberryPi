import time
import smbus

i2c_ch = 1
i2c_address = 0x5A
bus = smbus.SMBus(i2c_ch)
while True:
    try:
        reading = bus.read_word_data(i2c_address, 0x07)
        temp = reading * .02 - 273.15
        print("temp: ", reading, temp)
    except IOError:
        pass
    finally:
        time.sleep(0.1)