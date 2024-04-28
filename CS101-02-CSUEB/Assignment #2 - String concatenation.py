"""
Alan Nguyen
sj5778
"""
print("Trip Planner")

miles = float(input("How many miles will you drive? "))
#Takes user input to define variable miles
speed = float(input("How fast do you drive? "))
#Takes user input to define variable speed
stops = float(input("How many stops will you make? "))
#Takes user input to define variable stops
stopDuration = float(input("How long is each stop? "))
#Takes userinput to define variable 

totalStopDuration = stops * stopDuration
#Calculate total time spend on stops
totalDriveDuration = (miles / speed) * 60
#Calculate total time spend driving on the road

totalTravelDuration = str(totalStopDuration + totalDriveDuration)
#Calculate total travel duration

print("The total trip should take " + totalTravelDuration + " minutes")
#concatenate and print out total trip in minutes
