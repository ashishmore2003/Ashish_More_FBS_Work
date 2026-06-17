### 1. Convert the time entered in hh,min and sec into seconds.

# Take hours as input from user 
hours = int ( input("Enter The Hours :"))

# Take minutes as input from user 
minutes = int ( input("Enter The Minutes :"))

# Take Seconds as input from user 
seconds = int ( input("Enter The Seconds :"))

# Calculate total seconds
total_sec = (hours * 3600) + (minutes * 60) + seconds

# Display Result
print('Total Seconds :',total_sec)
