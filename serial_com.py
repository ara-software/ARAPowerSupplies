# basic commands to serially control XLN60026 power supply in rack 13
# EJO : 2018-1-19
#
# to-do: more error handling
####################
import time
import serial

class SerialCom:
    
    def __init__(self, port):
        self.serdev = serial.Serial(port=port, 
                                    baudrate=57600,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    timeout=1
                                    )
        self.serdev.close()
        
    def openConnection(self):
        self.serdev.open()
        
    def closeConnection(self):
        self.serdev.close()

    def sendCommand(self, cmd, value=None):
        retstring=''
        if value == None:
            self.serdev.write(bytes(cmd+'\r\n'))
        else:
            self.serdev.write(bytes(cmd+str(value)+'\r\n'))
        time.sleep(0.1) #seems to be robust
        while self.serdev.inWaiting() > 0:
            retstring += self.serdev.read(1)
#            print (retstring)
        return retstring

    def identify(self):
        readback = self.sendCommand('*IDN?')
        return readback
    
    def getStatus(self):
        readback = self.sendCommand('STATUS?')
        return readback


    def getCurrentOutput(self):
        readback = self.sendCommand('IOUT?')
        try: 
            return float(readback)
        except: 
            return -1 

    def getCurrentSetting(self):
        readback = self.sendCommand('ISET?')
        return float(readback)

    def getVoltageOutput(self):
        readback = self.sendCommand('VOUT?')
        try:
             return float(readback)
        except: 
             return -1

    def getVoltageSetting(self):
        readback = self.sendCommand('VSET?')
        return float(readback)

    def setOutput(self, mode=0):
        '''
        mode=0, turn off; mode=1 turn on
        '''
        if mode==1:
            readback = self.sendCommand('OUT on')
            return readback
        elif mode==0:
            readback = self.sendCommand('OUT off')
            return readback
        else:
            print ('mode input not accepted')
            return

    def setVoltage(self, voltage):
        if voltage > 420:
            print ('voltage too high, probably, so will not program')
            return
        readback = self.sendCommand(cmd='VSET ', value=voltage)
        return readback

    def setCurrent(self, current):
        if current > 2.5:
            print ('exceeds current limit on supply, will not program')
            return
        readback = self.sendCommand(cmd='ISET ', value=current)
        return readback
        


