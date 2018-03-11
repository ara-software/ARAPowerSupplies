import time
import serial

LF = 0x0A
CR = 0x0D

dev=serial.Serial(
    port='/dev/ttyUSB1',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)


dev.close()
dev.open()
dev.isOpen()

input=1
while 1:
    input = raw_input(">>")
    if input == 'exit':
        dev.close()
        exit()
    else:
        out = ''
        dev.write(input+'\r\n')
        time.sleep(0.1)
        while dev.inWaiting() > 0:
            out += dev.read(1)
        if out != '':
            print ">>" + out

    '''
    dev.flushInput()
    dev.flushOutput()
    dev.write('VOLTage?' + '\r\n')
    dev.flush()
    
    out=None
    while True:
        resp=''
        while True:
            char = dev.read()
            print len(char)
            resp += char
            if char == '\r':
                break

            if resp == 'OK\r':
                print out

            out = resp
    '''
    #dev.write(input)
    

'''
import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB1',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.open()
ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
exit()
else:
    # send the character to the device
    # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
    ser.write(input + '\r\n')
out = ''
# let's wait one second before reading output (let's give device time to answer)
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
    
if out != '':
    print ">>" + out
'''
