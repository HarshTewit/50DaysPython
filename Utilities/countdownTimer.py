import time 

while True:
    try:
        timerLen = int(input("Enter the time in seconds."))
        if timerLen < 1:
            print("Please enter a number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid input, please enter a whole number")

print("Timer Started! ")

for remaining in range(timerLen, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"Time left: {time_format}", end = "\r")
    time.sleep(1)

print("Time's up! Onto the next.")
