"""
Sensor for WLAN signal
"""
import logging
import re
import subprocess

from raspi_mqtt_client.sensors import Sensor


class RaspiWlanSensor(Sensor):
    """
    Reads wlan signal from iwconfig command
    """

    interface = "wlan0"

    def read_sensor_data(self) -> list:
        """
        :return: WLAN signal data as list
        """
        result = []
        try:
            command_result = subprocess.check_output(
                ["iwconfig", self.interface], stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            logging.error(
                "Unable to retrieve network information from iwconfig!"
            )
            return []

        for line in str(command_result).split("\n"):

            link_quality = re.search(
                r"Link Quality=([0-9]{1,3})/([0-9]{1,3})", line
            )
            signal_level = re.search(
                r"Signal level=([0-9]{1,3})/([0-9]{1,3})", line
            )
            noise_level = re.search(
                r"Noise level=([0-9]{1,3})/([0-9]{1,3})", line
            )

            if link_quality:
                result.append(
                    {
                        "name": "link_quality",
                        "value": int(
                            round(
                                float(link_quality.group(1))
                                / float(link_quality.group(2))
                                * 100
                            )
                        ),
                    }
                )
            if signal_level:
                result.append(
                    {
                        "name": "signal_level",
                        "value": int(
                            round(
                                float(signal_level.group(1))
                                / float(signal_level.group(2))
                                * 100
                            )
                        ),
                    }
                )
            if noise_level:
                result.append(
                    {
                        "name": "noise_level",
                        "value": int(
                            round(
                                float(noise_level.group(1))
                                / float(noise_level.group(2))
                                * 100
                            )
                        ),
                    }
                )

        return result
