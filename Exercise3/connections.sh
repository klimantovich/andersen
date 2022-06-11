#!/bin/bash

VERBOSE=false
NUMBERS=false

while [[ $# -gt 0 ]]; do
  case $1 in
    -v|--verbose)
      VERBOSE=true
      shift # past argument
      ;;
    -c|--count)
      NUMBERS=true
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

sudo netstat -tunapl | awk -v proc=$PROCESS '$0 ~ proc {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n5 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F':' '/^Organization/ {print $2}' ; done

