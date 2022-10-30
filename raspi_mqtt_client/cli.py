"""CLI interface for raspi mqtt client
"""
import logging
import signal
import sys
import time

from decouple import UndefinedValueError, config

from raspi_mqtt_client.mqtt import MQTT
from raspi_mqtt_client.sensors.raspi_sensor_cpu import RaspiCpuLoadSensor
from raspi_mqtt_client.sensors.raspi_sensor_memory import RaspiMemorySensor
from raspi_mqtt_client.sensors.raspi_sensor_temperature import (
    RaspiCpuTemperatureSensor,
)
from raspi_mqtt_client.sensors.raspi_sensor_wlan import RaspiWlanSensor


def fetch_env_value(env_name, default_value=""):
    """ "
    Fetch properties from environment
    """
    try:
        return config(str(env_name))
    except UndefinedValueError:
        logging.error(
            "Environment parameter %s not set. "
            "Please check your configuration.",
            env_name,
        )
        return default_value


def main(exit_please=False):  # pragma: no cover
    """
    Start the main logic
    """
    logging.basicConfig(
        format="%(levelname)s:%(message)s",
        filename="raspi_mqtt_client.log",
        level=logging.DEBUG,
    )

    logging.info("Starting Raspberry Pi MQTT client...")

    mqtt_broker_host = fetch_env_value("MQTT_BROKER_HOST", "localhost")
    mqtt_broker_port = fetch_env_value("MQTT_BROKER_PORT", "1883")
    mqtt_broker_user = fetch_env_value("MQTT_BROKER_USER")
    mqtt_broker_pass = fetch_env_value("MQTT_BROKER_PASS")
    location = fetch_env_value("LOCATION", "unknown")
    timeout = fetch_env_value("TIMEOUT", "2")

    sensors = [
        RaspiCpuLoadSensor(location),
        RaspiCpuTemperatureSensor(location),
        RaspiMemorySensor(location),
        RaspiWlanSensor(location),
    ]

    mqtt_client = MQTT(
        mqtt_broker_host,
        int(mqtt_broker_port),
        mqtt_broker_user,
        mqtt_broker_pass,
    )

    def signal_handler(sig, frame):
        logging.debug("Caught signal: %s in frame: %s", str(sig), str(frame))
        mqtt_client.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    mqtt_client.start()

    while not exit_please:
        for sensor in sensors:
            topic = sensor.read_topic()
            data = sensor.read_sensor_data()
            mqtt_client.publish_all(topic, data)

        time.sleep(int(timeout))

    mqtt_client.stop()
    logging.info("Raspberry Pi MQTT client stopped.")
