import pandas as pd
from scrapers.movie_info_scraper import IMDBScraper
from settings.config import Config

if __name__ == "__main__":
    df = pd.read_csv(Config.links_csv_path)
    scraper = IMDBScraper()

    results = []
    for imdbid in df["imdbId"].head(5):  # test için 5 film
        data = scraper.scrape_movie(str(imdbid).zfill(7))
        results.append(data)

    scraper.close()

    out_df = pd.DataFrame(results)
    out_df.to_csv("movies_training_data.csv", index=False)