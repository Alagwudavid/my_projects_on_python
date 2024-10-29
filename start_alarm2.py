# You look at the clock and it is exactly 2 pm.
# You set an alarm to go off in 51 hours.
# At what time does the alarm go off?
# (Hint: you could count on your fingers, but this is not the aim.
# If you are tempted to count on your fingers, change the 51 to 5100.)
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours),
# and ask for the number of hours to wait.
# Your program should output the time on the clock when the alarm goes off.

try:
    # Get the current time and the number of hours to wait for the alarm
    current_time = int(input("Enter the current time in hours (24-hour format, between 0 and 23): "))

    # Check if the input time is within valid 24-hour range
    if current_time < 0 or current_time > 23:
        raise ValueError("Invalid 24-hour time")

    hours_to_wait = int(input("Enter the number of hours to wait: "))

    # Calculate the total number of hours (including current time and waiting time)
    total_hours = current_time + hours_to_wait

    # Calculate the number of days and the remaining hours on the clock
    day_hours = total_hours // 24  # Number of full days
    alarm_time = total_hours % 24  # Time when the alarm goes off

    # Determine if it's AM or PM
    if alarm_time == 0:
        print(f"The alarm will go off in {day_hours} day(s) at 12:00am.")
    elif alarm_time == 12:
        print(f"The alarm will go off in {day_hours} day(s) at 12:00pm.")
    elif alarm_time > 12:
        print(f"The alarm will go off in {day_hours} day(s) at {alarm_time - 12}:00pm.")
    else:
        print(f"The alarm will go off in {day_hours} day(s) at {alarm_time}:00am.")

except ValueError:
    print("Please input a valid 24-hour time and a valid number of hours to wait.")
