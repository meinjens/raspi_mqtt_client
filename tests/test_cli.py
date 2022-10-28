import unittest
from raspi_mqtt_client.cli import main


class CliTestCase(unittest.TestCase):
    def test_logging_should_contain_start_and_stop_message(self):
        with self.assertLogs("root", level="INFO") as error_logs:
            main()
        self.assertEqual(
            error_logs.output[0],
            "INFO:root:Starting Raspberry Pi MQTT client...",
        )
        self.assertEqual(
            error_logs.output[-1],
            "INFO:root:Raspberry Pi MQTT client stopped.",
        )

    def test_no_config_should_log_errors(self):
        with self.assertLogs("root", level="ERROR") as error_logs:
            main()
        self.assertEqual(
            error_logs.output,
            [
                "ERROR:root:Environment parameter MQTT_BROKER_HOST not set. Please check your configuration.",
                "ERROR:root:Environment parameter MQTT_BROKER_PORT not set. Please check your configuration.",
                "ERROR:root:Environment parameter MQTT_BROKER_USER not set. Please check your configuration.",
                "ERROR:root:Environment parameter MQTT_BROKER_PASS not set. Please check your configuration.",
            ],
        )


if __name__ == "__main__":
    unittest.main()
