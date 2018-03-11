#!/usr/bin/env python

#UNTESTED AS OF 20 Jan 2018
import time
import araPowerSupply
import sys
#from optparse import OptionParser

accepted_args = ['ara1', 'ara2', 'ara3', 'all']

if __name__=='__main__':
    #usage = "usage : %prog [options]"
    #parser = OptionParser(usage)

    if len(sys.argv) != 2:
        print 'usage : program requires one argument:' 
        print 'specify PS by adding argument \'ara1\', \'ara2\',\'ara3\','
        print 'or \'all\' if you want to power up all of them'
        sys.exit()
    
    #dumb way to check if argument is in accepted list
    good_arg=False
    for arg in accepted_args:
        if sys.argv[1] == arg:
            good_arg=True
            break;

    if good_arg == False:
        print 'argument not accepted'
        print 'accepted program arguments are', accepted_args
        sys.exit()
       
    print 'proceeding...'
    
    ara_power = araPowerSupply.ARAPowerSupplies()
    
    if sys.argv[1] == 'ara1' or sys.argv[1] == 'all':
        print 'turning on ARA1/4 supply...'
        ara_power.ara1.setOutput(mode=1)
        time.sleep(1)
    if sys.argv[1] == 'ara2' or sys.argv[1] == 'all': 
        print 'turning on ARA2/5 supply...'
        ara_power.ara2.setOutput(mode=1)
        time.sleep(1)
    if sys.argv[1] == 'ara3' or sys.argv[1] == 'all':
        print 'turning on ARA3 supply...'
        ara_power.ara3.setOutput(mode=1)
        time.sleep(1)
    
    print '**'
    print 'check status by running ./getPowerSupplyStatus.py'

    ara_power.closeConnections()
    
