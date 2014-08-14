# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 11:47:39 2014

@author: Kyle Goyette
"""

import visa

def connect2inst(to):
    
    global rm, devs, LCR
    rm = visa.ResourceManager()
    ii = 1
    for i in rm.list_resources():
        try: 
            idn = rm.get_instrument(rm.list_resources()[ii-1],timeout=0.01).ask('*idn?')
            idn = rm.get_instrument(rm.list_resources()[ii-1],timeout=0.01).ask('*idn?')
            print str(ii)+'.-'+idn.strip('\n')
        except:
            idn = 'Unknown device'
            print str(ii)+'.-'+idn+'\n'
        ii += 1
    r = True
    while r:
        try:
            device = raw_input('Select the instrument you want to control: ')
            device = int(device,base=10)-1
            devs = rm.list_resources()[device]
            r = False
        except:
            print 'INVALID INSTRUMENT'
    LCR = rm.get_instrument(devs, timeout=to)      #opens the instrument and assings it to class LCR
        
    LCR.write('*cls;:abor;:disp:ccl')
    print '\n%s\n' %LCR
        
    
    return LCR