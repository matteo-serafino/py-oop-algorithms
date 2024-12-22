from src.algorithm.step_count import StepCountAlgorithm
from src.data.accelerometer import AccelerometerData
from src.converter.accelerometer import AccelerometerConverter
from numpy import array, float32


def main():

    acc_conv = AccelerometerConverter()
    print(acc_conv.offset)

    my_x = array([1, 2, 4], dtype=float32)
    my_y = array([1, 0, 4], dtype=float32)
    my_z = array([1, 1, 3], dtype=float32)

    steps = StepCountAlgorithm(
        accelerometer=AccelerometerData(
            x=my_x,
            y=my_y,
            z=my_z,
            fs=32)).estimate()
    steps_agg = steps.aggregate(method='sum')
    print(steps_agg)


if __name__ == "__main__":
    main()
