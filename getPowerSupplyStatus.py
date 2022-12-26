#!/usr/bin/env python

#simple script to print out BK power supply current/voltages
import araPowerSupply

ara_power = araPowerSupply.ARAPowerSupplies()

print
print '---------------'
print 'ARA ICL RACK 13 power supply status'
print '---------------'
print '* ARA1/4 supply', ara_power.ara1.identify()
print '* * VOLTAGE:', ara_power.ara1.getVoltageOutput()
print '* * CURRENT:', ara_power.ara1.getCurrentOutput()
print '---------------'
print '* ARA5 + PA supply', ara_power.ara5.identify()
print '* * VOLTAGE:', ara_power.ara5.getVoltageOutput()
print '* * CURRENT:', ara_power.ara5.getCurrentOutput()
print '* * STATUS:', ara_power.ara5.getStatus()
print '* * VSETTING:', ara_power.ara5.getVoltageSetting()
print '* * ISETTING:', ara_power.ara5.getCurrentSetting()
print '---------------'
print '* ARA2/3 supply', ara_power.ara3.identify()
print '* * VOLTAGE:', ara_power.ara3.getVoltageOutput()
print '* * CURRENT:', ara_power.ara3.getCurrentOutput()
print 

ara_power.closeConnections()
