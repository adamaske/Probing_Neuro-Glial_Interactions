
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

def write_read(x):
    
    arduino.write(bytes(x, 'utf-8'))
    
    time.sleep(0.05)
    
    data = arduino.readline()
    
    return data

def write_serial(x) -> (int|None):
    result = arduino.write(bytes(x, 'utf-8'))
    return result

if __name__ == "__main__":
    # platform controller
    
    # what can it do ? 
    
    # 1. Tell the motor how to turn -> adjust the position of the wedge
    # and adjusts the angle of the stepping platform
    
    # 2. Inspect and validate the data from the gyroscope and accelerometer
    
    # 3. Launch the pnematic system
    
    
    write_serial("SM:34")
    
    
