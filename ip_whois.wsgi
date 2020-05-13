#!/user/bin/python3

import sys, logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/ip_whois/")

from ip_whois import app as application