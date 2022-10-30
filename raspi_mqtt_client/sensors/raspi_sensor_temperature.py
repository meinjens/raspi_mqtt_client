"""
Measure CPU temperature of raspberry pi
"""
import logging
import subprocess
from pathlib import Path


class RaspiCpuTemperatureSensor:
    """
    Reads cpu temperature from raspberry pi
    """

    category = "sensor"
    component = "cpu"
    location = "unknown"
    vcgencmd = "/usr/bin/vcgencmd"

    def __init__(self, location: str = "unknown"):
        self.location = location

    def read_sensor_data(self) -> list:
        """
        :return: list with measured temperature
        """
        if not self.is_command_available():
            logging.warning(
                "Unable to find command for measuring cpu temperature: %s",
                self.vcgencmd,
            )
            return []

        try:
            temperature_string = subprocess.check_output(
                [self.vcgencmd, "measure_temp"]
            )
            temperature = float(
                str(temperature_string.decode().split("=")[1][:-3])
            )

            return [{"name": "temperature", "value": temperature}]
        except subprocess.CalledProcessError:
            return []

    def read_topic(self) -> str:
        """
        :return: Answer name of topic as str
        """
        return f"/{self.location}/{self.category}/{self.component}/"

    def is_command_available(self):
        """
        :return: check if tool for measuring temperature is installed
        """
        return Path(self.vcgencmd).is_file()
