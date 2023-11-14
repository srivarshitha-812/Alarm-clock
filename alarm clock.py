import datetime
import time
from playsound import playsound

def get_alarm_input():
    while True:
        try:
            alarm_hour = int(input("Enter Hour:"))
            alarm_min = int(input("Enter Minutes:"))
            alarm_am = input("am/pm:")
            alarm_sound = input("Enter the filename of the sound you want to play:")
            if alarm_am == "pm":
                alarm_hour += 12
            return alarm_hour, alarm_min, alarm_sound
        except ValueError:
            print("Invalid input. Please enter a valid hour (0-12) and minute (0-59).")

def set_alarm(alarm_hour, alarm_min, alarm_sound):
    while True:
        now = datetime.datetime.now()
        if alarm_hour == now.hour and alarm_min == now.minute:
            print("playing")
            playsound(alarm_sound)
            snooze = input("Do you want to snooze? (yes/no)")
            if snooze.lower() == "yes":
                time.sleep(600)  # snooze for 10 minutes
                print("playing")
                playsound(alarm_sound)
            else:
                break
        time.sleep(30)  # check every 30 seconds
