""""
CPU sensor
"""
import psutil

from raspi_mqtt_client.sensors import Sensor


class RaspiCpuLoadSensor(Sensor):
    """
    Reads cpu load
    """
    component = "cpu"

    def read_sensor_data(self) -> list:
        """
        Read sensor data and answer it as dict
        :return:
        """

        cpu_metrics = psutil.cpu_times_percent(interval=1, percpu=False)

        return [
            {"name": "user", "value": cpu_metrics[0]},
            {"name": "nice", "value": cpu_metrics[1]},
            {"name": "system", "value": cpu_metrics[2]},
            {"name": "idle", "value": cpu_metrics[3]},
        ]

    def read_topic(self) -> str:
        """
        Answer name of topic
        :return:
        """
        return f"/{self.location}/{self.category}/{self.component}/load/"
