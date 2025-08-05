#sensor readings (simulated values)
temperature = 32 #in °C
motion_detected = True
light_level = 15     #%
battery_voltage = 3.4 #volts

#--temperature check----
print("temperature:", temperature , "°C")
if temperature > 30:
  print("Warning Overheating!")
else:
  print("Temperature ok")

#--- Motion + light level check ----
print("/nLight level:", light_level, "%")
print("Motion:"), motion_detected
if motion_detected = True and light_level < 30:
  print("el señor de la noche")
else: 
    print("shhhhhh")

# --- Battery check --- 
print("/nBattery voltage:" , battery_voltage, "V")
if battery_voltage < 3.3:
  print("rojo Critical! shut daun de sistem")
elif battery voltage < 3.7:
  print("amarillo low battery plesaase recharge")
else:
  print(";D todo ok")
