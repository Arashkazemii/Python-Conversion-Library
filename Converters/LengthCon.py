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
        
