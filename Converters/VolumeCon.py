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
    
    
# Test
print('''Cubic meter': 'm³', 'Liter': 'l', 'Milliliter': 'mL', 'Cubic centimeter': 'cm³', 'Cubic foot': 'ft³',
        'Cubic inch': 'in³', 'Gallon': 'gal', 'Quart': 'qt', 'Pint': 'pt', 'Cup': 'cup', 'Fluid ounce': 'fl oz''')

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ').lower()
outScale = input('Enter Desired Scale :  ').lower()

print(f'{value} {inScale} = {volumeCon(value,inScale,outScale)} {outScale}')