# The WSGI file used by Apache to run Flask app

import logging, sys
# Logging can found in /var/log/apache2/error.log, specificed in the conf file above.
# /var/log/apache2 is the default global variable.
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/flask_app/app.py')


from app import app as application
