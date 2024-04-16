def pressureCon(value, inScale, outScale) :
    pressureScaleDict = {'Bar': 'bar', 'Pascal': 'pa', 'Pound per Square inch': 'psi', 'Standard Atmosphere': 'atm', 'Torr': 'torr'}
    
    if inScale == 'bar' :
        if outScale == 'pa' :
            return value * 100000
        elif outScale == 'psi' :
            return value * 14.504
        elif outScale == 'atm' :
            return value / 1.013
        elif outScale == 'torr' :
            return value * 750.062
        else :
            return value
    
    elif inScale == 'pa' :
        if outScale == 'bar' :
            return value / 100000
        elif outScale == 'psi' :
            return value / 6895
        elif outScale == 'atm' :
            return value / 101300
        elif outScale == 'torr' :
            return value / 133.3
        else :
            return value
            
    elif inScale == 'psi' :
        if outScale == 'bar' :
            return value / 14.504
        elif outScale == 'pa' :
            return value * 6894.76
        elif outScale == 'atm' :
            return value / 14.696
        elif outScale == 'torr' :
            return value * 51.7149
        else :
            return value
            
    elif inScale == 'atm' :
        if outScale == 'bar' :
            return value * 1.013
        elif outScale == 'pa' :
            return value * 101300
        elif outScale == 'psi' :
            return value * 14.696
        elif outScale == 'torr' :
            return value * 760
        else :
            return value
            
    elif inScale == 'torr' :
        if outScale == 'bar' :
            return value / 1.013
        elif outScale == 'pa' :
            return value * 133.3
        elif outScale == 'psi' :
            return value / 51.715
        elif outScale == 'atm' :
            return value / 760
        else :
            return value
            
    else :
            return value


# Test!
print("Scales : Bar': 'bar', 'Pascal': 'pa', 'Pound per Square inch': 'psi', 'Standard Atmosphere': 'atm', 'Torr': 'torr")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ').lower()
outScale = input('Enter Desired Scale :  ').lower()

print(f'{value} {inScale} = {pressureCon(value,inScale,outScale)} {outScale}')