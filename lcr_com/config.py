# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 15:10:30 2014

@author: Eusebio OLG
"""

import numpy

def element_singlefreq(LCR,freq,level,acl,function):
    LCR.write('''\
    :SOUR:DCS:STAT OFF;\
    :BIAS:STAT OFF;\
    :COMP:BIN:COUN:CLE;\
    :LIST:CLE:ALL;\
    :COMP:BIN:CLE;\
    \
    :AMPL:ALC %d;\
    \
    :APER MED,6;\
    :BIAS:POL:AUTO ON;\
    :BIAS:RANG:AUTO ON;\
    :BIAS:VOLT:LEV 0;\
    :COMP:ABIN OFF;\
    :COMP:BIN:COUN:STAT OFF;\
    :COMP:MODE ATOL;\
    :COMP:SLIM -9.9e+37,9.9e+37;\
    :COMP:STAT OFF;\
    :COMP:SWAP OFF;\
    :COMP:TOL:NOM 0;\
    \
    :CURR:LEV %f;\
    \
    :DISP:ENAB ON;\
    :DISP:LINE "TCX;60";\
    :DISP:WIND:TEXT1:DATA:FMSD:DATA 1e-09;\
    :DISP:WIND:TEXT2:DATA:FMSD:DATA 1e-09;\
    :FORM:ASC:LONG OFF;\
    :FORM:BORD NORM;\
    :FORM:DATA ASC,64;\
    \
    :FREQ:CW %f;\
    \
    :FUNC:DCR:RANG:VAL 100;\
    :FUNC:DEV1:MODE OFF;\
    :FUNC:DEV1:REF:VAL 0;\
    :FUNC:DEV2:MODE OFF;\
    :FUNC:DEV2:REF:VAL 0;\
    :FUNC:IMP:RANG:VAL 10;\
    \
    :FUNC:IMP:TYPE %s;\
    \
    :FUNC:SMON:IDC:STAT OFF;\
    :FUNC:SMON:VDC:STAT OFF;\
    :INIT:CONT OFF;\
    :LIST:MODE SEQ;\
    :LIST:STIM:TYPE FREQ,NONE;\
    :OUTP:DC:ISOL:LEV:VAL 0.1;\
    :OUTP:DC:ISOL:STAT OFF;\
    :SOUR:DCS:VOLT:LEV 0;\
    :TRIG:DEL 0;\
    :TRIG:SOUR INT;\
    :TRIG:TDEL 0;\
    :DISP:WIND:TEXT1:DATA:FMSD:STAT OFF;\
    :DISP:WIND:TEXT2:DATA:FMSD:STAT OFF;\
    :FUNC:DCR:RANG:AUTO ON;\
    :FUNC:IMP:RANG:AUTO ON;\
    :OUTP:DC:ISOL:LEV:AUTO ON;\
    :DISP:PAGE MEASurement;''' %(acl, level/1000.0 ,freq, function))

    return LCR


    
def dielectric_singlefreq(LCR,freq,level,acl,function):
    LCR.write(''':SOUR:DCS:STAT OFF;\
    :BIAS:STAT OFF;\
    :COMP:BIN:COUN:CLE;\
    :LIST:CLE:ALL;\
    :COMP:BIN:CLE;\
    \
    :AMPL:ALC %d;\
    \
    :APER MED,6;\
    :BIAS:POL:AUTO ON;\
    :BIAS:RANG:AUTO ON;\
    :BIAS:VOLT:LEV 0;\
    :COMP:ABIN OFF;\
    :COMP:BIN:COUN:STAT OFF;\
    :COMP:MODE ATOL;\
    :COMP:SLIM -9.9e+37,9.9e+37;\
    :COMP:STAT OFF;\
    :COMP:SWAP OFF;\
    :COMP:TOL:NOM 0;\
    :DISP:ENAB ON;\
    :DISP:LINE "TCX;60";\
    :DISP:WIND:TEXT1:DATA:FMSD:DATA 1e-09;\
    :DISP:WIND:TEXT2:DATA:FMSD:DATA 1e-09;\
    :FORM:ASC:LONG OFF;\
    :FORM:BORD NORM;\
    :FORM:DATA ASC,64;\
    \
    :FREQ:CW %f;\
    \
    :FUNC:DCR:RANG:VAL 100;\
    :FUNC:DEV1:MODE OFF;\
    :FUNC:DEV1:REF:VAL 0;\
    :FUNC:DEV2:MODE OFF;\
    :FUNC:DEV2:REF:VAL 0;\
    :FUNC:IMP:RANG:VAL 10;\
    \
    :FUNC:IMP:TYPE %s;\
    \
    :FUNC:SMON:IDC:STAT OFF;\
    :FUNC:SMON:VDC:STAT OFF;\
    :INIT:CONT OFF;\
    :LIST:MODE SEQ;\
    :LIST:STIM:TYPE FREQ,NONE;\
    :OUTP:DC:ISOL:LEV:VAL 0.1;\
    :OUTP:DC:ISOL:STAT OFF;\
    :SOUR:DCS:VOLT:LEV 0;\
    :TRIG:DEL 0;\
    :TRIG:SOUR INT;\
    :TRIG:TDEL 0;\
    \
    :VOLT:LEV %f;\
    \
    :DISP:WIND:TEXT1:DATA:FMSD:STAT OFF;\
    :DISP:WIND:TEXT2:DATA:FMSD:STAT OFF;\
    :FUNC:DCR:RANG:AUTO ON;\
    :FUNC:IMP:RANG:AUTO ON;\
    :OUTP:DC:ISOL:LEV:AUTO ON;\
    :DISP:PAGE MEASurement;''' %(acl, freq, function, level))

    return LCR
    

def element_freqsweep(LCR,lowlim,uplim,bandsize,level,acl,function):
    
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
    
    LCR.write('''\
    :DISP:CCL;\
    :SOUR:DCS:STAT OFF;\
    :BIAS:STAT OFF;\
    :COMP:BIN:COUN:CLE;\
    :LIST:CLE:ALL;\
    :COMP:BIN:CLE;\
    \
    :AMPL:ALC %d;\
    \
    :APER SHOR,1;\
    :BIAS:POL:AUTO ON;\
    :BIAS:RANG:AUTO ON;\
    :BIAS:VOLT:LEV 0;\
    :COMP:ABIN OFF;\
    :COMP:BIN:COUN:STAT OFF;\
    :COMP:MODE ATOL;\
    :COMP:SLIM -9.9e+37,9.9e+37;\
    :COMP:STAT OFF;\
    :COMP:SWAP OFF;\
    :COMP:TOL:NOM 0;\
    \
    :CURR:LEV %f;\
    \
    :DISP:ENAB ON;\
    :DISP:LINE "TCX: EL_SWEEP";\
    :DISP:WIND:TEXT1:DATA:FMSD:DATA 1e-09;\
    :DISP:WIND:TEXT2:DATA:FMSD:DATA 1e-09;\
    :FORM:ASC:LONG OFF;\
    :FORM:BORD NORM;\
    :FORM:DATA ASC,64;\
    :FUNC:DCR:RANG:VAL 100;\
    :FUNC:DEV1:MODE OFF;\
    :FUNC:DEV1:REF:VAL 0;\
    :FUNC:DEV2:MODE OFF;\
    :FUNC:DEV2:REF:VAL 0;\
    :FUNC:IMP:RANG:VAL 10;\
    \
    :FUNC:IMP:TYPE %s;\
    \
    :FUNC:SMON:IDC:STAT OFF;\
    :FUNC:SMON:VDC:STAT OFF;\
    :INIT:CONT OFF;\
    :LIST:CLE:ALL;\
    :LIST:MODE STEP;\
    :LIST:STIM:TYPE FREQ,NONE;\
    :OUTP:DC:ISOL:LEV:VAL 0.1;\
    :OUTP:DC:ISOL:STAT OFF;\
    :SOUR:DCS:VOLT:LEV 0;\
    :TRIG:DEL 0;\
    :TRIG:SOUR BUS;\
    :TRIG:TDEL 0;\
    :DISP:WIND:TEXT1:DATA:FMSD:STAT OFF;\
    :DISP:WIND:TEXT2:DATA:FMSD:STAT OFF;\
    :FUNC:DCR:RANG:AUTO ON;\
    :FUNC:IMP:RANG:AUTO ON;\
    :OUTP:DC:ISOL:LEV:AUTO ON;\
    :DISP:PAGE list;''' %(acl, level/1000.0, function))
    
    
    LCR.write(':list:freq%s;' %freqstr)
    
    return LCR, sweepfreq
    

def dielectric_freqsweep(LCR,lowlim,uplim,bandsize,level,acl,function):
    
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
    
    LCR.write('''\
    :DISP:CCL;\
    :SOUR:DCS:STAT OFF;\
    :BIAS:STAT OFF;\
    :COMP:BIN:COUN:CLE;\
    :LIST:CLE:ALL;\
    :COMP:BIN:CLE;\
    \
    :AMPL:ALC %d;\
    \
    :APER SHOR,1;\
    :BIAS:POL:AUTO ON;\
    :BIAS:RANG:AUTO ON;\
    :BIAS:VOLT:LEV 0;\
    :COMP:ABIN OFF;\
    :COMP:BIN:COUN:STAT OFF;\
    :COMP:MODE ATOL;\
    :COMP:SLIM -9.9e+37,9.9e+37;\
    :COMP:STAT OFF;\
    :COMP:SWAP OFF;\
    :COMP:TOL:NOM 0;\
    \
    :VOLT:LEV %f;\
    \
    :DISP:ENAB ON;\
    :DISP:LINE "TCX: EL_SWEEP";\
    :DISP:WIND:TEXT1:DATA:FMSD:DATA 1e-09;\
    :DISP:WIND:TEXT2:DATA:FMSD:DATA 1e-09;\
    :FORM:ASC:LONG OFF;\
    :FORM:BORD NORM;\
    :FORM:DATA ASC,64;\
    :FUNC:DCR:RANG:VAL 100;\
    :FUNC:DEV1:MODE OFF;\
    :FUNC:DEV1:REF:VAL 0;\
    :FUNC:DEV2:MODE OFF;\
    :FUNC:DEV2:REF:VAL 0;\
    :FUNC:IMP:RANG:VAL 10;\
    \
    :FUNC:IMP:TYPE %s;\
    \
    :FUNC:SMON:IDC:STAT OFF;\
    :FUNC:SMON:VDC:STAT OFF;\
    :INIT:CONT OFF;\
    :LIST:CLE:ALL;\
    :LIST:MODE STEP;\
    :LIST:STIM:TYPE FREQ,NONE;\
    :OUTP:DC:ISOL:LEV:VAL 0.1;\
    :OUTP:DC:ISOL:STAT OFF;\
    :SOUR:DCS:VOLT:LEV 0;\
    :TRIG:DEL 0;\
    :TRIG:SOUR BUS;\
    :TRIG:TDEL 0;\
    :DISP:WIND:TEXT1:DATA:FMSD:STAT OFF;\
    :DISP:WIND:TEXT2:DATA:FMSD:STAT OFF;\
    :FUNC:DCR:RANG:AUTO ON;\
    :FUNC:IMP:RANG:AUTO ON;\
    :OUTP:DC:ISOL:LEV:AUTO ON;\
    :DISP:PAGE LIST;''' %(acl, level, function))
    
    
    LCR.write(':list:freq%s;' %freqstr)
    
    return LCR, sweepfreq
