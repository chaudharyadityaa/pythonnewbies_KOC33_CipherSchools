def clockangle (hour, minutes):
    if 00 <= hour <= 24 and 00 <= minutes <= 60:
        #converting the 24hr format to 12 to make calculation easier
        if hour > 12:
            hour = hour - 12

#if user inputs 3:60 the program will assume the time as 4:00
        if minutes == 60:
            hour=hour + 1
            minutes = 00

#calculating the angle

        hour = 0.5*(hour*60+minutes)
        minutes=6*minutes
        hour = hour + minutes / 60
        angle=abs(hour - minutes)
        angle=min(360-angle, angle)

        return angle

    else:
        print("Enter a correct time.")
        exit()

print("_______________________________________________\n")

print("Give a time in hh:mm format in 24 hour notation")

print("_______________________________________________\n")

angle=clockangle(int(input("Hour: ")), int(input("Minutes: ")))

postangle=format (angle, ".2f")

print("\nThe difference between the hour and the minute hand is", postangle + "*")