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
            return value
            
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
            return value
            
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
            return value
            
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
            return value
            
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
            return value
            
    else :
        return value

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

def tempCon(value, inScale, outScale) :
    tempScaleDict = {'Celsius' : 'C', 'Fahrenheit' : 'F', 'Kelvin' : 'K'}
    
    if inScale == 'C' :
        if outScale == 'F' :
            return value * 9/5 + 32
        elif outScale == 'K' :
            return value + 273.15
        else :
            return value
    
    elif inScale == 'F' :
        if outScale == 'C' :
            return (value - 32) * 5/9
        elif outScale == 'K' :
            return (value - 32) * 5/9 + 273.15
        else :
            return value
    
    elif inScale == 'K' :
        if outScale == 'C' :
            return value - 273.15
        elif outScale == 'F' :
            return (value - 273.15) * 9/5 + 32
        else :
            return value
    
    else :
        return value

def areaCon(value, inScale, outScale):
    areaScaleDict = {'Square meter': 'm2', 'Square kilometer': 'km2', 'Square centimeter': 'cm2', 'Square millimeter': 'mm2', 'Hectare': 'ha', 'Square foot': 'ft2', 'Square yard': 'yd2', 'Acre': 'ac'}

    if inScale == 'm2':
        if outScale == 'km2':
            return value * 1e-6
        elif outScale == 'cm2':
            return value * 10000
        elif outScale == 'mm2':
            return value * 1e+6
        elif outScale == 'ha':
            return value * 1e-4
        elif outScale == 'ft2':
            return value * 10.7639
        elif outScale == 'yd2':
            return value * 1.19599
        elif outScale == 'ac':
            return value * 0.000247105
        else:
            return value
    elif inScale == 'km2':
        if outScale == 'm2':
            return value * 1e+6
        elif outScale == 'cm2':
            return value * 1e+10
        elif outScale == 'mm2':
            return value * 1e+12
        elif outScale == 'ha':
            return value * 100
        elif outScale == 'ft2':
            return value * 10763900.389
        elif outScale == 'yd2':
            return value * 11959900.01
        elif outScale == 'ac':
            return value * 247.105
        else:
            return value
    elif inScale == 'cm2':
        if outScale == 'm2':
            return value * 1e-4
        elif outScale == 'km2':
            return value * 1e-10
        elif outScale == 'mm2':
            return value * 100
        elif outScale == 'ha':
            return value * 1e-8
        elif outScale == 'ft2':
            return value * 0.00107639
        elif outScale == 'yd2':
            return value * 0.00119599
        elif outScale == 'ac':
            return value * 2.47105e-8
        else:
            return value
    elif inScale == 'mm2':
        if outScale == 'm2':
            return value * 1e-6
        elif outScale == 'km2':
            return value * 1e-12
        elif outScale == 'cm2':
            return value * 0.01
        elif outScale == 'ha':
            return value * 1e-10
        elif outScale == 'ft2':
            return value * 1.07639e-5
        elif outScale == 'yd2':
            return value * 1.19599e-5
        elif outScale == 'ac':
            return value * 2.47105e-10
        else:
            return value
    elif inScale == 'ha':
        if outScale == 'm2':
            return value * 10000
        elif outScale == 'km2':
            return value * 0.01
        elif outScale == 'cm2':
            return value * 1e+8
        elif outScale == 'mm2':
            return value * 1e+10
        elif outScale == 'ft2':
            return value * 107639.104
        elif outScale == 'yd2':
            return value * 119599.004
        elif outScale == 'ac':
            return value * 2.47105
        else:
            return value
    elif inScale == 'ft2':
        if outScale == 'm2':
            return value * 0.092903
        elif outScale == 'km2':
            return value * 9.2903e-8
        elif outScale == 'cm2':
            return value * 929.03
        elif outScale == 'mm2':
            return value * 92903.04
        elif outScale == 'ha':
            return value * 9.2903e-6
        elif outScale == 'yd2':
            return value * 0.111111
        elif outScale == 'ac':
            return value * 2.2957e-5
        else:
            return value
    elif inScale == 'yd2':
        if outScale == 'm2':
            return value * 0.836127
        elif outScale == 'km2':
            return value * 8.36127e-7
        elif outScale == 'cm2':
            return value * 8361.27
        elif outScale == 'mm2':
            return value * 836127
        elif outScale == 'ha':
            return value * 8.36127e-5
        elif outScale == 'ft2':
            return value * 9
        elif outScale == 'ac':
            return value * 0.000206612
        else:
            return value
    elif inScale == 'ac':
        if outScale == 'm2':
            return value * 4046.86
        elif outScale == 'km2':
            return value * 0.00404686
        elif outScale == 'cm2':
            return value * 40468564.2
        elif outScale == 'mm2':
            return value * 4.04686e+9
        elif outScale == 'ha':
            return value * 0.404686
        elif outScale == 'ft2':
            return value * 43560
        elif outScale == 'yd2':
            return value * 4840
        else:
            return value
    else:
        return value

def energyCon(value, inScale, outScale):
    energyScaleDict = {'Joule': 'j', 'Kilojoule': 'kj', 'Calorie': 'cal', 'Kilocalorie': 'kcal', 'Electronvolt': 'ev', 'British thermal unit': 'btu', 'Foot-pound': 'ft-lb'}

    if inScale == 'j':
        if outScale == 'kj':
            return value * 0.001
        elif outScale == 'cal':
            return value * 0.239006
        elif outScale == 'kcal':
            return value * 0.000239006
        elif outScale == 'ev':
            return value * 6.242e+18
        elif outScale == 'btu':
            return value * 0.000947817
        elif outScale == 'ft-lb':
            return value * 0.737562
        else:
            return value
    elif inScale == 'kj':
        if outScale == 'j':
            return value * 1000
        elif outScale == 'cal':
            return value * 239.006
        elif outScale == 'kcal':
            return value * 0.239006
        elif outScale == 'ev':
            return value * 6.242e+21
        elif outScale == 'btu':
            return value * 0.947817
        elif outScale == 'ft-lb':
            return value * 737.562
        else:
            return value
    elif inScale == 'cal':
        if outScale == 'j':
            return value * 4.184
        elif outScale == 'kj':
            return value * 0.004184
        elif outScale == 'kcal':
            return value * 0.001
        elif outScale == 'ev':
            return value * 2.613e+19
        elif outScale == 'btu':
            return value * 0.00396567
        elif outScale == 'ft-lb':
            return value * 3.08596
        else:
            return value
    elif inScale == 'kcal':
        if outScale == 'j':
            return value * 4184
        elif outScale == 'kj':
            return value * 4.184
        elif outScale == 'cal':
            return value * 1000
        elif outScale == 'ev':
            return value * 2.613e+22
        elif outScale == 'btu':
            return value * 3.96567
        elif outScale == 'ft-lb':
            return value * 3085.96
        else:
            return value
    elif inScale == 'ev':
        if outScale == 'j':
            return value * 1.602e-19
        elif outScale == 'kj':
            return value * 1.602e-22
        elif outScale == 'cal':
            return value * 3.8293e-20
        elif outScale == 'kcal':
            return value * 3.8293e-23
        elif outScale == 'btu':
            return value * 3.828e-20
        elif outScale == 'ft-lb':
            return value * 2.685e-19
        else:
            return value
    elif inScale == 'btu':
        if outScale == 'j':
            return value * 1055.06
        elif outScale == 'kj':
            return value * 1.05506
        elif outScale == 'cal':
            return value * 252.164
        elif outScale == 'kcal':
            return value * 0.252164
        elif outScale == 'ev':
            return value * 2.611e+19
        elif outScale == 'ft-lb':
            return value * 778.169
        else:
            return value
    elif inScale == 'ft-lb':
        if outScale == 'j':
            return value * 1.35582
        elif outScale == 'kj':
            return value * 0.00135582
        elif outScale == 'cal':
            return value * 0.323831
        elif outScale == 'kcal':
            return value * 0.000323831
        elif outScale == 'ev':
            return value * 3.725e+18
        elif outScale == 'btu':
            return value * 0.00128507
        else:
            return value
    else:
        return value

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

