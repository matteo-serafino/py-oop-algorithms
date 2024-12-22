from src.converter.base import BaseConveter


class AccelerometerConverter(BaseConveter):

    def __init__(
            self,
            adc_bits: int = 16,
            sensor_range: float = 32,
            offset: float = 0) -> None:
        super().__init__(adc_bits, sensor_range, offset)
