import requests
import settings

class Slack:

    def Prepare(string):

        string = str.replace(string,'&','&amp;')
        string = str.replace(string,'<','&lt;')
        string = str.replace(string,'>','&gt;')

        return string

    def Alert(service,method,message):

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        try:
            service = str(service)
            method = str(method)
            message = str(message)

        except:
            api_data['ApiHttpResponse'] = 500
            api_data['ApiMessages'] += ['ERROR - Could not parse inputs as string']

            return api_data
        
        data = {
			'blocks': [
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '*Service:* ' + service
                    }
                },
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '*Method:* ' + method
                    }
                },
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '>' + Slack.Prepare(message)
                    }
                }
            ]
        }

        result = requests.post(f'{settings.SLACK_WEBHOOK_ALERTS}',json = data,stream = True)

        if result.status_code == 200:
            api_data['ApiHttpResponse'] = 201
            api_data['ApiMessages'] += ['INFO - Request processed successfully']

            return api_data

        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] += ['ERROR - Could not send alert']

        return api_data

    def Feedback(user_id,user_status,rating,feedback_type=False,feedback=False):

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        try:
            user_id = str(user_id)
            user_status = str(user_status)
            rating = str(rating)

        except:
            api_data['ApiHttpResponse'] = 500
            api_data['ApiMessages'] += ['ERROR - Could not parse inputs as string']

            return api_data
        
        feedback_type = str(feedback_type) if feedback_type else 'None'
        feedback = str(feedback) if feedback else 'None'

        rating = (rating + ' :fire:') if rating.lower() == 'excellent' else rating
        rating = (rating + ' :+1:') if rating.lower() == 'good' else rating
        rating = (rating + ' :neutral_face:') if rating.lower() == 'fair' else rating
        rating = (rating + ' :disappointed:') if rating.lower() == 'bad' else rating
        rating = (rating + ' :rage:') if rating.lower() == 'horrible' else rating
        
        data = {
			'blocks': [
				{
					'type': 'header',
					'text': {
						'type': 'plain_text',
						'text': rating.capitalize(),
						'emoji': True
                    }
                },
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '*UserId:* ' + user_id
                    }
                },
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '*User Status:* ' + user_status
                    }
                },
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '*Feedback Type:* ' + feedback_type.capitalize()
                    }
                },
				{
					'type': 'section',
					'text': {
						'type': 'mrkdwn',
						'text': '>' + Slack.Prepare(feedback)
                    }
                },
                {
                    'type': 'divider'
                }
            ]
        }

        result = requests.post(f'{settings.SLACK_WEBHOOK_FEEDBACK}',json = data,stream = True)

        if result.status_code == 200:
            api_data['ApiHttpResponse'] = 201
            api_data['ApiMessages'] += ['INFO - Request processed successfully']

            return api_data

        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] += ['ERROR - Could not send alert']

        return api_data