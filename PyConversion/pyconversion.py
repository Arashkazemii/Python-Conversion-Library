class UnitConversion():

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
                return value
        
        elif inScale == 'kilowatt':
            if outScale == 'watt':
                return value * 1000
            elif outScale == 'megawatt':
                return value * 0.001
            elif outScale == 'horsepower':
                return value * 1.34102
            else:
                return value
        
        elif inScale == 'megawatt':
            if outScale == 'watt':
                return value * 1e6
            elif outScale == 'kilowatt':
                return value * 1000
            elif outScale == 'horsepower':
                return value * 1341.02
            else:
                return value
        
        elif inScale == 'horsepower':
            if outScale == 'watt':
                return value * 745.7
            elif outScale == 'kilowatt':
                return value * 0.7457
            elif outScale == 'megawatt':
                return value * 0.0007457
            else:
                return value
        
        else:
            return value

    def timeCon(value, inScale, outScale):
        timeScaleDict = {'Second': 's', 'Millisecond': 'ms', 'Microsecond': 'µs', 'Nanosecond': 'ns', 'Minute': 'min', 'Hour': 'hr', 'Day': 'day', 'Week': 'week'}

        if inScale == 's':
            if outScale == 'ms':
                return value * 1000
            elif outScale == 'µs':
                return value * 1e+6
            elif outScale == 'ns':
                return value * 1e+9
            elif outScale == 'min':
                return value / 60
            elif outScale == 'hr':
                return value / 3600
            elif outScale == 'day':
                return value / 86400
            elif outScale == 'week':
                return value / 604800
            else:
                return value
            
        elif inScale == 'ms':
            if outScale == 's':
                return value * 0.001
            elif outScale == 'µs':
                return value * 1000
            elif outScale == 'ns':
                return value * 1e+6
            elif outScale == 'min':
                return value / 60000
            elif outScale == 'hr':
                return value / 3.6e+6
            elif outScale == 'day':
                return value / 8.64e+7
            elif outScale == 'week':
                return value / 6.048e+8
            else:
                return value
            
        elif inScale == 'µs':
            if outScale == 's':
                return value * 1e-6
            elif outScale == 'ms':
                return value * 0.001
            elif outScale == 'ns':
                return value * 1000
            elif outScale == 'min':
                return value / 6e+7
            elif outScale == 'hr':
                return value / 3.6e+9
            elif outScale == 'day':
                return value / 8.64e+10
            elif outScale == 'week':
                return value / 6.048e+11
            else:
                return value
            
        elif inScale == 'ns':
            if outScale == 's':
                return value * 1e-9
            elif outScale == 'ms':
                return value * 1e-6
            elif outScale == 'µs':
                return value * 0.001
            elif outScale == 'min':
                return value / 6e+10
            elif outScale == 'hr':
                return value / 3.6e+12
            elif outScale == 'day':
                return value / 8.64e+13
            elif outScale == 'week':
                return value / 6.048e+14
            else:
                return value
            
        elif inScale == 'min':
            if outScale == 's':
                return value * 60
            elif outScale == 'ms':
                return value * 60000
            elif outScale == 'µs':
                return value * 6e+7
            elif outScale == 'ns':
                return value * 6e+10
            elif outScale == 'hr':
                return value / 60
            elif outScale == 'day':
                return value / 1440
            elif outScale == 'week':
                return value / 10080
            else:
                return value
            
        elif inScale == 'hr':
            if outScale == 's':
                return value * 3600
            elif outScale == 'ms':
                return value * 3.6e+6
            elif outScale == 'µs':
                return value * 3.6e+9
            elif outScale == 'ns':
                return value * 3.6e+12
            elif outScale == 'min':
                return value * 60
            elif outScale == 'day':
                return value / 24
            elif outScale == 'week':
                return value / 168
            else:
                return value
            
        elif inScale == 'day':
            if outScale == 's':
                return value * 86400
            elif outScale == 'ms':
                return value * 8.64e+7
            elif outScale == 'µs':
                return value * 8.64e+10
            elif outScale == 'ns':
                return value * 8.64e+13
            elif outScale == 'min':
                return value * 1440
            elif outScale == 'hr':
                return value * 24
            elif outScale == 'week':
                return value / 7
            else:
                return value
            
        elif inScale == 'week':
            if outScale == 's':
                return value * 604800
            elif outScale == 'ms':
                return value * 6.048e+8
            elif outScale == 'µs':
                return value * 6.048e+11
            elif outScale == 'ns':
                return value * 6.048e+14
            elif outScale == 'min':
                return value * 10080
            elif outScale == 'hr':
                return value * 168
            elif outScale == 'day':
                return value * 7
            else:
                return value
        else:
            return value

    def volumeCon(value, inScale, outScale):
        volumeScaleDict = {'Cubic meter': 'm³', 'Liter': 'l', 'Milliliter': 'mL', 'Cubic centimeter': 'cm³', 'Cubic foot': 'ft³',
                        'Cubic inch': 'in³', 'Gallon': 'gal', 'Quart': 'qt', 'Pint': 'pt', 'Cup': 'cup', 'Fluid ounce': 'fl oz'}

        if inScale == 'm³':
            if outScale == 'l':
                return value * 1000
            elif outScale == 'mL':
                return value * 1e+6
            elif outScale == 'cm³':
                return value * 1e+6
            elif outScale == 'ft³':
                return value * 35.3147
            elif outScale == 'in³':
                return value * 61023.7
            elif outScale == 'gal':
                return value * 264.172
            elif outScale == 'qt':
                return value * 1056.69
            elif outScale == 'pt':
                return value * 2113.38
            elif outScale == 'cup':
                return value * 4226.75
            elif outScale == 'fl oz':
                return value * 33814
            else:
                return value
        elif inScale == 'l':
            if outScale == 'm³':
                return value * 0.001
            elif outScale == 'mL':
                return value * 1000
            elif outScale == 'cm³':
                return value * 1000
            elif outScale == 'ft³':
                return value * 0.0353147
            elif outScale == 'in³':
                return value * 61.0237
            elif outScale == 'gal':
                return value * 0.264172
            elif outScale == 'qt':
                return value * 1.05669
            elif outScale == 'pt':
                return value * 2.11338
            elif outScale == 'cup':
                return value * 4.22675
            elif outScale == 'fl oz':
                return value * 33.814
            else:
                return value
        elif inScale == 'mL':
            if outScale == 'm³':
                return value * 1e-6
            elif outScale == 'l':
                return value * 0.001
            elif outScale == 'cm³':
                return value
            elif outScale == 'ft³':
                return value * 3.5315e-5
            elif outScale == 'in³':
                return value * 0.0610237
            elif outScale == 'gal':
                return value * 0.000264172
            elif outScale == 'qt':
                return value * 0.00105669
            elif outScale == 'pt':
                return value * 0.00211338
            elif outScale == 'cup':
                return value * 0.00422675
            elif outScale == 'fl oz':
                return value * 0.033814
            else:
                return value
        elif inScale == 'cm³':
            if outScale == 'm³':
                return value * 1e-6
            elif outScale == 'l':
                return value * 0.001
            elif outScale == 'mL':
                return value
            elif outScale == 'ft³':
                return value * 3.5315e-5
            elif outScale == 'in³':
                return value * 0.0610237
            elif outScale == 'gal':
                return value * 0.000264172
            elif outScale == 'qt':
                return value * 0.00105669
            elif outScale == 'pt':
                return value * 0.00211338
            elif outScale == 'cup':
                return value * 0.00422675
            elif outScale == 'fl oz':
                return value * 0.033814
            else:
                return value
        elif inScale == 'ft³':
            if outScale == 'm³':
                return value * 0.0283168
            elif outScale == 'l':
                return value * 28.3168
            elif outScale == 'mL':
                return value * 28316.8
            elif outScale == 'cm³':
                return value * 28316.8
            elif outScale == 'in³':
                return value * 1728
            elif outScale == 'gal':
                return value * 7.48052
            elif outScale == 'qt':
                return value * 29.9221
            elif outScale == 'pt':
                return value * 59.8442
            elif outScale == 'cup':
                return value * 119.688
            elif outScale == 'fl oz':
                return value * 957.506
            else:
                return value
        elif inScale == 'in³':
            if outScale == 'm³':
                return value * 1.63871e-5
            elif outScale == 'l':
                return value * 16.3871
            elif outScale == 'mL':
                return value * 16387.1
            elif outScale == 'cm³':
                return value * 16387.1
            elif outScale == 'ft³':
                return value * 0.000578704
            elif outScale == 'gal':
                return value * 0.004329
            elif outScale == 'qt':
                return value * 0.017316
            elif outScale == 'pt':
                return value * 0.034632
            elif outScale == 'cup':
                return value * 0.0692641
            elif outScale == 'fl oz':
                return value * 0.554113
            else:
                return value
        elif inScale == 'gal':
            if outScale == 'm³':
                return value * 0.00378541
            elif outScale == 'l':
                return value * 3.78541
            elif outScale == 'mL':
                return value * 3785.41
            elif outScale == 'cm³':
                return value * 3785.41
            elif outScale == 'ft³':
                return value * 0.133681
            elif outScale == 'in³':
                return value * 231
            elif outScale == 'qt':
                return value * 4
            elif outScale == 'pt':
                return value * 8
            elif outScale == 'cup':
                return value * 16
            elif outScale == 'fl oz':
                return value * 128
            else:
                return value
        elif inScale == 'qt':
            if outScale == 'm³':
                return value * 0.000946353
            elif outScale == 'l':
                return value * 0.946353
            elif outScale == 'mL':
                return value * 946.353
            elif outScale == 'cm³':
                return value * 946.353
            elif outScale == 'ft³':
                return value * 0.0334201
            elif outScale == 'in³':
                return value * 57.75
            elif outScale == 'gal':
                return value * 0.25
            elif outScale == 'pt':
                return value * 2
            elif outScale == 'cup':
                return value * 4
            elif outScale == 'fl oz':
                return value * 32
            else:
                return value
        elif inScale == 'pt':
            if outScale == 'm³':
                return value * 0.000473176
            elif outScale == 'l':
                return value * 0.473176
            elif outScale == 'mL':
                return value * 473.176
            elif outScale == 'cm³':
                return value * 473.176
            elif outScale == 'ft³':
                return value * 0.0167101
            elif outScale == 'in³':
                return value * 28.875
            elif outScale == 'gal':
                return value * 0.125
            elif outScale == 'qt':
                return value * 0.5
            elif outScale == 'cup':
                return value * 2
            elif outScale == 'fl oz':
                return value * 16
            else:
                return value
        elif inScale == 'cup':
            if outScale == 'm³':
                return value * 0.000236588
            elif outScale == 'l':
                return value * 0.236588
            elif outScale == 'mL':
                return value * 236.588
            elif outScale == 'cm³':
                return value * 236.588
            elif outScale == 'ft³':
                return value * 0.00835503
            elif outScale == 'in³':
                return value * 14.4375
            elif outScale == 'gal':
                return value * 0.0625
            elif outScale == 'qt':
                return value * 0.25
            elif outScale == 'pt':
                return value * 0.5
            elif outScale == 'fl oz':
                return value * 8
            else:
                return value
        elif inScale == 'fl oz':
            if outScale == 'm³':
                return value * 2.9574e-5
            elif outScale == 'l':
                return value * 0.0295735
            elif outScale == 'mL':
                return value * 29.5735
            elif outScale == 'cm³':
                return value * 29.5735
            elif outScale == 'ft³':
                return value * 0.00104438
            elif outScale == 'in³':
                return value * 1.80469
            elif outScale == 'gal':
                return value * 0.0078125
            elif outScale == 'qt':
                return value * 0.03125
            elif outScale == 'pt':
                return value * 0.0625
            elif outScale == 'cup':
                return value * 0.125
            else:
                return value
        else:
            return value

    def digitalStorageCon(value, inScale, outScale) :
        digitalStorageScalesDict = {'Byte' : 'b', 'Kilobyte' : 'kb', 'Megabyte' : 'mb', 'Gigabyte' : 'gb', 'Terabyte' : 'tb', 'Petabyte' : 'pb'}
        
        if inScale == 'b' :
            if outScale == 'kb' :
                return value / 1000
            elif outScale == 'mb' :
                return value / 1e+6
            elif outScale == 'gb' :
                return value / 1e+9
            elif outScale == 'tb' :
                return value / 1e+12
            elif outScale == 'pb' :
                return value / 1e+15
            else :
                return value
        
        elif inScale == 'kb' :
            if outScale == 'b' :
                return value * 1000
            elif outScale == 'mb' :
                return value / 1000
            elif outScale == 'gb' :
                return value / 1e+6
            elif outScale == 'tb' :
                return value / 1e+9
            elif outScale == 'pb' :
                return value / 1e+12
            else :
                return value
            
        elif inScale == 'mb' :
            if outScale == 'b' :
                return value * 1e+6
            elif outScale == 'kb' :
                return value * 1000
            elif outScale == 'gb' :
                return value / 1000
            elif outScale == 'tb' :
                return value / 1e+6
            elif outScale == 'pb' :
                return value / 1e+9
            else :
                return value
            
        elif inScale == 'gb' :
            if outScale == 'b' :
                return value * 1e+9
            elif outScale == 'kb' :
                return value * 1e+6
            elif outScale == 'mb' :
                return value * 1000
            elif outScale == 'tb' :
                return value / 1000
            elif outScale == 'pb' :
                return value / 1e+6
            else :
                return value
            
        elif inScale == 'tb' :
            if outScale == 'b' :
                return value * 1e+12
            elif outScale == 'kb' :
                return value * 1e+9
            elif outScale == 'mb' :
                return value * 1e+6
            elif outScale == 'gb' :
                return value * 1000
            elif outScale == 'pb' :
                return value / 1000
            else :
                return value
            
        elif inScale == 'pb' :
            if outScale == 'b' :
                return value * 1e+15
            elif outScale == 'kb' :
                return value * 1e+12
            elif outScale == 'mb' :
                return value * 1e+9
            elif outScale == 'gb' :
                return value * 1e+6
            elif outScale == 'tb' :
                return value * 1000
            else :
                return value
        
        else :
            return value

    def dataTransferRateCon(value, inScale, outScale) :
        digitalStorageScalesDict = {'Bit per Second' : 'bs', 'Kilobit per Second' : 'kbs', 'Megabit per Second' : 'mbs', 'Gigabit per Second' : 'gbs',
                                    'Terabit per Second' : 'tbs', 'Petabit per Second' : 'pbs'}
        
        if inScale == 'bs' :
            if outScale == 'kbs' :
                return value / 1000
            elif outScale == 'mbs' :
                return value / 1e+6
            elif outScale == 'gbs' :
                return value / 1e+9
            elif outScale == 'tbs' :
                return value / 1e+12
            elif outScale == 'pbs' :
                return value / 1e+15
            else :
                return value
        
        elif inScale == 'kbs' :
            if outScale == 'bs' :
                return value * 1000
            elif outScale == 'mbs' :
                return value / 1000
            elif outScale == 'gbs' :
                return value / 1e+6
            elif outScale == 'tbs' :
                return value / 1e+9
            elif outScale == 'pbs' :
                return value / 1e+12
            else :
                return value
            
        elif inScale == 'mbs' :
            if outScale == 'bs' :
                return value * 1e+6
            elif outScale == 'kbs' :
                return value * 1000
            elif outScale == 'gbs' :
                return value / 1000
            elif outScale == 'tbs' :
                return value / 1e+6
            elif outScale == 'pbs' :
                return value / 1e+9
            else :
                return value
            
        elif inScale == 'gbs' :
            if outScale == 'bs' :
                return value * 1e+9
            elif outScale == 'kbs' :
                return value * 1e+6
            elif outScale == 'mbs' :
                return value * 1000
            elif outScale == 'tbs' :
                return value / 1000
            elif outScale == 'pbs' :
                return value / 1e+6
            else :
                return value
            
        elif inScale == 'tbs' :
            if outScale == 'bs' :
                return value * 1e+12
            elif outScale == 'kbs' :
                return value * 1e+9
            elif outScale == 'mbs' :
                return value * 1e+6
            elif outScale == 'gbs' :
                return value * 1000
            elif outScale == 'pbs' :
                return value / 1000
            else :
                return value
            
        elif inScale == 'pbs' :
            if outScale == 'bs' :
                return value * 1e+15
            elif outScale == 'kbs' :
                return value * 1e+12
            elif outScale == 'mbs' :
                return value * 1e+9
            elif outScale == 'gbs' :
                return value * 1e+6
            elif outScale == 'tbs' :
                return value * 1000
            else :
                return value
        
        else :
            return value
        
    def angleCon(value, inScale, outScale):
        angleScaleDict = {'Degree': 'degree', 'Radian': 'radian', 'Gradian': 'gradian'}
        
        if inScale == 'degree':
            if outScale == 'radian':
                return value * 0.0174533
            elif outScale == 'gradian':
                return value * 1.11111
            else:
                return value
        
        elif inScale == 'radian':
            if outScale == 'degree':
                return value * 57.2958
            elif outScale == 'gradian':
                return value * 63.6619
            else:
                return value
        
        elif inScale == 'gradian':
            if outScale == 'degree':
                return value * 0.9
            elif outScale == 'radian':
                return value * 0.01570796
            else:
                return value
        
        else:
            return value

