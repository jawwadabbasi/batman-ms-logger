# batman-ms-logger

## Overview
**batman-ms-logger** is a centralized logging microservice responsible for capturing exceptions, bad requests, and other critical logs. It stores all logs in a database for historical tracking and integrates with **Slack** and **Telegram** to provide real-time alerts when critical events occur.

## Features
- **Centralized Logging**: Captures bad requests, API errors, and exceptions across microservices.
- **Database Storage**: Logs are persisted for later analysis and debugging.
- **Real-time Alerts**: Integrates with Slack and Telegram to notify teams instantly when critical issues arise.
- **Easy Integration**: Designed to be plugged into any microservice for quick logging and monitoring.

## How It Works
Whenever a bad request or an exception is encountered in any microservice, a request is sent to **batman-ms-logger** with relevant details. The service processes the log, stores it in the database, and, if necessary, triggers alerts to **Slack** and **Telegram**.


### Example Slack Alert
```
🚨 *[ERROR]* batman-ms-orchestrator
❌ Message: Failed to process workflow sequence
🔍 Exception: KeyError: 'task_id'
📅 Timestamp: 2025-02-02 14:55 UTC
```

## Integration with Other Services
- **batman-ms-orchestrator**: Sends workflow execution failures.
- **batman-ms-stripe**: Reports failed payment transactions.
- **batman-ms-broadcast**: Logs failed email or webhook notifications.
- **batman-ms-crons**: Captures job failures or timeout issues.

## Setting Up Notifications
To receive alerts via **Slack**, configure a webhook URL in the environment variables:
```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

For **Telegram**, provide the bot API token and chat ID:
```env
TELEGRAM_BOT_TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ
TELEGRAM_CHAT_ID=-1001234567890
```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/v1/Service/CreateLog` | Logs bad requests |
| POST | `/api/v1/Exception/CreateLog` | Logs exceptions |


## Conclusion
**batman-ms-logger** ensures that critical issues are captured, stored, and reported instantly. It provides visibility into microservice health, allowing teams to react quickly and efficiently to failures.

_As Batman always says, 'The night is darkest before the dawn'—but with real-time logging, we see the light before trouble arises!_ 🦇

