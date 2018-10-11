import os 
import re

m1 = {}

'''
output_file = open("/home/prasad/Desktop/btp/test2/service-logging/service_data.pl","r")

for line in output_file:
	if 'service_mon' in line:
		name = line.split(',')
		ser_name = name[0].split('(')
		ser_state = name[1].split(')')
		if ser_name[1] in m1:		
			if not(ser_state[0].lower() in m1[ser_name[1]]):
				m1[ser_name[1]].append(ser_state[0].lower())							
		else:
			m1[ser_name[1]] = [ser_state[0].lower()]
	else: 
		break
	
output_file.close()
'''

output_file = open("service_knowledgebase.txt","r")
knowledge_base = output_file.readlines()
output_file.close()

in_file = open("service.log","r")
output_file = open("service_data.pl","w+")

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

output_file.write('\n')
output_file.writelines(knowledge_base)	
output_file.close()
in_file.close()	
	    
		






