import pandas as pd

NAME_BASICS_PATH = r".\data\name.basics.tsv"
TITLE_AKAS_PATH = r".\data\title.akas.tsv"
TITLE_BASICS_PATH = r".\data\title.basics.tsv"
TITLE_CREW_PATH = r".\data\title.crew.tsv"
TITLE_EPISODE_PATH = r".\data\title.episode.tsv"
TITLE_PRINCIPALS_PATH = r".\data\title.principals.tsv"
TITLE_RATINGS_PATH = r".\data\title.ratings.tsv"

name_basics_df = pd.read_csv(NAME_BASICS_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')
title_akas_df = pd.read_csv(TITLE_AKAS_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')
title_basics_df = pd.read_csv(TITLE_BASICS_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')
title_crew_df = pd.read_csv(TITLE_CREW_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')
title_episodes_df = pd.read_csv(TITLE_EPISODE_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')
title_principals_df = pd.read_csv(TITLE_PRINCIPALS_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')
title_ratings_df = pd.read_csv(TITLE_RATINGS_PATH, sep="\t", low_memory=False, na_values="\\N", on_bad_lines='skip')

print(name_basics_df.head())
print(title_akas_df.head())
print(title_basics_df.head())
print(title_crew_df.head())
print(title_episodes_df.head())
print(title_principals_df.head())
print(title_ratings_df.head())