import pandas as pd
from typing import List

class DataPreprocessing:

    def __init__(self, data_paths: List[str]):
        self.data_paths = data_paths
        self.dfs : List[pd.DataFrame] = []

    def _load_data(self) -> List[pd.DataFrame]:
        self.dfs = []
        try:
            for path in self.data_paths:
                df = pd.read_csv(path)
                self.dfs.append(df)
            return self.dfs
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def merge_ratings_movies(self):
        dfs_dict = {
            path.split("/")[-1].replace(".csv", ""): df
            for path, df in zip(self.data_paths, self.dfs)
        }

        movie_data = pd.merge(dfs_dict["ratings"],dfs_dict["movies"], on='movie_id')
        movie_data.groupby('title')['rating'].count().sort_values(ascending=False)
