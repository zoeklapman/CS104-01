#Temperature Conditions
#Zoë Klapman
#2 October 2020

temp = int(input("Please enter the current temperature:\n"))
while(temp!=999):
    if temp>90:
        print("Wear shorts")
    elif temp>70:
        print("Short sleeves are fine")
    elif temp>50:
        print("Wear a jacket")
    elif temp>32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")
    temp = int(input("Please enter a new temperature:\n"))