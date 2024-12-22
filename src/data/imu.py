from dataclasses import dataclass
from numpy import array, sqrt, float32


@dataclass
class IMUData:
    x: array
    y: array
    z: array
    fs: int = 64

    @property
    def magnitude(self) -> array:
        """Accelerometer Magnitude"""
        return sqrt(self.x**2 + self.y**2 + self.z**2)


if __name__ == "__main__":

    my_x = array([1, 2, 4], dtype=float32)
    my_y = array([1, 0, 4], dtype=float32)
    my_z = array([1, 1, 3], dtype=float32)

    acc = IMUData(x=my_x, y=my_y, z=my_z, fs=32)

    print(acc.magnitude)
