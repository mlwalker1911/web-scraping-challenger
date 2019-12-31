# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'web-scraping-challenger'))
	print(os.getcwd())
except:
	pass

# %%
from splinter import Browser
from bs4 import BeautifulSoup


# %%
executable_path = {"executable_path": r"C:\SMU Data Scientist\homework\WEb Scaping\web-scraping-challenger\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# %% [markdown]
# ### Mars Site

# %%
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# %%
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elm = news_soup.select_one("ul.item_list li.slide" ,)


# %%
slide_elm.find("div", class_='content_title')


# %%
news_title = slide_elm.find("div", class_='content_title').get_text()
news_title


# %%
news_p = slide_elm.find("div", class_='article_teaser_body').get_text()
news_p

# %% [markdown]
# ### JPL Space Images

# %%
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# %%
full_image_elm = browser.find_by_id('full_image')
full_image_elm.click()


# %%
browser.is_element_present_by_text('more info' , wait_time=1)
more_info_elm = browser.find_link_by_partial_text('more info')
more_info_elm.click()


# %%
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# %%
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# %%
img_url = f'https://www.jpl.nasa.gov'
img_url

# %% [markdown]
# ### Mars Weather

# %%
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# %%
html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# %%
mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
mars_weather_tweet


# %%
mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather

# %% [markdown]
# ### Mars Hemisphere

# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# %%
hemisphere_image_urls =[]

links = browser.find_by_css("a.product-item h3")

for i in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css("a.product-item h3")[i].click()
    
    sample_elem = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] =sample_elem['href']
sample_elem


# %%



myData = {}

myData["news_title"] = news_title

myData["news_p"] = news_p

myData["img_url_rel"] = img_url_rel

myData["img_url"] = img_url

myData["mars_weather_tweet"] = mars_weather_tweet

myData["mars_weather"] = mars_weather


