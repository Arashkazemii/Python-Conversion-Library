def frequencyCon(value, inScale, outScale):
    frequencyScaleDict = {'Hertz': 'Hz', 'Kilohertz': 'kHz', 'Megahertz': 'MHz', 'Gigahertz': 'GHz'}

    if inScale == 'Hz':
        if outScale == 'kHz':
            return value * 0.001
        elif outScale == 'MHz':
            return value * 1e-6
        elif outScale == 'GHz':
            return value * 1e-9
        else:
            return value
    elif inScale == 'kHz':
        if outScale == 'Hz':
            return value * 1000
        elif outScale == 'MHz':
            return value * 1e-3
        elif outScale == 'GHz':
            return value * 1e-6
        else:
            return value
    elif inScale == 'MHz':
        if outScale == 'Hz':
            return value * 1e+6
        elif outScale == 'kHz':
            return value * 1000
        elif outScale == 'GHz':
            return value * 0.001
        else:
            return value
    elif inScale == 'GHz':
        if outScale == 'Hz':
            return value * 1e+9
        elif outScale == 'kHz':
            return value * 1e+6
        elif outScale == 'MHz':
            return value * 1000
        else:
            return value
    else:
        return value
    
    
print("Scales : Hertz': 'Hz', 'Kilohertz': 'kHz', 'Megahertz': 'MHz', 'Gigahertz': 'GHz")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ')
outScale = input('Enter Desired Scale :  ')

print(f'{value} {inScale} = {frequencyCon(value,inScale,outScale)} {outScale}')