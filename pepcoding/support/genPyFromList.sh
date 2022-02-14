size=`wc -l $1|colrm 2`
echo $size
for (( i=0; i<$size; i++ )) 
do
	name=`sed -n "$((i+1)) p" $1`;
	fileName="P${i}_$name"
	fileName=`echo "$fileName"|grep -o '\w*'`
	cat /home/abhishekpowar/Desktop/Desktop14/PepCoding/support/temp.text > "$fileName.py";
done
