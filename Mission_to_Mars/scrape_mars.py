
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    #scrape for mars news 
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html,"html.parser")
    thread = soup.find("div", class_="list_text")
    news_title = thread.find("div", class_= "content_title").text
    news_p = thread.find("div", class_="article_teaser_body").text

    #scrape for featured image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = bs(html,"html.parser")
    featured_image = soup.find("img", class_="thumb")["src"]
    image_url = "https://www.jpl.nasa.gov/" + featured_image

    #scrape for mars facts
    facts_url = "https://space-facts.com/mars/"
    df = pd.read_html(facts_url)
    mars_df = df[0]
    marss_df.columns=["Description", "Mars"]
    mars_df.set_index("Description", inplace=True)
    mars_facts = mars_df.to_html("mars_data.html")

    #scrape for hemispheres
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)     
    html = browser.html
    soup = bs(html, "html.parser")
    results = soup.find_all("div", class_="item")
    hemisphere_image_urls = []
    for result in results:
        title = result.find("h3").text
        hemi_link = result.find("a", class_="itemLink product-item")["href"]
        image_link = "https://astrogeology.usgs.gov/" + hemi_link
        browser.visit(image_link)
        image_html = browser.html
        soup = bs(image_html, "html.parser")
        image_url = "https://astrogeology.usgs.gov/" + soup.find("img", class_="wide-image")["src"]
        hemisphere_image_urls.append({"title":title, "Image_url":image_url})

    mars_data = {"news_title":news_title, "news_text":news_p,"featured_image":image_url,
                "mars_facts":mars_facts, "hemi_image_urls":hemisphere_image_urls}

    browser.quit()

    return mars_data
   