def energyCon(value, inScale, outScale):
    energyScaleDict = {'Joule': 'J', 'Kilojoule': 'kJ', 'Calorie': 'cal', 'Kilocalorie': 'kcal', 'Electronvolt': 'eV', 'British thermal unit': 'BTU', 'Foot-pound': 'ft-lb'}

    if inScale == 'J':
        if outScale == 'kJ':
            return value * 0.001
        elif outScale == 'cal':
            return value * 0.239006
        elif outScale == 'kcal':
            return value * 0.000239006
        elif outScale == 'eV':
            return value * 6.242e+18
        elif outScale == 'BTU':
            return value * 0.000947817
        elif outScale == 'ft-lb':
            return value * 0.737562
        else:
            return value
    elif inScale == 'kJ':
        if outScale == 'J':
            return value * 1000
        elif outScale == 'cal':
            return value * 239.006
        elif outScale == 'kcal':
            return value * 0.239006
        elif outScale == 'eV':
            return value * 6.242e+21
        elif outScale == 'BTU':
            return value * 0.947817
        elif outScale == 'ft-lb':
            return value * 737.562
        else:
            return value
    elif inScale == 'cal':
        if outScale == 'J':
            return value * 4.184
        elif outScale == 'kJ':
            return value * 0.004184
        elif outScale == 'kcal':
            return value * 0.001
        elif outScale == 'eV':
            return value * 2.613e+19
        elif outScale == 'BTU':
            return value * 0.00396567
        elif outScale == 'ft-lb':
            return value * 3.08596
        else:
            return value
    elif inScale == 'kcal':
        if outScale == 'J':
            return value * 4184
        elif outScale == 'kJ':
            return value * 4.184
        elif outScale == 'cal':
            return value * 1000
        elif outScale == 'eV':
            return value * 2.613e+22
        elif outScale == 'BTU':
            return value * 3.96567
        elif outScale == 'ft-lb':
            return value * 3085.96
        else:
            return value
    elif inScale == 'eV':
        if outScale == 'J':
            return value * 1.602e-19
        elif outScale == 'kJ':
            return value * 1.602e-22
        elif outScale == 'cal':
            return value * 3.8293e-20
        elif outScale == 'kcal':
            return value * 3.8293e-23
        elif outScale == 'BTU':
            return value * 3.828e-20
        elif outScale == 'ft-lb':
            return value * 2.685e-19
        else:
            return value
    elif inScale == 'BTU':
        if outScale == 'J':
            return value * 1055.06
        elif outScale == 'kJ':
            return value * 1.05506
        elif outScale == 'cal':
            return value * 252.164
        elif outScale == 'kcal':
            return value * 0.252164
        elif outScale == 'eV':
            return value * 2.611e+19
        elif outScale == 'ft-lb':
            return value * 778.169
        else:
            return value
    elif inScale == 'ft-lb':
        if outScale == 'J':
            return value * 1.35582
        elif outScale == 'kJ':
            return value * 0.00135582
        elif outScale == 'cal':
            return value * 0.323831
        elif outScale == 'kcal':
            return value * 0.000323831
        elif outScale == 'eV':
            return value * 3.725e+18
        elif outScale == 'BTU':
            return value * 0.00128507
        else:
            return value
    else:
        return value
    

# Test
print("Scales : Joule': 'J', 'Kilojoule': 'kJ', 'Calorie': 'cal', 'Kilocalorie': 'kcal', 'Electronvolt': 'eV', 'British thermal unit': 'BTU', 'Foot-pound': 'ft-lb")

value = float(input("Enter Value :  "))
inScale = input('Enter Value Scale :  ')
outScale = input('Enter Desired Scale :  ')

print(f'{value} {inScale} = {energyCon(value,inScale,outScale)} {outScale}')