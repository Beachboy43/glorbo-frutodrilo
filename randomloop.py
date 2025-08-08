import time
import random

def control_motor(is_on):
  if is_on:
    print("Motor On")
  else:
    print("Motor off")

def check_temperature(temp):
  if temp > 40:
    print("Critical: Shut down system")
  elif temp > 30:
    print("Warning: High temperature")
  else:
    print("Temp OK")

def check_battery(voltage):
  if voltage < 3.3:
    print("Critical: Shut down system")
  elif voltage < 3.7:
    print("Warning: Low battery")
  else:
    print("Battery OK")
#----- continous monitoring____
while True:
  motor_state = random.choice([True, False])
  temperature = randoom.uniform(20, 50)
  battery_voltage = random.uniform(3, 4.2)

  PRINT("N/---- SENSOR CHECK ----")
  control_motor(motor_state)
  check_temperature(temperature)
  check_battery(battery_voltage)

  time.sleep(5)

