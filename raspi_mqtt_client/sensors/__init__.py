"""
Sensors that publish their values over MQTT
"""


class Sensor:
    """
    Abstract sensor class
    """

    location = None
    category = "sensor"
    component = "unknown"

    def __init__(self, location="unknown"):
        self.location = location

    def read_sensor_data(self) -> list:
        """
        :return: Read sensor data and answer it as dict
        """
        return []

    def read_topic(self) -> str:
        """
        :return: Answer name of topic to publish the values as str
        """
        return f"/{self.location}/{self.category}/{self.component}/"
