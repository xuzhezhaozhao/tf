
class Celsius(object):
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


if __name__ == "__main__":
    man = Celsius(20)
    print man.temperature
    man.temperature = -220
    print man.to_fahrenheit()

    man.temperature = -320
    print man.to_fahrenheit()
