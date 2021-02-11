import calendar as cal
from datetime import *

print("\n",cal.month(int(input("\nEnter a year:\t")),int(input("Enter a month:\t"))))

print("Is leap year:\t",cal.isleap(int(input("Enter a year to check for leap year:\t"))))

today = datetime.today()
print("\n\n\tTODAY\nDate:\t",today.day,"\\",today.month,"\\",today.year,"\n")
print("Time:\t",today.hour,":",today.minute,":",today.second)
