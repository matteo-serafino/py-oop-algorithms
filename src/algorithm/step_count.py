from src.algorithm.base import BaseAlgorithm
from src.data.accelerometer import AccelerometerData
from numpy import sum


class StepCountAlgorithm(BaseAlgorithm):

    _version = 'v0.1'

    def __init__(self,
                 accelerometer: AccelerometerData,
                 window_length: int = 5
                 ) -> None:

        self.accelerometer = accelerometer
        self.window_length = window_length
        return None

    def estimate(self):
        self.values = sum(self.accelerometer.magnitude)
        self.timestamps = None
        return self

    def aggregate(self,
                  method: str = 'mean'
                  ):
        return super().aggregate(self.timestamps, self.values, method)


# class StepCountAlgorithmV2(BaseAlgorithmV2):

#     def __init__(self,
#                  x: ndarray = None,
#                  y: ndarray = None,
#                  z: ndarray = None,
#                  window_length: int = 5,
#                  fs: int = 64) -> None:

#         super().__init__(self)

#         self.x = x
#         self.y = y
#         self.z = z
#         self.window_length = window_length
#         self.fs = fs


# if __name__ == '__main__':

#     step_algo = StepCountAlgorithm()


#     print(step_algo.version)
