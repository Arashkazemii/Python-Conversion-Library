def angleCon(value, inScale, outScale):
    angleScaleDict = {'Degree': 'degree', 'Radian': 'radian', 'Gradian': 'gradian'}
    
    if inScale == 'degree':
        if outScale == 'radian':
            return value * 0.0174533
        elif outScale == 'gradian':
            return value * 1.11111
        else:
            print("Undefined Scale")
    
    elif inScale == 'radian':
        if outScale == 'degree':
            return value * 57.2958
        elif outScale == 'gradian':
            return value * 63.6619
        else:
            print("Undefined Scale")
    
    elif inScale == 'gradian':
        if outScale == 'degree':
            return value * 0.9
        elif outScale == 'radian':
            return value * 0.01570796
        else:
            print("Undefined Scale")
    
    else:
        print("Undefined Scale")
        
# Test!
print("Scales: 'Degree': 'degree', 'Radian': 'radian', 'Gradian': 'gradian'")

value = float(input("Enter Value: "))
inScale = input('Enter Value Scale: ')
outScale = input('Enter Desired Scale: ')

print(f'{value} {inScale} = {angleCon(value, inScale, outScale)} {outScale}')