# 🕒 4. Countdown Timer
# User enters time (e.g., 1 min 30 sec), and it counts down to zero.
# Prints each second in the console.

import time

seconds = int(input("Enter time in seconds: "))
while seconds:
    mins, secs = divmod(seconds, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1
print("Time's up!")

# Alternative implementation using a simple loop
# seconds = int(input("Enter time in seconds: "))
# while seconds:
#     print(f"Time left: {seconds} sec")
#     time.sleep(1)
#     seconds -= 1

# print("Time's up!")