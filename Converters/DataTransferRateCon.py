def dataTransferRateCon(value, inScale, outScale) :
    digitalStorageScalesDict = {'Bit per Second' : 'bs', 'Kilobit per Second' : 'kbs', 'Megabit per Second' : 'mbs', 'Gigabit per Second' : 'gbs',
                                'Terabit per Second' : 'tbs', 'Petabit per Second' : 'pbs'}
    
    if inScale == 'bs' :
        if outScale == 'kbs' :
            return value / 1000
        elif outScale == 'mbs' :
            return value / 1e+6
        elif outScale == 'gbs' :
            return value / 1e+9
        elif outScale == 'tbs' :
            return value / 1e+12
        elif outScale == 'pbs' :
            return value / 1e+15
        else :
            return value
    
    elif inScale == 'kbs' :
        if outScale == 'bs' :
            return value * 1000
        elif outScale == 'mbs' :
            return value / 1000
        elif outScale == 'gbs' :
            return value / 1e+6
        elif outScale == 'tbs' :
            return value / 1e+9
        elif outScale == 'pbs' :
            return value / 1e+12
        else :
            return value
        
    elif inScale == 'mbs' :
        if outScale == 'bs' :
            return value * 1e+6
        elif outScale == 'kbs' :
            return value * 1000
        elif outScale == 'gbs' :
            return value / 1000
        elif outScale == 'tbs' :
            return value / 1e+6
        elif outScale == 'pbs' :
            return value / 1e+9
        else :
            return value
        
    elif inScale == 'gbs' :
        if outScale == 'bs' :
            return value * 1e+9
        elif outScale == 'kbs' :
            return value * 1e+6
        elif outScale == 'mbs' :
            return value * 1000
        elif outScale == 'tbs' :
            return value / 1000
        elif outScale == 'pbs' :
            return value / 1e+6
        else :
            return value
        
    elif inScale == 'tbs' :
        if outScale == 'bs' :
            return value * 1e+12
        elif outScale == 'kbs' :
            return value * 1e+9
        elif outScale == 'mbs' :
            return value * 1e+6
        elif outScale == 'gbs' :
            return value * 1000
        elif outScale == 'pbs' :
            return value / 1000
        else :
            return value
        
    elif inScale == 'pbs' :
        if outScale == 'bs' :
            return value * 1e+15
        elif outScale == 'kbs' :
            return value * 1e+12
        elif outScale == 'mbs' :
            return value * 1e+9
        elif outScale == 'gbs' :
            return value * 1e+6
        elif outScale == 'tbs' :
            return value * 1000
        else :
            return value
    
    else :
        return value
    

# Test
print("""Scales : 'Bit per Second' : 'bs', 'Kilobit per Second' : 'kbs', 'Megabit per Second' : 'mbs', 'Gigabit per Second' : 'gbs',
                                'Terabit per Second' : 'tbs', 'Petabit per Second' : 'pbs' """)

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ')
outScale = input('Enter Desired Scale :  ')

print(f'{value} {inScale} = {dataTransferRateCon(value,inScale,outScale)} {outScale}')