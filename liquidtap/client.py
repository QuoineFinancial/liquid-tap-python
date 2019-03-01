import logging

from .pysher.pusher import Pusher
from .pysher.channel import Channel
from .utils import createJWT

class Client(object):
    def __init__(self, tokenId=None, tokenSecret=None, secure=True, secret="", user_data=None, log_level=logging.INFO,
                 daemon=True, port=443, reconnect_interval=10, custom_host="tap.liquid.com", auto_sub=False,
                 http_proxy_host="", http_proxy_port=0, http_no_proxy=None, http_proxy_auth=None):

        self.pusher = Pusher('PythonClient', secure=secure, secret=secret, user_data=user_data, log_level=log_level,
                 daemon=daemon, port=port, reconnect_interval=reconnect_interval, custom_host=custom_host, auto_sub=auto_sub,
                 http_proxy_host=http_proxy_host, http_proxy_port=http_proxy_port, http_no_proxy=http_no_proxy, http_proxy_auth=http_proxy_auth)

        self.authenticating = False
        self.authenticated = False
        self.send_buffer = []
        if (tokenId != None and tokenSecret != None):
            self.authenticate(tokenId, tokenSecret)
        self.pusher.connection.bind('pusher:connection_established', self.handle_connected)
        self.pusher.connection.bind('quoine:auth_success', self.handle_auth_success)


    def connected(self):
        return self.pusher.connection.state == 'connected'

    def send_event(self, event, data, channel=None):
        if (self.connected()):
            return self.pusher.connection.send_event(event, data)
        else:
            self.send_buffer.append({
                'event': event,
                'data': data,
                'channel': channel
            })
        return None

    def _send_all_waiting(self):
        for message in self.send_buffer:
            self.pusher.connection.send_event(message['event'], message['data'], message['channel'])

    def authenticate(self, tokenId, tokenSecret):
        self.authenticating = True

  
        auth_payload = {
            'path': '/realtime',
            'headers': {
                'X-Quoine-Auth': createJWT(tokenId, tokenSecret),
            },
        }

        self.send_event('quoine:auth_request', auth_payload)

    def subscribe(self, channel_name, auth=None):
        """Subscribe to a channel.

        :param str channel_name: The name of the channel to subscribe to.
        :param str auth: The token to use if authenticated externally.
        :rtype: pysher.Channel
        """
        self.pusher.channels[channel_name] = Channel(channel_name, self.pusher.connection)
        if (self._can_subscribe_now(self.pusher.channels[channel_name])):
            self._execute_subscription(self.pusher.channels[channel_name])               

        return self.pusher.channels[channel_name]

    def _execute_subscription(self, channel):
        if not channel.subscribed:
            data = {'channel': channel.name}
            self.pusher.connection.send_event('pusher:subscribe', data)


    def _can_subscribe_now(self, channel):
        connectionReady = self.connected()
        authReady = (not self.authenticating) or self.authenticated 
        channelReady = True
        return connectionReady and authReady and channelReady

    def _subscribe_all_waiting(self):
        for channel_name in self.pusher.channels:
            self._execute_subscription(self.pusher.channels[channel_name])


    def handle_connected(self, data):
        self._send_all_waiting()
        if not self.authenticating:
            self._subscribe_all_waiting

    def handle_auth_success(self, data):
        self.authenticated = True
        self.authenticating = False
        self._subscribe_all_waiting()
