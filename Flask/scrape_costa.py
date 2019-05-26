from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://ogmaribel.github.io/comparison.html/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser
    soup = bs(html, "html.parser")

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data
