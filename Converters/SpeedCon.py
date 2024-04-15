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

