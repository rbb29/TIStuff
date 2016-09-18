import datetime

totaldays = raw_input("Enter the avg number of days you menstruate per month:")
date = raw_input("Enter the day (1-30/31) of the month your period normally starts on:")
bl_endcycle = float(date) + float(totaldays)
bl_startcycle = floate (date)

now = datetime.datetime.now()
nextmonth = now + 1

print "Your next cycle should start on" %bl_startcycle "," %nextmonth
