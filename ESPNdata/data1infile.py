
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

base_url = ("http://espn.go.com/college-football/rankings")

soup = BeautifulSoup(urlopen(base_url).read())
teams = soup.find_all("td", "align-left team")
team_urls = [td.a["href"] for td in teams]

with open("data/src-ESPN_NCAAF_teams.tsv", "w") as f:
    fieldnames = ("rank", "team", "record", "points", "trend")
    output = csv.writer(f, delimiter="\t")
    output.writerow(fieldnames)

    for url in team_urls:
        url = url.replace("http://espn.go.com", "")  # inconsistent URL
        page = urlopen("http://espn.go.com{0}".format(url))
        team1 = BeautifulSoup(page.read()).find("td", {"id": "team"})
        rank = team1.find("td", {"id": "rank"}).encode_contents().strip()
        team2 = team1.h1.encode_contents().strip().split("<br/>")[0]
        restaurant = team1.h1.span.encode_contents()
        description = team1.p.encode_contents().strip()

        output.writerow([rank, team, record, points, trend])

print "Done writing file"