import os 
import re
import datetime

currentDT = datetime.datetime.now()

m1 = {}

match1 = "session opened for"

in_file = open("/var/log/auth.log","r")
output_file = open("/home/prasad/Desktop/btp/en_file/login_data_"+str(currentDT.hour)+":"+str(currentDT.minute)+".pl","w+")

for line in in_file:
	if match1 in line:
		date_time = line[0:16]
		s = line[line.rindex('user'):]
		a = s.split(' ')
		if a[1] in m1:
			if not ('vm2' in m1[a[1]]):
				m1[a[1]].append('vm2')	
				file_out = "user_login("+a[1]+",vm2).\n"
				output_file.write(file_out)
		else:	
			m1[a[1]] = ['vm2']
			file_out = "user_login("+a[1]+",vm2).\n"
			output_file.write(file_out)

output_file.close()
in_file.close()
