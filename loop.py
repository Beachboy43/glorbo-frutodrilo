import time #lets us add delays 

def control_motor(is_on):
  if is_on:
    print("Motor On")
  else:
    print("Motor off")

def check_temperature(temp):
  if temp > 40:
    print("Critical: System Overheating")
  elif temp > 30:
    print(" Warning: High temperature")
  else:
    print (" Battery OK")

def check_battery(voltage):
  if voltage < 3.3:
    print(" Critical: shut down")
  elif voltage < 3.7:
    print(" low battery: please recjarge")
  else:
      print("battery OK")
#---- Continpus monitoring ---
while True:
  motor_state = True
  temperature = 35
  battery_voltage = 3.5

print("/N---- Sensor check ---")
cotrol_motor(motor_state)
check_temperature(temperature)
check_battery(battery_voltage)

time.sleep(2)
  
