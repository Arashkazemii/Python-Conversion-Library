def frequencyCon(value, inScale, outScale):
    frequencyScaleDict = {'Hertz': 'hz', 'Kilohertz': 'khz', 'Megahertz': 'mhz', 'Gigahertz': 'ghz'}

    if inScale == 'hz':
        if outScale == 'khz':
            return value * 0.001
        elif outScale == 'mhz':
            return value * 1e-6
        elif outScale == 'ghz':
            return value * 1e-9
        else:
            return value
    elif inScale == 'khz':
        if outScale == 'hz':
            return value * 1000
        elif outScale == 'mhz':
            return value * 1e-3
        elif outScale == 'ghz':
            return value * 1e-6
        else:
            return value
    elif inScale == 'mhz':
        if outScale == 'hz':
            return value * 1e+6
        elif outScale == 'khz':
            return value * 1000
        elif outScale == 'ghz':
            return value * 0.001
        else:
            return value
    elif inScale == 'ghz':
        if outScale == 'hz':
            return value * 1e+9
        elif outScale == 'khz':
            return value * 1e+6
        elif outScale == 'mhz':
            return value * 1000
        else:
            return value
    else:
        return value
    
    
print("Scales : Hertz': 'hz', 'Kilohertz': 'khz', 'Megahertz': 'mhz', 'Gigahertz': 'GHz")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ')
outScale = input('Enter Desired Scale :  ')

print(f'{value} {inScale} = {frequencyCon(value,inScale,outScale)} {outScale}')