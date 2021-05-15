###################
# IMPORT MODULES
###################
import datetime

# Define Variables
timeDay = ""


# Define Functions
def getTimeDay():
    time = datetime.datetime.now().strftime('%H')
    if time[0] == 0:
        date = time[1]

    if time >= "0" and time < "12":
        timeDay = "morning"
        return timeDay

    elif time >= "12" and time < "18":
        timeDay = "afternoon"
        return timeDay

    elif time >= "18" and time < "20":
        timeDay = "evening"
        return timeDay

    elif time >= "20" and time < "24":
        timeDay = "night"
        return timeDay

