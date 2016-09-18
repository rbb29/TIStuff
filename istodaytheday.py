import datetime
update_count = x 
#pull this count in from memory somewhere...? 
yes = str (yes)

#update our baseline as cycle starts on new dates
now = datetime.datetime.now()
verify = str (raw_input("Is today the day?"))

print "Great, we'll make some updates to your info."

#update baseline (if verify is yes, and now.date is not equal to baseline...)  
#count updates to cycle baseline
if verify == yes & baseline != now.date: 
  bl_startcycle = now 
  update_count = x + 1
  






