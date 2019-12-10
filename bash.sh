count=104
while true
do 
    python -u "/home/master/Desktop/Python-Nuu/code.py"
    python -u "/home/master/Desktop/Python-Nuu/get_Img.py" $count
    (( count+=4 ))
done