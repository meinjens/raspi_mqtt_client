# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import unittest
from raspi_mqtt_client.cli import main


class CliTestCase(unittest.TestCase):
    def test_logging_should_contain_start_and_stop_message(self):
        with self.assertLogs("root", level="INFO") as error_logs:
            main(exit_please=True)
        self.assertEqual(
            error_logs.output[0],
            "INFO:root:Starting Raspberry Pi MQTT client...",
        )
        self.assertEqual(
            error_logs.output[-1],
            "INFO:root:Raspberry Pi MQTT client stopped.",
        )


if __name__ == "__main__":
    unittest.main()
