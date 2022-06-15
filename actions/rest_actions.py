import os
import requests
import json

response = None
statusCode = None
request = None


class RestActions:
    folder = os.getcwd()
    f = open(folder + '\\resources\\config.json', 'rt')
    data = json.load(f)
    apiBaseUrl = data["appConfig"]["baseURL"]
    global response, statusCode

    @staticmethod
    def open_rest_client():
        global request
        request = requests
        return request

    @staticmethod
    def get(url, headers):
        return request.get(url, headers=headers)

    @staticmethod
    def post(url, data, headers):
        return request.post(url, json=data, headers=headers)

    @staticmethod
    def put(url, data, headers):
        return request.put(url, json=data, headers=headers)

    @staticmethod
    def patch(url, data, headers):
        return request.patch(url, json=data, headers=headers)

    @staticmethod
    def delete(url, headers):
        return request.delete(url, headers=headers)
