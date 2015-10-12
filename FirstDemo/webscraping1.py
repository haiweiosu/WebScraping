#Sample web-scrpaing functions. 
#Credited to: http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/


from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "httl://www.chicagoreader.com"

def get_category_links(section_url):
	html = urlopen(section_url).read()
	soup = make_soup(url)
	boccat = soup.find("dl", "boccat")
	category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
	return category_links

def get_category_winner(category_url):
	html = urlopen(category_url).read()
	soup = make_soup(url)
	category = soup.find("h1", "headline").string
	winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
	runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
	return {"category": category,
			"category_url": category_url,
			"winner": winner,
			"runners_up": runners_up}

def make_soup(url):
	html = urlopen(url).read()
	return BeautifulSoup(html, "lxml")
