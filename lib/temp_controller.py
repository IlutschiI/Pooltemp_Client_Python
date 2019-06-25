import sched

from w1thermsensor import W1ThermSensor
import time


class TempController:
    s = sched.scheduler(time.time, time.sleep)

    def start(self):
        self.s.enter(5, 1, self.read_temperatures)
        self.s.run()

    def read_temperatures(self):
        sensors = W1ThermSensor.get_available_sensors()
        for sensor in sensors:
            print("Sensor " + sensor.id + " found: " + str(sensor.get_temperature()))
        self.s.enter(5, 1, self.read_temperatures)
        self.s.run()
