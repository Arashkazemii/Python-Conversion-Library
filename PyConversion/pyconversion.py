def speedCon(value, inScale, outScale) :
    speedScaleDict = {'Meter per second': 'm/s', 'Kilometer per hour': 'km/h', 'Mile per hour': 'mph', 'Knot': 'kn', 'Foot per second': 'ft/s'}
    
    if inScale == 'm/s' :
        if outScale == 'km/h':
            return value * 3.6
        elif outScale == 'mph' :
            return value * 2.237
        elif outScale == 'kn' :
            return value * 1.944
        elif outScale == 'ft/s' :
            return value * 3.281
        else :
            print("Undefined Scale")
            
    elif inScale == 'km/h' :
        if outScale == 'm/s':
            return value / 3.6
        elif outScale == 'mph' :
            return value / 1.609
        elif outScale == 'kn' :
            return value / 1.852
        elif outScale == 'ft/s' :
            return value / 1.097
        else :
            print("Undefined Scale")
            
    elif inScale == 'mph' :
        if outScale == 'm/s':
            return value / 2.237
        elif outScale == 'km/h' :
            return value * 1.609
        elif outScale == 'kn' :
            return value / 1.151
        elif outScale == 'ft/s' :
            return value * 1.467
        else :
            print("Undefined Scale")
            
    elif inScale == 'kn' :
        if outScale == 'm/s':
            return value / 1.944
        elif outScale == 'km/h' :
            return value * 1.852
        elif outScale == 'mph' :
            return value * 1.151
        elif outScale == 'ft/s' :
            return value * 1.688
        else :
            print("Undefined Scale")
            
    elif inScale == 'ft/s' :
        if outScale == 'm/s':
            return value / 3.281
        elif outScale == 'km/h' :
            return value * 1.097
        elif outScale == 'mph' :
            return value / 1.467
        elif outScale == 'kn' :
            return value / 1.688
        else :
            print("Undefined Scale")
            
    else :
        print("Undefined Scale")

def lengthCon(value, inScale, outScale):
    lengthScaleDict = {'Meter': 'm', 'Kilometer': 'km', 'Centimeter': 'cm', 'Millimeter': 'mm', 'Micrometer': 'µm', 'Nanometer': 'nm', 'Mile': 'ml', 'Yard': 'yd',
                       'Foot': 'ft', 'Inch': 'in', 'Nautical Mile': 'nml'}

    if inScale == 'm':
        if outScale == 'km':
            return value / 1000
        elif outScale == 'cm':
            return value * 100
        elif outScale == 'mm':
            return value * 1000
        elif outScale == 'µm':
            return value * 1000000
        elif outScale == 'nm':
            return value * 1000000000
        elif outScale == 'ml':
            return value / 1609
        elif outScale == 'yd':
            return value * 1.094
        elif outScale == 'ft':
            return value * 3.281
        elif outScale == 'in':
            return value * 39.37
        elif outScale == 'nml':
            return value / 1852
        else:
            return value

    elif inScale == 'km':
        if outScale == 'm':
            return value * 1000
        elif outScale == 'cm':
            return value * 100000
        elif outScale == 'mm':
            return value * 1000000
        elif outScale == 'µm':
            return value * 1000000000
        elif outScale == 'nm':
            return value * 1000000000000
        elif outScale == 'ml':
            return value / 1.609
        elif outScale == 'yd':
            return value * 1093.61
        elif outScale == 'ft':
            return value * 3280.84
        elif outScale == 'in':
            return value * 39370.1
        elif outScale == 'nml':
            return value / 1.852
        else:
            return value

    elif inScale == 'cm':
        if outScale == 'm':
            return value / 100
        elif outScale == 'km':
            return value / 100000
        elif outScale == 'mm':
            return value * 10
        elif outScale == 'µm':
            return value * 10000
        elif outScale == 'nm':
            return value * 10000000
        elif outScale == 'ml':
            return value / 160900
        elif outScale == 'yd':
            return value / 91.44
        elif outScale == 'ft':
            return value / 30.48
        elif outScale == 'in':
            return value / 2.54
        elif outScale == 'nml':
            return value / 185200
        else:
            return value

    elif inScale == 'mm':
        if outScale == 'm':
            return value / 1000
        elif outScale == 'km':
            return value / 1000000
        elif outScale == 'cm':
            return value / 10
        elif outScale == 'µm':
            return value * 1000
        elif outScale == 'nm':
            return value * 1000000
        elif outScale == 'ml':
            return value / 1609000
        elif outScale == 'yd':
            return value / 914.4
        elif outScale == 'ft':
            return value / 304.8
        elif outScale == 'in':
            return value / 25.4
        elif outScale == 'nml':
            return value / 1852000
        else:
            return value

    elif inScale == 'µm':
        if outScale == 'm':
            return value / 1000000
        elif outScale == 'km':
            return value / 1000000000
        elif outScale == 'cm':
            return value / 10000
        elif outScale == 'mm':
            return value / 1000
        elif outScale == 'nm':
            return value * 1000
        elif outScale == 'ml':
            return value / 1609000000
        elif outScale == 'yd':
            return value / 914400
        elif outScale == 'ft':
            return value / 304800
        elif outScale == 'in':
            return value / 25400
        elif outScale == 'nml':
            return value / 1852000000
        else:
            return value
        
    elif inScale == 'nm':
        if outScale == 'm':
            return value / 1000000000
        elif outScale == 'km':
            return value / 1000000000000
        elif outScale == 'cm':
            return value / 10000000
        elif outScale == 'mm':
            return value / 1000000
        elif outScale == 'µm':
            return value / 1000
        elif outScale == 'ml':
            return value / 1609000000000
        elif outScale == 'yd':
            return value / 914400000
        elif outScale == 'ft':
            return value / 304800000
        elif outScale == 'in':
            return value / 25400000
        elif outScale == 'nml':
            return value / 1852000000000
        else:
            return value

    elif inScale == 'ml':
        if outScale == 'm':
            return value * 1609
        elif outScale == 'km':
            return value * 1.609
        elif outScale == 'cm':
            return value * 160900
        elif outScale == 'mm':
            return value * 1609000
        elif outScale == 'µm':
            return value * 1609000000
        elif outScale == 'nm':
            return value * 1609000000000
        elif outScale == 'yd':
            return value * 1760
        elif outScale == 'ft':
            return value * 5280
        elif outScale == 'in':
            return value * 63360
        elif outScale == 'nml':
            return value / 1.151
        else:
            return value

    elif inScale == 'yd':
        if outScale == 'm':
            return value / 1.094
        elif outScale == 'km':
            return value / 1093.61
        elif outScale == 'cm':
            return value * 91.44
        elif outScale == 'mm':
            return value * 914.4
        elif outScale == 'µm':
            return value * 914400
        elif outScale == 'nm':
            return value * 914400000
        elif outScale == 'ml':
            return value / 1760
        elif outScale == 'ft':
            return value * 3
        elif outScale == 'in':
            return value * 36
        elif outScale == 'nml':
            return value / 2025
        else:
            return value

    elif inScale == 'ft':
        if outScale == 'm':
            return value / 3.281
        elif outScale == 'km':
            return value / 3280.84
        elif outScale == 'cm':
            return value * 30.48
        elif outScale == 'mm':
            return value * 304.8
        elif outScale == 'µm':
            return value * 304800
        elif outScale == 'nm':
            return value * 304800000
        elif outScale == 'ml':
            return value / 5280
        elif outScale == 'yd':
            return value / 3
        elif outScale == 'in':
            return value * 12
        elif outScale == 'nml':
            return value / 6076.12
        else:
            return value

    elif inScale == 'in':
        if outScale == 'm':
            return value / 39.37
        elif outScale == 'km':
            return value / 39370.1
        elif outScale == 'cm':
            return value * 2.54
        elif outScale == 'mm':
            return value * 25.4
        elif outScale == 'µm':
            return value * 25400
        elif outScale == 'nm':
            return value * 25400000
        elif outScale == 'ml':
            return value / 63360
        elif outScale == 'yd':
            return value / 36
        elif outScale == 'ft':
            return value / 12
        elif outScale == 'nml':
            return value / 72913.4
        else:
            return value

    elif inScale == 'nml':
        if outScale == 'm':
            return value * 1852
        elif outScale == 'km':
            return value * 1.852
        elif outScale == 'cm':
            return value * 185200
        elif outScale == 'mm':
            return value * 1852000
        elif outScale == 'µm':
            return value * 1852000000
        elif outScale == 'nm':
            return value * 1852000000000
        elif outScale == 'ml':
            return value * 1.151
        elif outScale == 'yd':
            return value * 2025
        elif outScale == 'ft':
            return value * 6076.12
        elif outScale == 'in':
            return value * 72913.4
        else:
            return value
        
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
            print("Undefined Scale")
            
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
            print("Undefined Scale")
            
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
            print("Undefined Scale")
        
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
            print("Undefined Scale")
            
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
            print("Undefined Scale")
            
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
            print("Undefined Scale")
            
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
            print("Undefined Scale")
            
    else :
        print("Undefined Scale")
        
