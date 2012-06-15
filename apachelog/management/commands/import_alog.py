import re
from django.core.management import BaseCommand
from datetime import datetime

# Ripped from http://www.seehuhn.de/blog/52
# Edit According to your log format
from apachelog.models import Log

LOG_FORMAT_PARTS = [
	r'(?P<host>\S+)',                   # host %h
	r'\S+',                             # indent %l (unused)
	r'(?P<user>\S+)',                   # user %u
	r'\[(?P<time>.+)\]',                # time %t
	r'"(?P<request>.+)"',               # request "%r"
	r'(?P<status>[0-9]+)',              # status %>s
	r'(?P<size>\S+)',                   # size %b (careful, can be '-')
	r'"(?P<referer>.*)"',               # referer "%{Referer}i"
	r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
LOG_PATTERN = re.compile(r'\s+'.join(LOG_FORMAT_PARTS)+r'\s*\Z')


def test_regex():
	line = '8.28.16.254 - - [12/Jun/2012:09:50:01 -0400] "GET /facebook.html HTTP/1.1" 200 664 "-" "Mozilla/4.0 (compatible;)"'
	matches = LOG_PATTERN.match(line)
	results = matches.groupdict()
	print results

def parse_line(line):
	matches = LOG_PATTERN.match(line)
	results = matches.groupdict()

	# Fix size to int
	if results['size']=='-':
		results['size']==0
	else:
		results['size']==int(results['size'])

	results["status"] = int(results["status"])

	# referer and user can also give -
	time = datetime.strptime(results['time'][:-6],'%d/%b/%Y:%H:%M:%S')
	utc_offset = int(results['time'][-5:])/100
	results['time']=time
	results['utc_offset']=utc_offset

	log = Log(**results)
	log.save()

class Command(BaseCommand):
	"""
	Any future timezone programme should use django 1.4 with its good TimeZone support (USE_TZ = True)
/	"""
	def handle(self, *args, **options):
		"""

		"""
		file_path = args[0]
		print "Appending new logs to database"
		file_path = args[0]
		file = open(file_path)
		for index, line  in enumerate(iter(file)):
			parse_line(line)
		print 'Appended %s new records'%index
