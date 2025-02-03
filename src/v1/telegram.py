import requests
import settings

from werkzeug.datastructures import FileStorage

class Telegram:

    def SendNotification(message):

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        try:
            message = str(message)

        except:
            api_data['ApiHttpResponse'] = 500
            api_data['ApiMessages'] += ['ERROR - Invalid Arguments']

            return api_data
        
        data = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }

        result = requests.post(f'{settings.TELEGRAM_MESSAGE}',json = data,stream = True)

        if result.ok:
            api_data['ApiHttpResponse'] = 201
            api_data['ApiMessages'] += ['INFO - Request processed successfully']

            return api_data

        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] += ['ERROR - Could not send notification']

        return api_data
    
    def SendNotificationWithPhoto(image,caption=False):

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        if not isinstance(image, FileStorage):
            api_data['ApiHttpResponse'] = 500
            api_data['ApiMessages'] += ['ERROR - Invalid Arguments']

            return api_data
        
        files = {'photo': image}
        
        data = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'caption': caption if caption else False,
            'parse_mode': 'HTML'
        }

        result = requests.post(f'{settings.TELEGRAM_PHOTO}',data=data, files=files)

        if result.ok:
            api_data['ApiHttpResponse'] = 201
            api_data['ApiMessages'] += ['INFO - Request processed successfully']

            return api_data

        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] += ['ERROR - Could not send notification with photo']

        return api_data