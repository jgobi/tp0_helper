echo $1 $3 $2 > timedata.txt
for i in $(seq $1 $3 $2);
do
    python gen_data.py --output graph_data;
    time_old=$(date +%s%N)
    $4 graph_data.in > graph_data.out
    time_new=$(date +%s%N)
    let timediff=time_new-time_old
    echo $i $timediff
    (echo $i $timediff >> timedata.txt)
done
