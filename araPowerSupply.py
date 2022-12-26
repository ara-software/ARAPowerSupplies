#EJO, pole, 20-Jan 2018
#
# updated 11/24/2018 - ara5 supply isolated (ara5 + PA only). ara3 supply includes ara2 + 3
##
import serial_com
import config

class ARAPowerSupplies:
    def __init__(self):
        self.openConnections()

    def openConnections(self):

        self.ara1 = serial_com.SerialCom(port='/dev/serial/by-id/'+config.ps_id['ARA1'])
        self.ara1.openConnection()
        
        self.ara5 = serial_com.SerialCom(port='/dev/serial/by-id/'+config.ps_id['ARA5'])
        self.ara5.openConnection()
        
        self.ara3 = serial_com.SerialCom(port='/dev/serial/by-id/'+config.ps_id['ARA3'])
        self.ara3.openConnection()

        return self.ara1,self.ara5,self.ara3

    def closeConnections(self):
        self.ara1.closeConnection()
        self.ara5.closeConnection()
        self.ara3.closeConnection()
