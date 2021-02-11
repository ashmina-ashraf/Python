import datetime

time = datetime.datetime.now()
print("\n\na) Current Time:\t",time.strftime('%I:%M:%S'))

b = time - datetime.timedelta(days=5)
print("\nb) Subtracting 5 days from current date:\t",b.strftime('%d/%m/%Y'))

yest = time - datetime.timedelta(days=1)
tomo = time + datetime.timedelta(days=1)
print("\nc) Yesterday:\t",yest.strftime('%d/%m/%Y  %A'),"\n   Today:\t",time.strftime('%d/%m/%Y  %A'),
	"\n   Tomorrow:\t",tomo.strftime('%d/%m/%Y  %A'))

d = time + datetime.timedelta(days=5)
print("\nd) Next 5 days from today:\t",d.strftime('%d/%m/%Y'))

e = time + datetime.timedelta(seconds=5)
print("\ne) Adding 5 seconds to current time:\t",e.strftime('%I:%M:%S'),"\n\n")
