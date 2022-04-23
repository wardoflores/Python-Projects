cd /home/joey/coalemus/Python-Projects/fileorganizer/linuxfiles
while :
do
echo Put path to be organized here:
read orgdir
/bin/python organize.py $orgdir
done