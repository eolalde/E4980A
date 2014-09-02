# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 15:16:20 2014

@author: Eusebio OLG
"""

#import config, init, numpy

global LCR, lowlim, uplim, bandsize, e_level, d_level, acl, frequency, freqstr


def run_single(LCR, i, freq):

    result = []
    
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
        
        res = [freq]
        res = res + LCR.ask_for_values(':fetch?')
        #print res
        result.append(res)
        i -= 1
    
    return result

def run_sweep(LCR, i, sweepfreq):

    result = []
    
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
        #print res
        result.append(res)
        i -= 1
        ii +=1
    
    return result