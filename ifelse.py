motion_detected = True   #Boolean from PIR sensor 
light_level = 20         #light level from ldr sensor (0-100, lower = darker)
print("Light level", light_level, "%")
 print("Motion detected:", motion_detected)
if motion_detected and light_level < 30:
  print("Light ON")
else:
  print("Light OFF")
