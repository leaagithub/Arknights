import adbutils
import time
import random


RUN_TIME_SECONDS = 120
RUN_NUMBER = 5
RANDOM_NUMBER = 10
emulator_id = "emulator-5554"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)
START_SPACE = [1444, 810]
MISSION_START = [1375, 630]


def reset_run():
    r1 = random.randint(0, RANDOM_NUMBER)
    time.sleep(5 + r1)
    d.click(START_SPACE[0], START_SPACE[1])
    time.sleep(5 + r1)
    d.click(START_SPACE[0], START_SPACE[1])
    time.sleep(3)
    d.click(MISSION_START[0], MISSION_START[1])


i = 0
d.click(MISSION_START[0], MISSION_START[1])
print('Program Starting....')
while i < RUN_NUMBER:
    r2 = random.randint(0, RANDOM_NUMBER)
    time.sleep(113 + r2)
    print('Resetting Run....')
    reset_run()
    i += 1
    print("######################################################Run Number: ", i, "  With random int: ", r2)

