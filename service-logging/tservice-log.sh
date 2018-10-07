#!/bin/bash
while true
do
	oldtimestamp=`date +"%Y%m0%d%H%M%S"`
	newtimestamp=$(( $oldtimestamp + 1000 ))
	log_fine="service_$oldtimestamp"
	while [ $oldtimestamp -le $newtimestamp ]
	do	
		echo -e "\n$(printf '+%.0s' {1..15}) LOG STARTED $(printf '+%.0s' {1..15})">> ${log_fine}.log
		data=`service --status-all | grep ^" "  | awk '{"date +%Y-%m-%d,%H:%M:%S" | getline Time;if($2 == "+"){$2 = "ACTIVE"}else{$2 = "INACTIVE"}printf  $4 " " $2 " " Time"\n"}'`
		echo "$data">>${log_fine}.log
		echo -e "$(printf '+%.0s' {1..15}) LOG ENDED $(printf '+%.0s' {1..15})\n">>${log_fine}.log
		oldtimestamp=`date +"%Y%m0%d%H%M%S"`
	done
	echo "$oldtimestamp">>service_timestamp
done
