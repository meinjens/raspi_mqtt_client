import logging
import signal

import paho.mqtt.client as mqtt


class MQTT:
    """
    Control class handles the main loop
    """
    mqtt_client = None
    host = 'localhost'
    port = 1883
    username = None
    password = None

    def __init__(self, host='localhost', port=1883, username=None, password=None):
        """
        Constructor
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.mqtt_client = mqtt.Client(protocol=mqtt.MQTTv5)

        if self.username is not None:
            self.mqtt_client.username_pw_set(self.username, self.password)

        def on_connect():
            logging.info('Connected to MQTT server...')

        self.mqtt_client.on_connect = on_connect

        def on_disconnect():
            logging.info('Disconnected from MQTT server.')

        self.mqtt_client.on_disconnect = on_disconnect

        def signal_handler():
            self.stop()

        signal.signal(signal.SIGINT, signal_handler)

    def start(self):
        self.mqtt_client.connect(host=self.host, port=self.port)
        self.mqtt_client.loop_start()

    def stop(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
