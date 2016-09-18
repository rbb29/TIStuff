import datetime

totaldays = raw_input("Enter the avg number of days you menstruate per month:")
try:
  totaldays = float(rawstr)
except:
  totaldays = -1

if totaldays > 0:
  print "Thanks!"
else:
  print "Please enter a number"
  
date = raw_input("Enter the day (1-30/31) of the month your period normally starts on:")
try:
  date = float(rawstr)
except:
  date = -1
  
if totaldays > 0:
  print "Thanks!"
else:
  print "Please enter a number"
  
bl_endcycle = float(date) + float(totaldays)
bl_startcycle = floate (date)

now = datetime.datetime.now()
nextmonth = now + 1

print "Your next cycle should start on" %bl_startcycle "," %nextmonth
