import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class IMDBScraper:

    def __init__(self, base_url = "https://www.imdb.com/title/tt"):
        self.base_url = base_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_summary(self):
        try:
            elem = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='plot-xs_to_m']"))
            )
            return elem.text.strip()
        except:
            return None

    def get_credits(self):
        credits = {"Director": [], "Writer": [], "Stars": []}
        credit_items = self.driver.find_elements(By.CSS_SELECTOR, "li[data-testid='title-pc-principal-credit']")

        for item in credit_items:
            try:
                label = item.find_element(By.CSS_SELECTOR, "span.ipc-metadata-list-item__label").text.strip()
                # İsimleri hem <a> hem de diğer etiketlerden çek
                names = [el.text.strip() for el in
                         item.find_elements(By.CSS_SELECTOR, "a, span.ipc-metadata-list-item__list-content-item")]

                if "Director" in label:
                    credits["Director"].extend(names)
                elif "Writers" in label:
                    credits["Writer"].extend(names)
                elif "Stars" in label:
                    credits["Stars"].extend(names)
            except Exception as e:
                continue
        return credits

    def scrape_movie(self, imdbid):
        url = f"{self.base_url}{imdbid}/"
        self.driver.get(url)
        time.sleep(2)
        summary = self.get_summary()
        credits = self.get_credits()
        return {
            "imdbid": imdbid,
            "url": url,
            "summary": summary,
            "director": ", ".join(credits["Director"]),
            "writers": ", ".join(credits["Writer"]),
            "stars": ", ".join(credits["Stars"]),
        }

    def close(self):
        self.driver.quit()

