#!/bin/bash
OUTPUT=`service --status-all | grep ^" "  | awk '{print $2 " " $4}'`
TIME=`date`
STATUS="ACTIVE"
echo -e "\n$(printf '+%.0s' {1..15}) LOG STARTED $(printf '+%.0s' {1..15})">>service.log
for d in $OUTPUT; do
        if [[ $d == '+' ]]; then
        STATUS="ACTIVE"
        elif [[ $d == '-' ]]; then
        STATUS="INACTIVE"
        else
         echo "$d $STATUS $(date '+%Y-%m-%d %H:%M:%S')">>service.log
        fi
done
echo -e "$(printf '+%.0s' {1..15}) LOG ENDED $(printf '+%.0s' {1..15})\n">>service.log





