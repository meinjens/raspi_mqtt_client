"""
MQTT client logic
"""

import logging
import signal
import uuid

import paho.mqtt.client as mqtt


class MQTT:
    """
    Control class handles the main loop
    """

    mqtt_client = None
    host = "localhost"
    port = 1883
    username = None
    password = None

    def __init__(
        self, host="localhost", port=1883, username=None, password=None
    ):
        """
        Constructor
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client_id = f"raspi_mqtt_client-{uuid.uuid1()}".encode('utf-8')

        self.mqtt_client = mqtt.Client(
            client_id="raspi_mqtt_client", protocol=mqtt.MQTTv5
        )

        if self.username is not None:
            self.mqtt_client.username_pw_set(self.username, self.password)

        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self):
        """
        Stop server on SIGINT
        :return: nothing
        """
        self.stop()

    #pylint: disable=too-many-arguments
    def on_connect(self, client, userdata, flags, reason_code, properties):
        """
        Generate log string on connection
        :param client:
        :param userdata:
        :param flags:
        :param reason_code:
        :param properties:
        :return: nothing
        """
        logging.debug(
            "on_connect: client=%s, userdata=%s, flags=%s, properties=%s",
            str(client),
            str(userdata),
            str(flags),
            str(properties),
        )

        logging.info(
            "Connected client (id: %s) to MQTT broker (result: %s).",
            self.client_id,
            mqtt.connack_string(reason_code),
        )

    def on_disconnect(self, client, userdata, reason_code, properties):
        """
        Generate log string on disconnect
        :param client:
        :param userdata:
        :param reason_code:
        :param properties:
        :return:
        """
        logging.debug(
            "on_disconnect: client=%s, userdata=%s, reason_code=%s, properties=%s",
            str(client),
            str(userdata),
            str(reason_code),
            str(properties),
        )

        logging.info(
            "Disconnect client (id: %s) from MQTT broker.", self.client_id
        )

    def start(self):
        """
        Start mqtt client
        :return: nothing
        """
        self.mqtt_client.connect(host=self.host, port=self.port)
        self.mqtt_client.loop_start()

    def stop(self):
        """
        Stop mqtt client
        :return: nothing
        """
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
