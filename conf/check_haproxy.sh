#!/bin/bash

#检测haproxy进程是否存在
if [ `ps -C haproxy --no-header | wc -l ` -eq 0 ];then
    #不存在尝试启动haproxy
    service haproxy start
    sleep 3
    #再次检测haproxy进程是否存在
    if [ `ps -C haproxy --no-header | wc -l ` -eq 0 ];then
        #如果还没进程停止keepalived进程，VIP绑定到备机提供服务
        service keepalived stop
    fi

fi
