cd /home/joey/Joey-Repositories/Python-Projects/fileorganizer/linuxfiles
while :
do
echo Put path to be organized here:
read orgdir
/bin/python organize.py $orgdir
done