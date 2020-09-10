#/bin/bash

main_free_num1(){
cd /usr/local/ev_sdk/bin
./test-ji-api -f 1 -i /zhengzhong/1.jpg -r 1000000
}

main_free_num5(){
cd /usr/local/ev_sdk/bin
./test-ji-api -f 5 -i /zhengzhong/1.jpg -r 1000000
}
$1