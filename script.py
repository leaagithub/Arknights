import adbutils
import time
import random


RUN_TIME_SECONDS = 118
RUN_NUMBER = (138/15) - 1
RANDOM_NUMBER = 10
LEVEL_UP = False
emulator_id = "emulator-5554"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)
START_SPACE = [1444, 810]
MISSION_START = [1375, 630]
RANDOM_SPOT_CLAIM = [800, 250]


def reset_run():
    r1 = random.randint(0, RANDOM_NUMBER)
    r3 = random.randint(0, 100)
    r3 = r3/100
    time.sleep(5 + r1)
    d.click(RANDOM_SPOT_CLAIM[0], RANDOM_SPOT_CLAIM[1])
    time.sleep(8 + r3)
    d.click(START_SPACE[0], START_SPACE[1])
    time.sleep(5 + r3)
    if LEVEL_UP:
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

