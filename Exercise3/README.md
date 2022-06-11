SOURCE:
sudo netstat -tunapl | awk '/firefox/ {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n5 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F':' '/^Organization/ {print $2}' ; done

Скрипт выводит список названий организаций, которым принадлежат IP-адреса, которые подключены к определенному процессу на машине, на которой запущен скрипт (название процесса либо его PID передается как аргумент скрипта).

