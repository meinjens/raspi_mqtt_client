"""
Read free and used memory
"""
import os

from raspi_mqtt_client.sensors import Sensor


class RaspiMemorySensor(Sensor):
    """
    Read memory free and used memory
    """
    component = "memory"

    def read_sensor_data(self) -> list:
        """
        :return: Memory values as dict
        """
        memory_values = self.read_memory_values()

        return [
            {"name": "used", "value": memory_values[0]},
            {"name": "free", "value": memory_values[1]},
        ]

    def read_memory_values(self):
        """
        Use system process to read memory values
        :return:
        """
        system_process = os.popen("free")
        i = 0
        while 1:
            i += 1
            line = system_process.readline()
            if i == 2:
                return line.split()[1:4]
