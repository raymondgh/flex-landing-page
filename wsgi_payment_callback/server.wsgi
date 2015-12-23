# mod_wsgi

import sys, os

sys.path.insert(0, '/var/www/wsgi_payment_callback')

os.chdir('/var/www/wsgi_payment_callback')

from payment import app as application