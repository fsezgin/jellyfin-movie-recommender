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

    def merge_movie_tag_genre(self):
        # Merge on movieID
        # tag_genre_data = self.dfs['movies'].merge(self.dfs['links'], on = "movieId", how = "left")

        # Genome Scores + Tags merge
        genome = self.dfs['genome_score'].merge(self.dfs['genome_tag'], on = "tagId")
        movie_genome_matrix = genome.pivot_table(
            index="movieId",
            columns="tag",
            values="relevance",
            fill_value=0
        )

        top_tags = self.dfs['tags'].value_counts().head(500).index
        tags_filtered = self.dfs['tags'][self.dfs['tags']['tags'].isin(top_tags)]

        # Film x tag matrix (kaç kullanıcı eklemiş)
        movie_tag_matrix = tags_filtered.pivot_table(
            index='movieId',
            columns='tag',
            values='userId',
            aggfunc='count',
            fill_value=0
        )

        genres_expanded = self.dfs['movies']['genres'].str.get_dummies(sep='|')
        genres_expanded['movieId'] = self.dfs['movies']['movieId']

        movie_features = movie_genome_matrix.merge(
            movie_tag_matrix, left_index=True, right_index=True, how='outer'
        ).merge(
            genres_expanded.set_index('movieId'), left_index=True, right_index=True, how='outer'
        ).fillna(0)

        return movie_features