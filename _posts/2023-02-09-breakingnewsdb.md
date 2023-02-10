---
toc: false
layout: post
description: Breaking News Backend  Links to Maps
categories: [Breaking News Backend Links to Maps]
title: Breaking News Backend Links to Maps
---

## Breaking News Backend -- Links to Maps


On the Breakingnews Backend side ApiDBFlask/model/breakingnews.py defines the BreakingNews with News title, network, date, city, map coordinates and link to the actual web page. 
```
class BreakingNews(db.Model):
    __tablename__ = 'breakingnews'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(255), unique=False, nullable=False)
    _network = db.Column(db.String(255), unique=False, nullable=False)
    _day = db.Column(db.Date)
    _city = db.Column(db.String(255), unique=False, nullable=False)
    _zip =  db.Column(db.Integer, primary_key=True, unique=False)
    _link = db.Column(db.String(1024), unique=False, nullable=False)
```
<br/>
The BreakingNews class can be initialized to fill in the initial data in the SQL DB as shown in this code snippet
```
# Builds working data for testing
def initBreakingNews():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = BreakingNews(title='Padres FanFest mayhem: Long lines, crowded concourses, and delayed entry', network='CNN', day=date(2023, 1, 21), city="San Diego", zip=92127,"https://www.cbs8.com/article/news/local/padres-fanfest-mayhem-crowded-concourses-and-delayed-entry/509-543c588b-0eba-4c95-bb84-b3538894dd77")
    u2 = BreakingNews(title='Temecula - Forklifts Stolen From Home Depot', network='Fox', day=date(2023, 1, 20), city="Temecula", zip=92028,"https://fox5sandiego.com/news/local-news/forklift-stolen-from-oceanside-home-depot-in-broad-daylight/")
    u3 = BreakingNews(title='Long Beach State beats UC Irvine in OT', network='ABC', day=date(2023, 1, 19), city="Irvine", zip=92697,"https://www.usatoday.com/story/sports/ncaab/2023/02/05/long-beach-state-beats-uc-irvine-in-ot-for-6th-straight-win/51256357/")
    u4 = BreakingNews(title='El Centro will conduct a public hearing for new parks', network='NBC', day=date(2023, 1, 20), city="El Centro", zip=92243,"https://www.ivpressonline.com/")
    u5 = BreakingNews(title='Backpacking Permits For Joshua Tree National Park Available Online', network='BBC', day=date(2023, 1, 22), city="Joshua Tree", zip=92252,"https://www.nps.gov/jotr/planyourvisit/permitsandreservations.htm")
    u6 = BreakingNews(title='Escondido council appoints Palomar College trustee to vacant seat', network='CNN', day=date(2023, 1, 21), city="Escondido", zip=92025, "https://thecoastnews.com/escondido-council-appoints-palomar-college-trustee-to-vacant-seat/")
    u7 = BreakingNews(title='Salton Sea reduced inflow, the lake is shrinking and rising in salinity', network='Fox', day=date(2023, 1, 20), city="Salton Sea", zip=92274,"https://onlinelibrary.wiley.com/doi/10.1111/1752-1688.13063?af=R")
    u8 = BreakingNews(title='Mouse born at San Diego Zoo Safari Park wins Guinness award for longevity', network='CNN', day=date(2023, 1, 21), city="San Diego", zip=92127,"https://www.10news.com/news/local-news/mouse-born-at-san-diego-zoo-safari-park-wins-guinness-award-for-longevity")
    u9 = BreakingNews(title='Irvine Spectrum Adds First OC Shake Shack', network='NBC', day=date(2023, 1, 20), city="Irvine", zip=92697,"https://www.10news.com/news/local-news/mouse-born-at-san-diego-zoo-safari-park-wins-guinness-award-for-longevity")
    u10 = BreakingNews(title='San Diego celebrates National Pizza Day', network='BBC', day=date(2023, 1, 22), city="San Diego", zip=92127,"https://www.kusi.com/san-diego-celebrates-national-pizza-day/")
```


<br/>
The front end would fetch the breaking news data from the Breaking API services and displays the maps with links to the news site. Currently the news is grabbed from the static array but in furture this will use the API services to fill the map with news links.
<img src="{{site.baseurl}}/images/map.jpg" alt="group-flask-website jpg">

<br/>
 Clicking on the News Links in Maps leads to the online News Page
<img src="{{site.baseurl}}/images/maps2news.png" alt="group-flask-website jpg">
