import os.path

import pandas as pd
from typing import Dict

class DataPreprocessing:

    def __init__(self, data_paths: list[str], processed_dir: str = "processed"):
        self.data_paths = data_paths
        self.dfs : Dict[str, pd.DataFrame] = {}
        self.processed_dir = processed_dir

    def _load_data(self) -> Dict[str, pd.DataFrame]:
        self.dfs = {}
        try:
            for path in self.data_paths:
                key = os.path.splitext(os.path.basename(path))[0]
                self.dfs[key] = pd.read_csv(path)
            return self.dfs
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def save_as_parquet(self) -> None:
        for name, df in self.dfs.items():
            save_path = os.path.join(self.processed_dir, f"{name}.parquet")
            df.to_parquet(save_path, index=False)
            print(f"Saved {name} → {save_path}")

    def load_from_parquet(self) -> Dict[str, pd.DataFrame]:
        self.dfs = {}
        try:
            for file in os.listdir(self.processed_dir):
                if file.endswith(".parquet"):
                    key = file.replace(".parquet", "")
                    path = os.path.join(self.processed_dir, file)
                    self.dfs[key] = pd.read_parquet(path)
            return self.dfs
        except Exception as e:
            print(f"Error loading parquet data: {e}")
            raise

    def merge_movie_ratings(self):
        movie_data = pd.merge(self.dfs["ratings"],self.dfs["movies"], on='movie_id')
        movie_ratings = (
            movie_data.groupby("title")["rating"]
            .agg(avg_rating=lambda x: round(x.mean(), 1), rating_counts="count")
            .reset_index()
        )
        return movie_ratings
