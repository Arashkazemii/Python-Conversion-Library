import tkinter as tk
import pyconversion as pycon

def convert():
    func_name = var_func.get()
    value = entry_value.get()
    inScale = entry_inScale.get()
    outScale = entry_outScale.get()
    
    if func_name == 'Temperature':
        result = pycon.UnitConversion.tempCon(float(value), inScale, outScale)
    elif func_name == 'Angle':
        result = pycon.UnitConversion.angleCon(float(value), inScale, outScale)
    elif func_name == 'Area':
        result = pycon.UnitConversion.areaCon(float(value), inScale, outScale)
    elif func_name == 'DataTransferRate':
        result = pycon.UnitConversion.dataTransferRateCon(float(value), inScale, outScale)
    elif func_name == 'DigitalStorage':
        result = pycon.UnitConversion.digitalStorageCon(float(value), inScale, outScale)
    elif func_name == 'Energy':
        result = pycon.UnitConversion.energyCon(float(value), inScale, outScale)
    elif func_name == 'Frequency':
        result = pycon.UnitConversion.frequencyCon(float(value), inScale, outScale)
    elif func_name == 'Length':
        result = pycon.UnitConversion.lengthCon(float(value), inScale, outScale)
    elif func_name == 'Mass':
        result = pycon.UnitConversion.massCon(float(value), inScale, outScale)
    elif func_name == 'Power':
        result = pycon.UnitConversion.powerCon(float(value), inScale, outScale)
    elif func_name == 'Pressure':
        result = pycon.UnitConversion.pressureCon(float(value), inScale, outScale)
    elif func_name == 'Speed':
        result = pycon.UnitConversion.speedCon(float(value), inScale, outScale)
    elif func_name == 'Time':
        result = pycon.UnitConversion.timeCon(float(value), inScale, outScale)
    elif func_name == 'Volume':
        result = pycon.UnitConversion.volumeCon(float(value), inScale, outScale)
    
    
    label_result.config(text=f"Result: {result}")

# Create main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry('250x360')
root.resizable(False,False)

# Function selection
label_func = tk.Label(root, text="Select function:")
label_func.pack(pady=5)

var_func = tk.StringVar(root)
var_func.set('Temperature')

optionmenu_func = tk.OptionMenu(root, var_func, 'Temperature', 'Frequency', 'Power', 'Mass', 'Energy', 'Angle', 'Area', 'DataTransferRate', 'DigitalStorage', 'Length', 'Pressure', 'Speed', 'Time', 'Volume')
optionmenu_func.pack()

# Value input
label_value = tk.Label(root, text="Enter value:")
label_value.pack(pady=5)

entry_value = tk.Entry(root)
entry_value.pack()

# Input scale input
label_inScale = tk.Label(root, text="Enter input scale:")
label_inScale.pack(pady=5)

entry_inScale = tk.Entry(root)
entry_inScale.pack()

# Output scale input
label_outScale = tk.Label(root, text="Enter output scale:")
label_outScale.pack(pady=5)

entry_outScale = tk.Entry(root)
entry_outScale.pack()

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=10)

# Result display
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()