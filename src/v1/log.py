import json
import uuid
import settings

from datetime import timedelta
from includes.db import Db
from includes.common import Common

class Log:

	def Service(service,endpoint,request,response):

		api_data = {}
		api_data['ApiHttpResponse'] = 500
		api_data['ApiMessages'] = []
		api_data['ApiResult'] = []

		try:
			http_response = response['ApiHttpResponse']
			http_response = int(http_response)

		except:
			api_data['ApiHttpResponse'] = 400
			api_data['ApiMessages'] += ['INFO - Invalid HTTP response code']

			return api_data

		if http_response in [200,201,202,204,409]:
			api_data['ApiHttpResponse'] = 201
			api_data['ApiMessages'] += ['INFO - Request processed successfully']

			return api_data
		
		if http_response in [418,518]:
			request = Common.SantitizeConfidentialData(request)

		query = """
			INSERT INTO service_logs (
				log_id,
				service,
				endpoint,
				request,
				response,
				date
			) VALUES (
				%s,
				%s,
				%s,
				%s,
				%s,
				%s
			)
		"""

		inputs = (
			str(uuid.uuid4()),
			service,
			endpoint,
			json.dumps(request) if request else "",
			json.dumps(response) if response else "",
			str(Common.Datetime())
		)

		if Db.ExecuteQuery(query,inputs,True):
			api_data['ApiHttpResponse'] = 201
			api_data['ApiMessages'] += ['INFO - Request processed successfully']

			return api_data

		api_data['ApiHttpResponse'] = 500
		api_data['ApiMessages'] += ['ERROR - Could not create record']

		return api_data

	def Exception(service,method,exception,comments,payload):

		api_data = {}
		api_data['ApiHttpResponse'] = 500
		api_data['ApiMessages'] = []
		api_data['ApiResult'] = []

		if 'ALTER TABLE' in exception or 'ALTER TABLE' in comments:
			api_data['ApiHttpResponse'] = 201
			api_data['ApiMessages'] += ['INFO - Request processed successfully']

			return api_data

		query = """
			INSERT INTO exception_logs (
				log_id,
				service,
				method,
				exception,
				comments,
				payload,
				date
			) VALUES (
				%s,
				%s,
				%s,
				%s,
				%s,
				%s,
				%s
			)
		"""

		inputs = (
			str(uuid.uuid4()),
			service,
			method,
			exception,
			comments,
			json.dumps(payload) if payload else None,
			str(Common.Datetime())
		)

		if Db.ExecuteQuery(query,inputs,True):
			api_data['ApiHttpResponse'] = 201
			api_data['ApiMessages'] += ['INFO - Request processed successfully']

			return api_data

		api_data['ApiHttpResponse'] = 500
		api_data['ApiMessages'] += ['ERROR - Could not create record']

		return api_data

	def Purge():

		api_data = {}
		api_data['ApiHttpResponse'] = 500
		api_data['ApiMessages'] = []
		api_data['ApiResult'] = []

		inputs = (
			str(Common.DatetimeObject() - timedelta(minutes = settings.LOGGER_MAX_LOG_RETENTION)),
		)

		query = """
			DELETE FROM service_logs
			WHERE date < %s
		"""

		Db.ExecuteQuery(query,inputs,True)

		query = """
			DELETE FROM exception_logs
			WHERE date < %s
		"""

		Db.ExecuteQuery(query,inputs,True)

		api_data['ApiHttpResponse'] = 202
		api_data['ApiMessages'] += ['INFO - Request processed successfully']

		return api_data