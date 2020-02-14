import adbutils
import time
import random

# SANITY AND TIME VARIABLES
RUN_TIME_SECONDS_GT5 = 118
RUN_TIME_SECONDS_GT6 = 160
CURRENT_SANITY = 96
MAX_SANITY = 125
STAGE_COST = 15
RANDOM_NUMBER = 5
PRIME_REFILL = 5
CURRENT_EXP = 7276
TOTAL_EXP = 15000
EXP_PER_RUN = 180
RUN_NUMBER = 0

# SCREEN VARIABLES

START_SPACE = [1444, 810]
MISSION_START = [1375, 630]
RANDOM_SPOT_CLAIM = [800, 250]
REFILL_PRIME = [1360, 720]

# DECLARED VARIABLES NEEDED
emulator_id = "emulator-5554"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)
start_time = time.perf_counter()
OLD_LEFTOVER_SANITY = 0
LEFTOVER_CLOCK = 0
LEVEL_UP = False


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


def cal_run_number():
    global LEFTOVER_SANITY
    global RUN_NUMBER
    LEFTOVER_SANITY = (CURRENT_SANITY % STAGE_COST) + OLD_LEFTOVER_SANITY
    RUN_NUMBER = (CURRENT_SANITY // STAGE_COST)


def cal_exp():
    global CURRENT_EXP
    global TOTAL_EXP
    global EXP_PER_RUN
    global CURRENT_SANITY
    CURRENT_EXP += EXP_PER_RUN
    if CURRENT_EXP > TOTAL_EXP:
        # LEVEL UP
        CURRENT_EXP = CURRENT_EXP - TOTAL_EXP
        TOTAL_EXP = TOTAL_EXP + 1000
        # GUESS OF WHEN NEXT LEVEL UPS
        time.sleep(2)
        d.click(REFILL_PRIME[0], REFILL_PRIME[1])
        # CLICK ANYWHERE JUST TO GET OUT OF LEVEL UP SCREEN
        CURRENT_SANITY = (RUN_NUMBER*STAGE_COST) + LEFTOVER_SANITY + MAX_SANITY
        # RECALCULATE THE RUN NUMBERS
        cal_run_number()
    print('EXP NEEDED TO LEVEL', TOTAL_EXP-CURRENT_EXP)


print('Program Starting....')
d.click(MISSION_START[0], MISSION_START[1])

for x in range(PRIME_REFILL):
    i = 0
    cal_run_number()
    print('Run Number Count: ', RUN_NUMBER, 'Leftover Sanity: ', LEFTOVER_SANITY)
    while i < RUN_NUMBER:
        r2 = random.randint(0, RANDOM_NUMBER)
        time.sleep((RUN_TIME_SECONDS_GT6 - 5) + r2)
        cal_exp()
        print('Resetting Run....')
        end_run()
        i += 1
        print("Run Number:", i, "with random int: ", r2)
        print('Current clock: ', (int(time.perf_counter() - start_time) + (LEFTOVER_SANITY * 300) + LEFTOVER_CLOCK))
        if (int(time.perf_counter() - start_time) + (LEFTOVER_SANITY * 300) + LEFTOVER_CLOCK) >= 4500:
            RUN_NUMBER += 1
            LEFTOVER_CLOCK = (int(time.perf_counter() - start_time) + (LEFTOVER_SANITY * 300) + LEFTOVER_CLOCK) - 4500
            start_time = time.perf_counter()
            if LEFTOVER_SANITY != 0:
                print('Set the leftover sanity to 0, now we wait for next interval of 4500 seconds alone')
                LEFTOVER_SANITY = 0
            print('Increase run count because 4500 seconds has passed. Restarting Clock.')
            OLD_LEFTOVER_SANITY = 0

        if i < RUN_NUMBER:
            start_run()
            print("Start Run...")
    if x != PRIME_REFILL - 1:
        print('Prime Refill ', x)
        refill_prime()
    else:
        print('Stopping Last Prime Refill')
    CURRENT_SANITY = MAX_SANITY
    OLD_LEFTOVER_SANITY = LEFTOVER_SANITY
    start_run()
print('Done', time.clock() - start_time, "seconds")
