echo#!/bin/bash


#https://stackoverflow.com/a/23634080
function make_scientific_progress() {
echo "-----------------------------"
for ((k = 0; k <= 10 ; k++))
do
    echo -n "[ "
    for ((i = 0 ; i <= k; i++)); do echo -n "###"; done
    for ((j = i ; j <= 10 ; j++)); do echo -n "   "; done
    v=$((k * 10))
    echo -n " ] "
    echo -n "$v %" $'\r'
    sleep 0.05
done
echo ""
}

echo "___BEGIN SCIENCE_____________"
echo "Cleanupifying data directory..."
make_scientific_progress

rm counts.*.csv
rm *.seq 
#rm *.whatever

echo "Enstringinating nucleotide pairs..."
make_scientific_progress
for i in {1..5}; do
    python3 SequenceGenerator.py &> /dev/null
done

echo "Enfoldifying string sequences..."
make_scientific_progress
for i in *.seq; do # Whitespace-safe but not recursive.
    RNAfold < "$i" >> $i.whatever
done

RATIO_TOTAL=0
FILECOUNT=0

echo "Calculating parenthetization factor..."
make_scientific_progress
for i in *.whatever; do
    CHARACTERS="$(tail -n +2 $i | tr -d '\n' | wc -c)"
    GC="$(echo $i | cut -d'.' -f5 )"
    RUN="$(echo $i | cut -d'.' -f2 )"
    SEQ="$(echo $i | cut -d'.' -f3 )"
#    echo "run: $RUN series: $SEQ GC richness: $GC"
    DOTS="$(fgrep -o . $i | wc -l)"
#    echo "$i data || Dots: $DOTS || Characters: $CHARACTERS"
    FILELINE=$(echo "$SEQ,$GC,$DOTS,$CHARACTERS")
    CLEANLINE=$(echo ${FILELINE//[[:blank:]]/})
    FILENAME=counts.csv
    echo "$CLEANLINE" >> $FILENAME
done

echo "Enprintening test run statistics"
cat counts.csv

echo "Sciencing results"
python3 ProcessResults.py

echo "-------SCIENCE TERMINATED---------"
