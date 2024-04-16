def digitalStorageCon(value, inScale, outScale) :
    digitalStorageScalesDict = {'Byte' : 'b', 'Kilobyte' : 'kb', 'Megabyte' : 'mb', 'Gigabyte' : 'gb', 'Terabyte' : 'tb', 'Petabyte' : 'pb'}
    
    if inScale == 'b' :
        if outScale == 'kb' :
            return value / 1000
        elif outScale == 'mb' :
            return value / 1e+6
        elif outScale == 'gb' :
            return value / 1e+9
        elif outScale == 'tb' :
            return value / 1e+12
        elif outScale == 'pb' :
            return value / 1e+15
        else :
            return value
    
    elif inScale == 'kb' :
        if outScale == 'b' :
            return value * 1000
        elif outScale == 'mb' :
            return value / 1000
        elif outScale == 'gb' :
            return value / 1e+6
        elif outScale == 'tb' :
            return value / 1e+9
        elif outScale == 'pb' :
            return value / 1e+12
        else :
            return value
        
    elif inScale == 'mb' :
        if outScale == 'b' :
            return value * 1e+6
        elif outScale == 'kb' :
            return value * 1000
        elif outScale == 'gb' :
            return value / 1000
        elif outScale == 'tb' :
            return value / 1e+6
        elif outScale == 'pb' :
            return value / 1e+9
        else :
            return value
        
    elif inScale == 'gb' :
        if outScale == 'b' :
            return value * 1e+9
        elif outScale == 'kb' :
            return value * 1e+6
        elif outScale == 'mb' :
            return value * 1000
        elif outScale == 'tb' :
            return value / 1000
        elif outScale == 'pb' :
            return value / 1e+6
        else :
            return value
        
    elif inScale == 'tb' :
        if outScale == 'b' :
            return value * 1e+12
        elif outScale == 'kb' :
            return value * 1e+9
        elif outScale == 'mb' :
            return value * 1e+6
        elif outScale == 'gb' :
            return value * 1000
        elif outScale == 'pb' :
            return value / 1000
        else :
            return value
        
    elif inScale == 'pb' :
        if outScale == 'b' :
            return value * 1e+15
        elif outScale == 'kb' :
            return value * 1e+12
        elif outScale == 'mb' :
            return value * 1e+9
        elif outScale == 'gb' :
            return value * 1e+6
        elif outScale == 'tb' :
            return value * 1000
        else :
            return value
    
    else :
        return value
    
    
# Test
print("Scales : 'Byte' : 'b', 'Kilobyte' : 'kb', 'Megabyte' : 'mb', 'Gigabyte' : 'gb', 'Terabyte' : 'tb', 'Petabyte' : 'pb' ")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ')
outScale = input('Enter Desired Scale :  ')

print(f'{value} {inScale} = {digitalStorageCon(value,inScale,outScale)} {outScale}')