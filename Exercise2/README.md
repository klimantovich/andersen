
ansible-playbook -bK ./deploy_server_playbook.yaml

1. sudo apt update & upgrade
2. install apache & libapache2-mod-wsgi-py3
3. install python3-pip
4. mv flask_app to remote server
5. pip3-install -r requirements.txt
6. mv flask_app.conf to /etc/apache2/sites-aviable
7. a2dissite 000-default
8. a2ensite flask_app
9. systemctl restart
