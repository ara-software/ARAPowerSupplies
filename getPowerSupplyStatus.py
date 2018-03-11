#!/usr/bin/env python

#simple script to print out BK power supply current/voltages
import araPowerSupply

ara_power = araPowerSupply.ARAPowerSupplies()

print
print '---------------'
print 'ARA ICL RACK 13 power supply status'
print '---------------'
print '* ARA1/4 supply'
print '* * VOLTAGE:', ara_power.ara1.getVoltageOutput()
print '* * CURRENT:', ara_power.ara1.getCurrentOutput()
print '---------------'
print '* ARA2/5 supply'
print '* * VOLTAGE:', ara_power.ara2.getVoltageOutput()
print '* * CURRENT:', ara_power.ara2.getCurrentOutput()
print '---------------'
print '* ARA3 supply'
print '* * VOLTAGE:', ara_power.ara3.getVoltageOutput()
print '* * CURRENT:', ara_power.ara3.getCurrentOutput()
print 

ara_power.closeConnections()
