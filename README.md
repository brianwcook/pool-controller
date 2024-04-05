# pool-controller

control century vgreen via RS485

the motor needs to see a RS-485 command at least once per minute or it will time out

good info on how to make python speak modbus
https://medium.com/@peterfitch/modbus-and-rs485-a-python-test-rig-1b5014f709ec

vgreen modbus spec
https://www.troublefreepool.com/attachments/gen3-epc-modbus-communication-protocol-_rev4-17-pdf.358807/



Requirements
- config file should include
  - overall pump start and stop time
  - default pump speed DEFAULT
  - solar heater pump speed HEATER_SPEED which overrides normal pump speed when heater valve is open
  - skimmer mode speed SKIM_SPEED
  - skimmer mode start and stop time

  
define an object or class with pump_on (bool) and pump_speed (int)

Logic to determine pump state
- every 15 seconds figure out what the state of the pump should be, and then send a command
- if time is between start and stop time, pump_on = true and pump_speed = DEFAULT
- if heater is on set PUMP_SPEED = HEATER_SPEED
- if time is between skimmer start and end time
  - if skim_speed > PUMP_SPEED set PUMP_SPEED = skim_speed
send pump command
