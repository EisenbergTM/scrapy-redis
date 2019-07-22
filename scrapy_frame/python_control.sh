#!/bin/bash  

command="python3 redis_push.py"

status="./.status/redis_push.py"

start() {
    if [ ! -d "$status" ]; then
        mkdir -p "$status"
    fi  
    echo "starting: $command"
    /mnt/work/xtwang/daemontools/supervise -p "$status" -f "$command" > /dev/null 2>&1
}


stop() {
    if [ ! -d "$status" ]; then
        mkdir -p "$status"
    fi  
    pid=`ps -ef|grep "python3 redis_push.py" |grep -v grep|grep python3.6|awk '{print $2}'`
    echo "stoping: $command;  pid=$pid"
    if [ -n "$pid" ]; then
	kill -9 $pid
    fi	
#    pgrep log_server > /dev/null && echo d > "$status/control" && echo x > "$status/control"
    # FIXME
}


restart() {
    stop
    start
}


case "$1" in

start)
    start
    ;;  

stop)
    stop
    ;;  

restart)
    restart
    ;;  
*)

echo "Usage: $0 [start | stop | restart]"

exit 1

esac
