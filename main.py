#!/usr/bin/env python

from networktables import NetworkTables
import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH)

print("Setting up NetworkTables")
if not NetworkTables.isConnected():
    print("connecting network table")
    NetworkTables.startClientTeam(3566)
    # NetworkTables.initialize(server='10.35.66.2')
    time.sleep(1)
if NetworkTables.isConnected():
    print("Network table connected")

if NetworkTables.isConnected():
    print("Network table connected")

nt = NetworkTables.getTable("LiveWindow/LegoController")

try:
    while True:

        if not NetworkTables.isConnected():
            print("connection lost, restarting network table")
            NetworkTables.startClientTeam(3566)
            # NetworkTables.initialize(server='10.35.66.2')
            time.sleep(1)

        try:
            print('Gyro: ' + BP.get_sensor(BP.PORT_1))
            nt.putNumber('gyro', BP.get_sensor(BP.PORT_1))
            print('Infrared: ' + BP.get_sensor(BP.PORT_2))
            nt.putNumber('infrared', BP.get_sensor(BP.PORT_2))
            print('Touch: ' + BP.get_sensor(BP.PORT_3))
            nt.putNumber('touch', BP.get_sensor(BP.PORT_3))

        except brickpi3.SensorError as error:
            print(error)

        # time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except:  # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.