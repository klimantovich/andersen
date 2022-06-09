1. sudo apt update & upgrade
2. mkdir /var/www/flask-app
3. install apache & libapache2-mod-wsgi-py3
4. install python3-pip
5. mv flask_app to remote server
6. pip3-install -r requirements.txt
7. mv flask_app.conf to /etc/apache2/sites-aviable
8. a2dissite 000-default
9. a2ensite flask_app
10. systemctl restart
