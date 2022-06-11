#!/bin/bash

VERBOSE=false
COUNT=false

while [ $# -gt 0 ]; do
  case $1 in
    -v|--verbose)
      VERBOSE=true
      shift # past argument
      ;;
    -c|--count)
      COUNT=true
      shift # past argument
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      PROCESS=$1
      shift # past argument
      ;;
  esac
done

if [ -z $PROCESS ]; then
  echo "    usage: connections.sh [-v --verbose] [-c --count] process_name|PID"
  exit 1
fi

get_connection_info () {
  if $VERBOSE; then	  
    whois $IP | awk -F':' '/^Organization/ {print $2} /^CIDR/ {print $2} /^NetName/ {print $2}' | sed s/' '//g
  else
    whois $IP | awk -F':' '/^Organization/ {print $2}' | sed s/' '//g
  fi
}

#add all connections to array all_connections
all_connections=( $(sudo netstat -tunapl | awk -v proc=$PROCESS '$0 ~ proc {print $5}' | cut -d: -f1) )
#get unique ip addresses from list all_connections
ip_addresses=($(for ip in "${all_connections[@]}"; do echo "${ip}"; done | sort -u))

#get info from whois. Based in $VERBOSE variable
for IP in ${ip_addresses[*]}
do
    get_connection_info
done

