from datetime import datetime
import gzip
import base64


class Utils:
    def get_zoned_date_time():
        today = datetime.now()
        zonedDateTime = today.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'
        return zonedDateTime

    def compress(request):
         return gzip.compress(bytes(request))
    
    def decompress(request):
        return gzip.decompress(request)
    
    def base64_encode(message):
        return base64.b64encode(message)
    
    def base64_decode(message):
        return base64.b64decode(message)  

    def decode(message):
        return message.decode("utf-8")