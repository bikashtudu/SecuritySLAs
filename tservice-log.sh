#!/bin/bash
echo -e "\n$(printf '+%.0s' {1..15}) LOG STARTED $(printf '+%.0s' {1..15})">>nservice.log
data=`service --status-all | grep ^" "  | awk '{"date +%Y-%m-%d,%H:%M:%S" | getline Time;if($2 == "+"){$2 = "ACTIVE"}else{$2 = "INACTIVE"}printf  $4 " " $2 " " Time"\n"}'`
echo "$data">>nservice.log
echo -e "$(printf '+%.0s' {1..15}) LOG ENDED $(printf '+%.0s' {1..15})\n">>nservice.log
