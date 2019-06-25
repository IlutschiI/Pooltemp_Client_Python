from w1thermsensor import W1ThermSensor
import time


class TempController:

    def start(self):
        sensors = W1ThermSensor.get_available_sensors()

        print(sensors)

        for sensor in sensors:
            print("Sensor " + sensor.id + " found")

    def readTemperatures(self):
        sensors = W1ThermSensor.get_available_sensors()
        for sensor in sensors:
            print(f"Sensor {sensor.id} found: {sensor.get_temperature()}")
