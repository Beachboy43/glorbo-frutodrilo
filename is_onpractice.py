def control_motor (is_on):
  if is_on:
    print("MOtor ON")
  else:
      print("Motor OFF")


def check_temperature(temp):
  if temp > 40:
    print("System Overheating")
elif temp > 30:
    print(" High Temperature")
else:
  print("Todo ok")
  

def check_battery (voltage)
  if voltage < 3.3:
    print("Critical! Shut down")
  elif voltage < 3.7 
    print("Low battery")
  else
    print("Battery OK"


control_motor(True)
check_temperature(35)
check_battery(3.5)
    

