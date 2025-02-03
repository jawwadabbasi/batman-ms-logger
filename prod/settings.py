# Include all global variables in this file.
# These are used across different modules/packages
# where required.

# Service Name
SVC_NAME = 'batman-ms-logger'

# DB Settings
DB_HOST_WRITER = ''
DB_HOST_READER = ''
DB_PORT = ''
DB_NAME = 'batman_logger'
DB_USER = ''
DB_PASS = ''

# Logger Settings
LOGGER_MAX_LOG_RETENTION = 2880 #minutes

# Slack Settings
SLACK_WEBHOOK_ALERTS = ''
SLACK_WEBHOOK_FEEDBACK = ''

# Sentry Settings
SENTRY_DSN = ''
SENTRY_TRACES_SAMPLE_RATE = 0.05
SENTRY_PROFILES_SAMPLE_RATE = 0.1
SENTRY_ENVIRONMENT = 'dev'

# Telegram
TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = '-'
TELEGRAM_MESSAGE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
TELEGRAM_PHOTO = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"

# Grafana
GRAFANA_USER = ''

# Flask Settings
FLASK_PORT = 80
FLASK_DEBUG = False