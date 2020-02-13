import adbutils
import time
FRIEND_LIST_NUMBER = 25
NEXT_FRIEND_SPOT = [1480, 770]
emulator_id = "emulator-5554"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)

#Goes thru half the list expecting half the list to finish clues
for x in range(FRIEND_LIST_NUMBER//2 + 5):
    time.sleep(5)
    d.click(NEXT_FRIEND_SPOT[0], NEXT_FRIEND_SPOT[1])
    print('Friend #', x)

print('Done')