from abc import ABC
from pandas import DataFrame
from numpy import ndarray


class BaseAlgorithm(ABC):

    # Class Attributes
    _version = 'v0.0'
    _aggregation_window = 60

    def __init__(self) -> None:
        return None

    @property
    def version(self) -> str:
        """Algorithm Version"""
        return self._version

    @property
    def aggregation_window(self) -> int:
        """Aggregation Window in seconds"""
        return self._aggregation_window

    @classmethod
    def preprocess(self) -> None:
        pass

    @classmethod
    def estimate(self):
        raise NotImplementedError

    @classmethod
    def aggregate(self,
                  timestamps: ndarray,
                  values: ndarray,
                  method: str = 'mean'
                  ):

        df = DataFrame({'timestamps': timestamps, 'values': values})
        df = DataFrame(
            list(zip(timestamps, values)),
            columns=['timestamps', 'values']
        )

        df['timestamps_unix'] = df[
            'timestamps'].apply(lambda x: x // self.aggregation_window)

        if method == 'mean':
            df_agg = df.groupby('timestamps_unix')[
                'values'].mean().reset_index(drop=False)

        self.biomarker_agg = df_agg
        return self
