echo $1 $3 $2 > timedata.txt
for i in $(seq $1 $3 $2);
do
    python generate_input.py --output -o graph_data;
    time_old=$(date +%s%N)
    $4 < graph_data.in > graph_data.out
    time_new=$(date +%s%N)
    let timediff=time_new-time_old
    (echo $i $timediff >> timedata.txt)
    echo -ne "\t$i/$2\r";
done
echo -e "Done!                          \r";
