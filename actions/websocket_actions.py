import websocket
import ssl
import os
import json

ws = None
webSocketUrl = None


class WebsocketActions:
    global webSocketUrl
    folder = os.getcwd()
    f = open(folder + '\\resources\\config.json', 'rt')
    data = json.load(f)
    webSocketUrl = data["appConfig"]["socketType"] + data["appConfig"]["serviceFabricURL"]
    websocket.enableTrace(True)

    @staticmethod
    def create_connection():
        global ws
        websocket.enableTrace(True)
        ws = websocket.create_connection(webSocketUrl)
        return ws

    @staticmethod
    def add_sub_protocol():
        global ws
        websocket.enableTrace(True)
        ws = websocket.create_connection("wss://mendoza.slots.qa.intelligentgamingsystems.com:19081/Asajj/VentressService?ENTITY=1.492&TYPE=Device",subprotocols=["XmlGzip.Queuing.Ventress.IntelligentGaming.net"])
        return ws

    @staticmethod
    def send(message):
        return ws.send(message)

    @staticmethod
    def receive():
        return ws.recv()

    @staticmethod
    def close():
        ws.close()

    @staticmethod
    def create_ssl_certificate():
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context