import time
import random

# def waiting_game():
# This represents our number of target seconds to wait
target = random.randint(2,4)
print(f"Your target time is {target} seconds")

input("---Press Enter To Begin---")
start = time.perf_counter()

input(f"\n...Press Enter again after {target} seconds")
elapsed = time.perf_counter() - start

print(f"\n...Elapsed time : {elapsed:.3f} seconds")
if elapsed == target:
    print(f"Unbelievable perfect timing")
elif elapsed < target:
    print(f"Seconds too fast {(target - elapsed):.3f}")
else:
    print(f"Seconds too slow {(elapsed - target):.3f}")