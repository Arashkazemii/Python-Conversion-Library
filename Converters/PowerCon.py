def powerCon(value, inScale, outScale):
    powerScaleDict = {'Watt': 'watt', 'Kilowatt': 'kilowatt', 'Megawatt': 'megawatt', 'Horsepower': 'horsepower'}
    
    if inScale == 'watt':
        if outScale == 'kilowatt':
            return value * 0.001
        elif outScale == 'megawatt':
            return value * 1e-6
        elif outScale == 'horsepower':
            return value * 0.00134102
        else:
            print("Undefined Scale")
    
    elif inScale == 'kilowatt':
        if outScale == 'watt':
            return value * 1000
        elif outScale == 'megawatt':
            return value * 0.001
        elif outScale == 'horsepower':
            return value * 1.34102
        else:
            print("Undefined Scale")
    
    elif inScale == 'megawatt':
        if outScale == 'watt':
            return value * 1e6
        elif outScale == 'kilowatt':
            return value * 1000
        elif outScale == 'horsepower':
            return value * 1341.02
        else:
            print("Undefined Scale")
    
    elif inScale == 'horsepower':
        if outScale == 'watt':
            return value * 745.7
        elif outScale == 'kilowatt':
            return value * 0.7457
        elif outScale == 'megawatt':
            return value * 0.0007457
        else:
            print("Undefined Scale")
    
    else:
        print("Undefined Scale")


# Test!
print("Scales: 'Watt': 'watt', 'Kilowatt': 'kilowatt', 'Megawatt': 'megawatt', 'Horsepower': 'horsepower'")

value = float(input("Enter Value: "))
inScale = input('Enter Value Scale: ')
outScale = input('Enter Desired Scale: ')

print(f'{value} {inScale} = {powerCon(value, inScale, outScale)} {outScale}')