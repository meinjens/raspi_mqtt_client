from raspi_mqtt_client.control import Control


def test_control_can_be_created():
    control = Control()
    assert not control is None
