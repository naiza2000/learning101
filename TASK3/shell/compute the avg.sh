read l
sum=0
for ((i=1; i<=l; i=i+1))
do
read x
sum=`expr $sum + $x`
done
printf "%.3f\n" ` echo $sum / $l  | bc -l`