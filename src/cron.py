import sys

from v1.log import Log

class Cron:

	def __init__(self):

		try:
			job = sys.argv[1]

		except:
			sys.exit('ERROR - No job specified')

		if job == 'purge-logs':
			result = Log.Purge()

		else:
			sys.exit('ERROR - Unsupported job')

		if result['ApiHttpResponse'] == 500:
			sys.exit('ERROR - Job failed')

		sys.exit()

try:
	Cron()

except Exception as e:
	sys.exit(e)