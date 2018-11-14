#!/usr/bin/env python3
import os

#start = input("Enter start time")
#end = input("Enter end time")

start = '10:20'
end = '12:40'

start = start.split(':')
end = end.split(':')

files_dir = []

for filename in os.listdir('/home/prasad/Desktop/btp/decrypted/file_data'):                        
    file_time = filename.split('_')
    time = file_time[2]
    time = time[0:5]
    time = time.split(':')
    if(int(start[0])<=int(time[0]) and int(start[1])<=int(time[1]) and int(end[0])>=int(time[0]) and int(end[1])>=int(time[1])): 
    	files_dir.append('decrypted/file_data/'+filename)

output_file = open("/home/prasad/Desktop/btp/file_data.pl","w+")

for files in files_dir:
	input_file = open(files,"r")
	knowledge_base = input_file.readlines()
	output_file.writelines(knowledge_base) 
	input_file.close()

input_file = open("file_knowledgebase.txt","r")
knowledge_base = input_file.readlines()
output_file.writelines('\n')
output_file.writelines(knowledge_base)
output_file.close()
files_dir.clear()

for filename in os.listdir('/home/prasad/Desktop/btp/decrypted/login_data'):                        
    file_time = filename.split('_')
    time = file_time[2]
    time = time[0:5]
    time = time.split(':')
    if(int(start[0])<=int(time[0]) and int(start[1])<=int(time[1]) and int(end[0])>=int(time[0]) and int(end[1])>=int(time[1])): 
    	files_dir.append('decrypted/login_data/'+filename)

output_file = open("/home/prasad/Desktop/btp/login_data.pl","w+")

for files in files_dir:
	input_file = open(files,"r")
	knowledge_base = input_file.readlines()
	output_file.writelines(knowledge_base) 
	input_file.close()

input_file = open("login_knowledgebase.txt","r")
knowledge_base = input_file.readlines()
output_file.writelines('\n')
output_file.writelines(knowledge_base)
output_file.close()
files_dir.clear()

for filename in os.listdir('/home/prasad/Desktop/btp/decrypted/service_data'):                        
    file_time = filename.split('_')
    time = file_time[2]
    time = time[0:5]
    time = time.split(':')
    if(int(start[0])<=int(time[0]) and int(start[1])<=int(time[1]) and int(end[0])>=int(time[0]) and int(end[1])>=int(time[1])): 
    	files_dir.append('decrypted/service_data/'+filename)

output_file = open("/home/prasad/Desktop/btp/service_data.pl","w+")

for files in files_dir:
	input_file = open(files,"r")
	knowledge_base = input_file.readlines()
	output_file.writelines(knowledge_base) 
	input_file.close()

input_file = open("service_knowledgebase.txt","r")
knowledge_base = input_file.readlines()
output_file.writelines('\n')
output_file.writelines(knowledge_base)
output_file.close()




