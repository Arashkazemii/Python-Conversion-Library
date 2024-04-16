def tempCon(value, inScale, outScale) :
    tempScaleDict = {'Celsius' : 'C', 'Fahrenheit' : 'F', 'Kelvin' : 'K'}
    
    if inScale == 'C' or 'c' :
        if outScale == 'F' or 'f' :
            return value * 9/5 + 32
        elif outScale == 'K' or 'k' :
            return value + 273.15
        else :
            return value
    
    elif inScale == 'F' or 'f' :
        if outScale == 'C' or 'c' :
            return (value - 32) * 5/9
        elif outScale == 'K' or 'k' :
            return (value - 32) * 5/9 + 273.15
        else :
            return value
    
    elif inScale == 'K' or 'k' :
        if outScale == 'C' or 'c' :
            return value - 273.15
        elif outScale == 'F' or 'f' :
            return (value - 273.15) * 9/5 + 32
        else :
            return value
    
    else :
        return value
        
        
# Test
print("Scales : Celsius' : 'C', 'Fahrenheit' : 'F', 'Kelvin' : 'K'")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ')
outScale = input('Enter Desired Scale :  ')

print(f'{value} {inScale} = {tempCon(value,inScale,outScale)} {outScale}')