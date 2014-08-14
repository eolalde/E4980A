# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 15:16:20 2014

@author: Kyle Goyette
"""

import config, init, numpy

global LCR, lowlim, uplim, bandsize, e_level, d_level, acl, frequency, freqstr

LCR = init.connect2inst(5)      #Initializes the instrument and sets a timeout of 5 seconds

lowlim = 40.0         #Lower Frequency Limit in FreqSweep
uplim = 80.0          #Upper Frequency Limit in FreqSweep
bandsize = 21       #Number of Steps in FreqSweep
e_level = 25.0        #miliAmperes
d_level = 10.0        #Volts
frequency = 40.0      #Frequency for singlefreq measurements
acl = 0               #Automatic Level Contro tries to mantain the specified signal level across the DUT
j = 1
freqstr = ' '
sweepfreq = []
freqlist = numpy.linspace(lowlim,uplim,bandsize)


for j,i in enumerate(freqlist):
    if j < (bandsize-1):
        freqstr = freqstr + str(i) + ','
    else:
        freqstr = freqstr + str(i)
    sweepfreq.append(freqlist[j])


def run_single():
    result = []
    print '1.-Element\n2.-Dielectric\n'
    meas = raw_input('What is the type of DUT to measure?: ')
    r = True
    while r:
        if meas == '1':
            config.element_singlefreq(LCR,frequency,e_level,acl)
            r = False
        elif meas == '2':
            config.dielectric_singlefreq(LCR,frequency,d_level,acl)
            r = False
        elif meas not in [1,2]:
            meas = raw_input('Please select a valid measurement option: ')
            
    
    i = 5
    
    LCR.write(':abor')
    LCR.write(':init:cont 0')
    LCR.write(':trig:sour bus')
    LCR.write(':stat:oper:enab 16')
    LCR.write('*sre 128')
    
    while i:
        j = True
        LCR.write(':trig:imm')
        while j:
            stb = LCR.ask_for_values('*stb?')
            if stb[0] == 192:
                j = False
        
        res = LCR.ask_for_values(':fetch?')
        print res
        result.append(res)
        i -= 1
    
    return result

def run_sweep():
    result = []
    print '1.-Element\n2.-Dielectric\n'
    meas = raw_input('What is the type of DUT to measure?: ')
    r = True
    while r:
        if meas == '1':
            config.element_freqsweep(LCR,lowlim,uplim,bandsize,e_level,acl,freqstr)
            r = False
        elif meas == '2':
            config.dielectric_freqsweep(LCR,lowlim,uplim,bandsize,d_level,acl,freqstr)
            r = False
        else:
            meas = raw_input('Please select a valid measurement option: ')    
    
    i = bandsize
    
    LCR.write(':abor')
    LCR.write(':init:cont 0')
    LCR.write(':trig:sour bus')
    LCR.write(':stat:oper:enab 16')
    LCR.write('*sre 128')

    ii = 0
    while i:
        j = True
        LCR.write(':trig:imm')
        while j:
            stb = LCR.ask_for_values(':stat:oper:cond?')
            if stb[0] == 0:
                j = False
        
        res = [sweepfreq[ii]]
        res = res + LCR.ask_for_values(':fetch?')[:3]
        print res
        result.append(res)
        i -= 1
        ii +=1
    
    return result