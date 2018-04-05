echo $1 $3 $2 > errors.txt
for i in $(seq $1 $3 $2);
do
    python generate_input.py --output graph_data;
    $4 < graph_data.in > tested_data.out
    diff graph_data.out tested_data.out >> errors.txt
    echo -ne "\t$i/$2\r";
done
echo -e "Done!                          \r";
