#
#!/bin/bash


LOW_YEAR=$1
HI_YEAR=$2

for i in `seq $LOW_YEAR 1 $HI_YEAR`;
do 
	echo "Getting data for FIFA"$i
	python3 mycrawler.py $i
done
