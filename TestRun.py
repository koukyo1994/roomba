import create
import time

ROOMBA_PORT = "/dev/ttyUSB0"

robot = create.Create(ROOMBA_PORT)
robot.toSafeMode()

while True:
    robot.go(0, 20)
    time.sleep(3.0)
    robot.go(20, 0)
    time.sleep(3.0)
    robot.go(0, 20)
    time.sleep(3.0)
    robot.go(-20, 0)
    time.sleep(3.0)
