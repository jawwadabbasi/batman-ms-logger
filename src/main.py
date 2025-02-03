# Built with ingenuity,
# by Jawwad Abbasi (jawwad@kodelle.com)

# Initiates a Flask app to handle managed endpoints
# and relays to corresponding controller and module
# for processing.

import json
import sentry_sdk
import settings

from flask import Flask,Response,request
from v1.controller import Ctrl_v1
from v2.controller import Ctrl_v2

sentry_sdk.init(
	dsn = settings.SENTRY_DSN,
	traces_sample_rate = settings.SENTRY_TRACES_SAMPLE_RATE,
	profiles_sample_rate = settings.SENTRY_PROFILES_SAMPLE_RATE,
	environment = settings.SENTRY_ENVIRONMENT
)

app = Flask(__name__)

@app.errorhandler(404)
def RouteNotFound(e):

	return Response(None,status = 400,mimetype = 'application/json')

####################################
# Supported endpoints for API v1
####################################
@app.route('/api/v1/Service/CreateLog',methods = ['POST'])
def CreateServiceLog():

	data = Ctrl_v1.CreateServiceLog(request.json)
	return Response(json.dumps(data),status = data['ApiHttpResponse'],mimetype = 'application/json')

@app.route('/api/v1/Exception/CreateLog',methods = ['POST'])
def CreateExceptionLog():

	data = Ctrl_v1.CreateExceptionLog(request.json)
	return Response(json.dumps(data),status = data['ApiHttpResponse'],mimetype = 'application/json')

@app.route('/api/v1/Slack/SendAlert',methods = ['POST'])
def SendAlert():

	data = Ctrl_v1.SendAlert(request.json)
	return Response(json.dumps(data),status = data['ApiHttpResponse'],mimetype = 'application/json')

@app.route('/api/v1/Slack/SendFeedback',methods = ['POST'])
def SendFeedback():

	data = Ctrl_v1.SendFeedback(request.json)
	return Response(json.dumps(data),status = data['ApiHttpResponse'],mimetype = 'application/json')

@app.route('/api/v1/Telegram/SendNotification',methods = ['POST'])
def SendTelegramNotification():

	data = Ctrl_v1.SendTelegramNotification(request.json)
	return Response(json.dumps(data),status = data['ApiHttpResponse'],mimetype = 'application/json')

@app.route('/api/v1/Telegram/SendPhotoNotification',methods = ['POST'])
def SendTelegramNotificationWithPhoto():

	data = Ctrl_v1.SendTelegramNotificationWithPhoto(request.form,request.files)
	return Response(json.dumps(data),status = data['ApiHttpResponse'],mimetype = 'application/json')

####################################
# Initiate web server
####################################
app.run(host = '0.0.0.0',port = settings.FLASK_PORT,debug = settings.FLASK_DEBUG)