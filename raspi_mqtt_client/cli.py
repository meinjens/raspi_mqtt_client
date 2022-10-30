"""CLI interface for raspi mqtt client
"""
import logging

from decouple import UndefinedValueError, config

from raspi_mqtt_client.mqtt import MQTT


def fetch_env_value(env_name, default_value=""):
    """ "
    Fetch properties from environment
    """
    try:
        return config(str(env_name))
    except UndefinedValueError:
        logging.error(
            "Environment parameter %s not set. Please check your configuration.",
            env_name,
        )
        return default_value


def main():  # pragma: no cover
    """
    Start the main logic
    """
    logging.basicConfig(
        format="%(levelname)s:%(message)s",
        filename="raspi_mqtt_client.log",
        level=logging.DEBUG,
    )

    logging.info("Starting Raspberry Pi MQTT client...")

    mqtt_broker_host = fetch_env_value("MQTT_BROKER_HOST")
    mqtt_broker_port = int(fetch_env_value("MQTT_BROKER_PORT"))
    mqtt_broker_user = fetch_env_value("MQTT_BROKER_USER")
    mqtt_broker_pass = fetch_env_value("MQTT_BROKER_PASS")

    mqtt_client = MQTT(
        mqtt_broker_host, mqtt_broker_port, mqtt_broker_user, mqtt_broker_pass
    )
    mqtt_client.start()

    mqtt_client.stop()
    logging.info("Raspberry Pi MQTT client stopped.")
