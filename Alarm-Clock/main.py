from playsound3 import playsound
import time

CLEAR = "\033[23"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0    # track how many seconds have passed.

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)   # pauses the program for 1 second on each iteration.
        time_elapsed += 1   # Increase elapsed time by 1 second

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60        # Convert remaining seconds to minutes
        seconds_left = time_left % 60         # Get remaining seconds after minutes

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")  # Display time left in MM:SS format

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)