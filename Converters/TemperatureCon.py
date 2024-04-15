def tempCon(value, inScale, outScale) :
    tempScaleDict = {'Celsius' : 'C', 'Fahrenheit' : 'F', 'Kelvin' : 'K'}
    
    if inScale == 'C' :
        if outScale == 'F' :
            return value * 9/5 + 32
        elif outScale == 'K' :
            return value + 273.15
        else :
            print("Undefined Scale")
    
    elif inScale == 'F' :
        if outScale == 'C' :
            return (value - 32) * 5/9
        elif outScale == 'K' :
            return (value - 32) * 5/9 + 273.15
        else :
            print("Undefined Scale")
    
    elif inScale == 'K' :
        if outScale == 'C' :
            return value - 273.15
        elif outScale == 'F' :
            return (value - 273.15) * 9/5 + 32
        else :
            print("Undefined Scale")
    
    else :
        print("Undefined Scale")
        
        
# Test
print("Scales : Celsius' : 'C', 'Fahrenheit' : 'F', 'Kelvin' : 'K'")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ').lower()
outScale = input('Enter Desired Scale :  ').lower()

print(f'{value} {inScale} = {tempCon(value,inScale,outScale)} {outScale}')