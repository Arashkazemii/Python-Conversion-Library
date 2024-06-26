def massCon(value, inScale, outScale) :
    weightScaleDict = {'Kilogram': 'kg', 'Gram': 'g', 'Milligram': 'mg', 'Microgram': 'µg', 'Metric Ton': 't', 'Pound': 'lb', 'Ounce': 'oz'}
    if inScale == 'g' :
        if outScale == 'kg' :
            return value / 1000
        elif outScale == 'mg' :
            return value * 1000
        elif outScale == 'µg' :
            return value * 1e+6
        elif outScale == 't' :
            return value / 1e+6
        elif outScale == 'lb' :
            return value / 453.6
        elif outScale == 'oz' :
            return value / 28.35
        else :
            return value
            
    elif inScale == 'kg' :
        if outScale == 'g' :
            return value * 1000
        elif outScale == 'mg' :
            return value * 1e+6
        elif outScale == 'µg' :
            return value * 1e+9
        elif outScale == 't' :
            return value / 1000
        elif outScale == 'lb' :
            return value * 2.205
        elif outScale == 'oz' :
            return value * 35.274
        else :
            return value
            
    elif inScale == 'mg' :
        if outScale == 'g' :
            return value / 1000
        elif outScale == 'kg' :
            return value / 1e+6
        elif outScale == 'µg' :
            return value * 1000
        elif outScale == 't' :
            return value / 1e+9
        elif outScale == 'lb' :
            return value / 453600
        elif outScale == 'oz' :
            return value / 28350
        else :
            return value
        
    elif inScale == 'µg' :
        if outScale == 'g' :
            return value / 1e+6
        elif outScale == 'kg' :
            return value / 1e+9
        elif outScale == 'mg' :
            return value / 1000
        elif outScale == 't' :
            return value / 1e+12
        elif outScale == 'lb' :
            return value / 4.536e+8
        elif outScale == 'oz' :
            return value / 2.835e+7
        else :
            return value
            
    elif inScale == 't' :
        if outScale == 'g' :
            return value * 1e+6
        elif outScale == 'kg' :
            return value * 1000
        elif outScale == 'mg' :
            return value * 1e+9
        elif outScale == 'µg' :
            return value * 1e+12
        elif outScale == 'lb' :
            return value * 2205
        elif outScale == 'oz' :
            return value * 35270
        else :
            return value
            
    elif inScale == 'lb' :
        if outScale == 'g' :
            return value * 453.6
        elif outScale == 'kg' :
            return value / 2.205
        elif outScale == 'mg' :
            return value * 453600
        elif outScale == 'µg' :
            return value * 4.536e+8
        elif outScale == 't' :
            return value / 2205
        elif outScale == 'oz' :
            return value * 16
        else :
            return value
            
    elif inScale == 'oz' :
        if outScale == 'g' :
            return value * 28.35
        elif outScale == 'kg' :
            return value / 35.274
        elif outScale == 'mg' :
            return value * 28350
        elif outScale == 'µg' :
            return value * 2.835e+7
        elif outScale == 't' :
            return value / 35270
        elif outScale == 'lb' :
            return value / 16
        else :
            return value
            
    else :
        return value
        

# Test!
print("Scales : Kilogram': 'kg', 'Gram': 'g', 'Milligram': 'mg', 'Microgram': 'µg', 'Metric Ton': 't', 'Pound': 'lb', 'Ounce': 'oz")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ').lower()
outScale = input('Enter Desired Scale :  ').lower()

print(f'{value} {inScale} = {massCon(value,inScale,outScale)} {outScale}')