import os 
import re
import getpass
import datetime

currentDT = datetime.datetime.now()

username = getpass.getuser()

in_file = open("file_mon.txt","r")
output_file = open("/home/prasad/Desktop/btp/en_file/file_data_"+str(currentDT.hour)+":"+str(currentDT.minute)+".pl","w+")

file1 = "ssy"
file2 = "/var/log/syslog"

m1 = {}

for line in in_file:
	if ("ftrace_hook" in line) and ((file1 in line) or (file2 in line)):
		a = line.split(' ')
		cmd = a[4].split('(')
		file_dir = a[4].split(',')
		file_name = file_dir[1].split('/')
		name = file_name[len(file_name)-1]		
		if name in m1:	
			if not(cmd[0] in m1[name]):
				m1[name].append(cmd[0])
				file_output = 'file_mon('+name+','+cmd[0]+','+username+',vm2).\n'
				output_file.write(file_output)			
		else:	
			m1[name] = [cmd[0]]	
			file_output = 'file_mon('+name+','+cmd[0]+','+username+',vm2).\n'
			output_file.write(file_output)

output_file.close()
in_file.close()	
	    
	    
		






