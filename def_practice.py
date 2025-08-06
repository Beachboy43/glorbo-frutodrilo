def check_temperature(temp):
  if temp > 30:
    print("warning: Overheating")
  else:
    print("Temperature ok")

def control_light(motion, light_level):
  if motion and light_level < 30:
    print("light on")
  else:
    print("light off")

def check_battery(voltage):
  if voltage < 3.3:
    print("CRITICAL, shut down system")
  elif voltage < 3.7:
    print("low battery, please recharge")
  else:
    print("todo ok")

#-----Main program------
temperature = 32
motion_detected =True
light_level = 15
battery_voltage =3.4

print("temperature:", temperature, "°C")
print("motion detected:", motion_detected)
control_light(motion_detected, light level)

print("battery voltage:", battery_voltage, "V")
check_battery(battery_voltage)
