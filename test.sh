name1='{"draw_roi_area": false, "draw_result": true}'

n="./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/dynamiv_res/$name.jpg -a '$name1'"
cmd=`$n`
echo $cmd
echo $n