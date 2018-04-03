echo "" > data.txt
for i in "seq $1 $3 $2";
do
    python gen_data.py --output graph_data;
    (time ($4 graph_data.in > graph_data.out)) >> data.txt
done
rm graph_data.in graph_data.out
