#!/usr/bin/env python

#UNTESTED AS OF 20 Jan 2018
import time
import araPowerSupply
import sys
#from optparse import OptionParser

accepted_args = ['ara1', 'ara5', 'ara3', 'all']

if __name__=='__main__':
    #usage = "usage : %prog [options]"
    #parser = OptionParser(usage)

    if len(sys.argv) != 3:
        print 'usage : program requires two argument, the supply and the voltage:' 
        print 'specify PS by adding argument \'ara1\', \'ara5\',\'ara3\','
        print 'or \'all\' if you want to power up all of them'
	print 'example: ./setSupplyVoltage.py ara5 375'
        sys.exit()
    
    #dumb way to check if argument is in accepted list
    good_arg=False
    for arg in accepted_args:
        if sys.argv[1] == arg:
            good_arg=True
            break;

    if good_arg == False:
        print 'argument not accepted'
        print 'accepted program first arguments are', accepted_args
        sys.exit()
       
    print 'proceeding...'

    voltage = float(sys.argv[2]) 
    if (voltage < 0 or voltage > 420):
	print 'voltage out of range [0,420)'
	sys.exit()
    
    ara_power = araPowerSupply.ARAPowerSupplies()
    
    if sys.argv[1] == 'ara1' or sys.argv[1] == 'all':
        print 'setting voltage on ARA1/4 supply... to %g' % (voltage)
        ara_power.ara1.setVoltage(voltage)
        time.sleep(1)
    if sys.argv[1] == 'ara5' or sys.argv[1] == 'all': 
        print 'setting voltage on ARA5 supply... to %g' % (voltage)
        ara_power.ara5.setVoltage(voltage)
        time.sleep(1)
    if sys.argv[1] == 'ara3' or sys.argv[1] == 'all':
        print 'setting voltage on ARA2/3 supply... to %g' % (voltage)
        ara_power.ara3.setVoltage(voltage)
        time.sleep(1)
    
    print '**'
    print 'check status by running ./getPowerSupplyStatus.py'

    ara_power.closeConnections()
    
