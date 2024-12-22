from abc import ABC
from numpy import array


class BaseConveter(ABC):

    def __init__(
            self,
            adc_bits: int = None,
            sensor_range: float = None,
            offset: float = None) -> None:

        self.adc_bits = adc_bits
        self.sensor_range = sensor_range
        self.offset = offset
        self.adc_levels = 2**adc_bits if adc_bits else None

        return None

    @classmethod
    def convert_value(self, value: int) -> array:

        return value * (self.sensor_range / self.adc_levels) + self.offset

    @classmethod
    def convert_values(self, values: array) -> array:

        return values * (self.sensor_range / self.adc_levels) + self.offset
