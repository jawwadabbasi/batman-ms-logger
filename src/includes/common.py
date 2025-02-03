from datetime import datetime, timezone

class Common:

	def Date():

		return datetime.now(timezone.utc).strftime('%Y-%m-%d')

	def Datetime():

		return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

	def DateObject():

		return datetime.strptime(Common.Date(), '%Y-%m-%d')

	def DatetimeObject():

		return datetime.strptime(Common.Datetime(), '%Y-%m-%d %H:%M:%S')
	
	def SantitizeConfidentialData(data):

		if 'password' in data:
			del data['password']

		if 'Password' in data:
			del data['Password']

		if 'CurrentPassword' in data:
			del data['CurrentPassword']

		if 'currentpassword' in data:
			del data['currentpassword']

		if 'NewPassword' in data:
			del data['NewPassword']
		
		if 'newpassword' in data:
			del data['newpassword']
		
		return data