# A programs converts a time from one time zone to another
# 
# 1. Taking input
# 2. Create a datetime
# 3. Get the timezones (Eastern, Central, Mountain or Pacific)
# 4. Convert to timezones and store it
# 5. Print the time

# Visit: https://www.youtube.com/watch?v=3DT5_A9X7TM

# For instance
#   Time: 11:48 pm
#   Starting zone: Pacific
#   Ending zone: Eastern
#   2:48 am

from datetime import datetime
from pytz import timezone

t  = input('Enter a time in 24-hour format: \n')

time = datetime.strptime(t,'%H:%M')

print(time.strftime('%I:%M %p'))





