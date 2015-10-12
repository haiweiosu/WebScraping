from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://espn.go.com/college-football/rankings"

def get_team_links(section_url):
	html = urlopen(section_url).read()
	soup = make_soup(url)
	align_left_team = soup.find("tr", "")
	team_links = [BASE_URL + td.a["href"] for td in align_left_team.findAll("td")]
	return category_links

def get_regular_season(category_url):
	html = urlopen(category_url).read()
	soup = make_soup(url)
	category = soup.find("a", "&lpos=college-football:schedule:full").string
	first_match = [h2.string for h2 in soup.findAll("a", "&lpos=college-football:schedule:regular")]
	return {"category": category,
			"category_url": category_url,
			"first_match": first_match}

def make_soup(url):
	html = urlopen(url).read()
	return BeautifulSoup(html, "lxml")