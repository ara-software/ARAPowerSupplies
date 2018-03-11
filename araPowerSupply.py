#EJO, pole, 20-Jan 2018
##
import serial_com
import config

class ARAPowerSupplies:
    def __init__(self):
        self.openConnections()

    def openConnections(self):

        self.ara1 = serial_com.SerialCom(port='/dev/serial/by-id/'+config.ps_id['ARA1'])
        self.ara1.openConnection()
        
        self.ara2 = serial_com.SerialCom(port='/dev/serial/by-id/'+config.ps_id['ARA2'])
        self.ara2.openConnection()
        
        self.ara3 = serial_com.SerialCom(port='/dev/serial/by-id/'+config.ps_id['ARA3'])
        self.ara3.openConnection()

        return self.ara1,self.ara2,self.ara3

    def closeConnections(self):
        self.ara1.closeConnection()
        self.ara2.closeConnection()
        self.ara3.closeConnection()
