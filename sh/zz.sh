#/bin/bash
#name=${cmd#*\{} #从左向右截取第一个 src 后的字符串
#n1=${name%\}*}#从右向左截取第一个 src 后的字符串
ev_license_version=20.1.3
project_path="/usr/local/ev_sdk/"
verification_private_path="/usr/local/ev_sdk/authorization/privateKey.pem"
verification_pub_path="/usr/local/ev_sdk/authorization/pubKey.pem"
algo_config_path="/usr/local/ev_sdk/config/algo_config.json"
algo_readme_path="/usr/local/ev_sdk/config/README"
free_code1="main_free_num1"
free_code2="main_free_num5"
name=$2
name1=$3

#未实现的返回-999
main_not_function(){
cd /usr/local/ev_sdk/bin
code=`./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1`
res=`echo $code |grep -e "-999"`
if [[ $res == "" ]];then
    echo "授权失败返回-999没问题"
else
    echo "授权失败返回-999未实现"
fi
}

#授权
main_yes_function(){
if [ -e /usr/local/ev_sdk/bin/test-ji-api ]; then
    cp /usr/local/ev_sdk/3rd/license/bin/ev_license /usr/local/ev_sdk/authorization
    cd /usr/local/ev_sdk/authorization
    chmod +x ev_license
    ./ev_license -r r.txt
    ./ev_license -l privateKey.pem r.txt license.txt
    cp license.txt /usr/local/ev_sdk/bin
    cp /usr/local/ev_sdk/config/algo_config.json /zhengzhong/config
    echo "授权成功"
fi
}

#ev_license版本一致
main_ev_license(){
res=`cat /usr/local/ev_sdk/3rd/license/lib/pkgconfig/ji_license.pc |grep Version|awk '{print $2}' 2>&1`
if [[ $res == $ev_license_version ]];then
    echo "版本一致"
else
    echo "版本不一致"
fi
}

# 验证工程路径与规范一致
main_project_path(){
if [[ -d $project_path ]];then
    echo "工程路径一致"
else
    echo "工程路径与规范不一致"
fi
}

#验证test.cpp和makefile
main_make_file(){
rm -rf /usr/local/ev_sdk/test/* && cp /zhengzhong/sdk3_0/* /usr/local/ev_sdk/test/
code=`cd /usr/local/ev_sdk/test && make clean && make -j8 2>&1`
res=`echo $code |grep -e "err"`
if [[ $res == "" ]];then
    echo "test.cpp和makefile没问题"
else
    echo "test.cpp和makefile编译失败"
fi
}

# test-ji-api和license.txt移动到任意目录，都需要能够正常运行目录
main_catalogue(){
cp /usr/local/ev_sdk/bin/test-ji-api /root/ && cp /usr/local/ev_sdk/bin/license.txt /root/ && cd /root
code=`./test-ji-api -f 1 -i /zhengzhong/1.jpg 2>&1`
res=`echo $code |grep -e "return 0"`
if [[ $res == "" ]];then
    echo "移动到任意目录运行失败"
else
    echo "移动到任意目录没问题"
fi
}

#libjo.so链接所有库
main_libji_connect(){
res=`ldd /usr/local/ev_sdk/lib/libji.so|grep not 2>&1`
if [[ $res == "" ]];then
    echo "libji.so链接所有库没问题"
else
    echo "libji.so链接所有库失败"
fi
}

#实现的接口测试
main_function(){
cd /usr/local/ev_sdk/bin/
cmd=`./test-ji-api -f $name -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1`
res=`echo $cmd |grep -e "return 0"`
if [[ $res == "" ]];then
    echo "未实现接口$name"
else
    echo "已实现接口$name"
fi
}

# 公私钥位置，名称验证
main_verification_pem(){
if [[ -f $verification_private_path ]];then
    if [[ -f $verification_pub_path ]];then
        echo "公私钥名称OK"
    else
        echo "公私钥名称ERROR"
    fi
fi
}


#接口1测试内存显存泄露
main_free_num1(){
cd /zhengzhong/sh
nohup bash free_num.sh $free_code1 &
sleep 5
}
#接口5测试内存显存泄露
main_free_num5(){
cd /zhengzhong/sh
nohup bash free_num.sh $free_code2 &
sleep 5
}

main_run_sdk(){
cd /usr/local/ev_sdk/bin/
cmd=`./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res_jpg/$name.jpg 2>&1`
res=`echo $cmd |grep -e "return 0"`
if [[ $res == "" ]];then
    echo $name"图片保存失败"
else
    echo $name"图片保存成功"
fi
}

main_run_sdk_dynamiv(){
cd /usr/local/ev_sdk/bin/
cmd=`./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/dynamiv_res/$name.jpg -a '$name1' 2>&1`
res=`echo $cmd |grep -e "return 0"`
if [[ $res == "" ]];then
    echo $name"图片保存失败"
else
    echo $name"图片保存成功"
fi
}



$1
