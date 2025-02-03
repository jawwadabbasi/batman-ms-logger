import inspect
import json

from v1.log import Log
from v1.slack import Slack
from v1.telegram import Telegram

class Ctrl_v1:

	def Response(endpoint,request_data = None,api_data = None,log = True):

		return api_data

	def BadRequest(endpoint,request_data = None):

		api_data = {}
		api_data['ApiHttpResponse'] = 400
		api_data['ApiMessages'] = ['INFO - Missing required parameters']
		api_data['ApiResult'] = []

		return api_data

	def CreateServiceLog(request_data):

		if (not request_data.get('Service')
			or not request_data.get('Endpoint')
			or not request_data.get('Request')
			or not request_data.get('Response')
		):
			return Ctrl_v1.BadRequest(inspect.stack()[0][3],request_data)

		api_data = Log.Service(
			request_data.get('Service'),
			request_data.get('Endpoint'),
			request_data.get('Request'),
			request_data.get('Response')
		)

		return Ctrl_v1.Response(inspect.stack()[0][3],request_data,api_data)

	def CreateExceptionLog(request_data):

		if (not request_data.get('Service')
			or not request_data.get('Method')
		):
			return Ctrl_v1.BadRequest(inspect.stack()[0][3],request_data)

		api_data = Log.Exception(
			request_data.get('Service'),
			request_data.get('Method'),
			request_data.get('Exception',None),
			request_data.get('Comments',None),
			request_data.get('Payload',None)
		)

		return Ctrl_v1.Response(inspect.stack()[0][3],request_data,api_data)

	def SendAlert(request_data):

		if (not request_data.get('Service')
			or not request_data.get('Method')		
			or not request_data.get('Message')		
		):
			return Ctrl_v1.BadRequest(inspect.stack()[0][3],request_data)

		api_data = Slack.Alert(
			request_data.get('Service'),
			request_data.get('Method'),
			request_data.get('Message')
		)

		return Ctrl_v1.Response(inspect.stack()[0][3],request_data,api_data)

	def SendFeedback(request_data):

		if (not request_data.get('UserId')
			or not request_data.get('UserStatus')	
			or not request_data.get('Rating')
		):
			return Ctrl_v1.BadRequest(inspect.stack()[0][3],request_data)

		api_data = Slack.Feedback(
			request_data.get('UserId'),
			request_data.get('UserStatus'),
			request_data.get('Rating'),
			request_data.get('FeedbackType', False),
			request_data.get('Feedback', False)
		)

		return Ctrl_v1.Response(inspect.stack()[0][3],request_data,api_data)
	
	def SendTelegramNotification(request_data):

		if (not request_data.get('Message')):
			return Ctrl_v1.BadRequest(inspect.stack()[0][3],request_data)

		api_data = Telegram.SendNotification(
			request_data.get('Message')
		)

		return Ctrl_v1.Response(inspect.stack()[0][3],request_data,api_data)
	
	def SendTelegramNotificationWithPhoto(request_data,file_data):

		if (not file_data.get('Image')):
			return Ctrl_v1.BadRequest(inspect.stack()[0][3],request_data)
		
		payload_data = json.loads(request_data.get('Payload', '{}'))

		api_data = Telegram.SendNotificationWithPhoto(
			file_data.get('Image'),
			payload_data.get('Caption', False)
		)

		return Ctrl_v1.Response(inspect.stack()[0][3],request_data,api_data)