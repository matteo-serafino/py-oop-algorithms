from numpy import array
from src.data.gyroscope import GyroscopeData


class Magnetometer(GyroscopeData):
    x: array
    y: array
    z: array
    fs: int = 64
