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


