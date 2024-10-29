# You look at the clock and it is exactly 2 pm.
# You set an alarm to go off in 51 hours.
# At what time does the alarm go off?
# (Hint: you could count on your fingers, but this is not the aim.
# If you are tempted to count on your fingers, change the 51 to 5100.)
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours),
# and ask for the number of hours to wait.
# Your program should output the time on the clock when the alarm goes off.

# Get the current time and the number of hours to wait for the alarm
current_time = int(input("Enter the current time in hours (24-hour format): "))
hours_to_wait = int(input("Enter the number of hours to wait: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + hours_to_wait) % 24
day_hours = (current_time + hours_to_wait) // 24

# Output the result
if (current_time + hours_to_wait) > 24:
    if alarm_time > 12:
        print(f"The alarm will go off in {day_hours:.0f} day(s) at {alarm_time - 12}:00pm.")
    elif alarm_time < 12:
        print(f"The alarm will go off in {day_hours:.0f} day(s) at {alarm_time}:00am.")
elif (current_time + hours_to_wait) < 24:
    if alarm_time > 12:
        print(f"The alarm will go off today at {alarm_time - 12}:00pm.")
    elif alarm_time < 12:
        print(f"The alarm will go off today at {alarm_time}:00am.")