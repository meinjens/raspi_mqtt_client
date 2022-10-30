# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import unittest

from raspi_mqtt_client.mqtt import MQTT


class MyTestCase(unittest.TestCase):
    def test_mqtt_creates_a_client_id(self):
        mqtt = MQTT()

        self.assertIn(b"raspi_mqtt_client-", mqtt.client_id)


if __name__ == "__main__":
    unittest.main()
