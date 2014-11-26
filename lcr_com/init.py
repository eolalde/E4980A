# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 11:47:39 2014

@author: Eusebio OLG
"""

import visa

def connect2inst(to):
    
    global rm, devs, LCR
    rm = visa.ResourceManager()

    #devs = rm.list_resources()[0]
    #LCR = rm.get_instrument(devs, timeout=to)      #opens the instrument and assings it to class LCR
    LCR = rm.get_instrument('TCPIP0::192.168.185.127::inst0::INSTR')    
    
    LCR.write('*cls;:abor;:disp:ccl')

    return LCR