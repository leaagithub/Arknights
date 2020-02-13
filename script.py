import adbutils
import time
import random

RUN_TIME_SECONDS_GT5 = 118
RUN_TIME_SECONDS_GT6 = 160
CURRENT_SANITY = 18
MAX_SANITY = 125
STAGE_COST = 15
RANDOM_NUMBER = 5
PRIME_REFILL = 3
OLD_LEFTOVER_SANITY = 0
LEVEL_UP = False
emulator_id = "emulator-5554"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)
START_SPACE = [1444, 810]
MISSION_START = [1375, 630]
RANDOM_SPOT_CLAIM = [800, 250]
REFILL_PRIME = [1360, 720]
start_time = time.clock()


def reset_run():
    r1 = random.randint(0, RANDOM_NUMBER)
    r3 = random.randint(0, 100)
    r3 = r3 / 100
    time.sleep(5 + r1)
    d.click(RANDOM_SPOT_CLAIM[0], RANDOM_SPOT_CLAIM[1])
    time.sleep(8 + r3)
    d.click(START_SPACE[0], START_SPACE[1])
    time.sleep(5 + r3)
    if LEVEL_UP:
        d.click(START_SPACE[0], START_SPACE[1])
        time.sleep(3)
    d.click(MISSION_START[0], MISSION_START[1])


def end_run():
    r1 = random.randint(0, RANDOM_NUMBER)
    time.sleep(5 + r1)
    d.click(RANDOM_SPOT_CLAIM[0], RANDOM_SPOT_CLAIM[1])


def start_run():
    r3 = random.randint(0, 100)
    r3 = r3 / 100
    time.sleep(8 + r3)
    d.click(START_SPACE[0], START_SPACE[1])
    time.sleep(5 + r3)
    d.click(MISSION_START[0], MISSION_START[1])


def refill_prime():
    time.sleep(4)
    d.click(START_SPACE[0], START_SPACE[1])
    time.sleep(4)
    d.click(REFILL_PRIME[0], REFILL_PRIME[1])
    RUN_NUMBER = MAX_SANITY // STAGE_COST


print('Program Starting....')
d.click(MISSION_START[0], MISSION_START[1])

for x in range(PRIME_REFILL):
    i = 0
    LEFTOVER_SANITY = (CURRENT_SANITY % STAGE_COST) + OLD_LEFTOVER_SANITY
    RUN_NUMBER = (CURRENT_SANITY // STAGE_COST)
    print('Run Number Count: ', RUN_NUMBER, 'Leftover Sanity: ', LEFTOVER_SANITY)
    while i < RUN_NUMBER:
        r2 = random.randint(0, RANDOM_NUMBER)
        time.sleep((RUN_TIME_SECONDS_GT6 - 5) + r2)
        print('Resetting Run....')
        end_run()
        i += 1
        print("Run Number:", i, "with random int: ", r2)
        print('Current clock: ', (int(time.clock() - start_time) + (LEFTOVER_SANITY*300)))
        if (int(time.clock() - start_time) + (LEFTOVER_SANITY*300)) >= 4500:
            RUN_NUMBER += 1
            start_time = time.clock()
            if LEFTOVER_SANITY != 0:
                print('Set the leftover sanity to 0, now we wait for next interval of 4500 seconds alone')
                LEFTOVER_SANITY = 0
            print('Increase run count because 4500 seconds has passed. Restarting Clock.')
            OLD_LEFTOVER_SANITY = 0

        if i < RUN_NUMBER:
            start_run()
            print("Start Run...")
    print('Prime Refill ', x)
    refill_prime()
    CURRENT_SANITY = MAX_SANITY
    OLD_LEFTOVER_SANITY = LEFTOVER_SANITY
    start_run()
print('Done', time.clock() - start_time, "seconds")
