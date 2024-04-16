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
    

# Test!
print("Scales: 'Second': 's', 'Millisecond': 'ms', 'Microsecond': 'µs', 'Nanosecond': 'ns', 'Minute': 'min', 'Hour': 'hr', 'Day': 'day', 'Week': 'week' ")

value = float(input("Enter Value: "))
inScale = input('Enter Value Scale: ')
outScale = input('Enter Desired Scale: ')

print(f'{value} {inScale} = {timeCon(value, inScale, outScale)} {outScale}')