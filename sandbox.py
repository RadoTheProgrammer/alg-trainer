import time
import sys

start_time = time.time()

try:
    while True:
        elapsed = time.time() - start_time
        mins, secs = divmod(int(elapsed), 60)
        hrs, mins = divmod(mins, 60)
        # \r moves the cursor to the start of the line
        sys.stdout.write(f"\rStopwatch: {hrs:02}:{mins:02}:{secs:02}")
        #sys.stdout.flush()
        time.sleep(0.1)  # update 10 times per second
except KeyboardInterrupt:
    print("\nStopped")
