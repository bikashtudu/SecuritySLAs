import os 
import re
import datetime

currentDT = datetime.datetime.now()

m1 = {}

in_file = open("service.log","r")
output_file = open("/home/prasad/Desktop/btp/en_file/service_data_"+str(currentDT.hour)+":"+str(currentDT.minute)+".pl","w+")

soft1 = "acpid"
soft2 = "bluetooth"

for line in in_file:
	if (soft1 in line) or (soft2 in line):
		a = line.split(' ')
		ser_name = a[0].lower()
		ser_state = a[1].lower()
		if ser_name in m1:	
			if not(ser_state in m1[ser_name]):
				m1[ser_name].append(ser_state)
				file_output = 'service_check('+ser_name+','+ser_state+',vm2).\n'
				output_file.write(file_output)			
		else:	
			m1[ser_name] = [ser_state]	
			file_output = 'service_check('+ser_name+','+ser_state+',vm2).\n'
			output_file.write(file_output)

output_file.close()
in_file.close()	
	    
		






