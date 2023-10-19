# Programing Task - assignment
Use the scraper framework (of your choice: BeautifulSoup, Scrapy, etc.) to scrape the first
100 items (title, image URL, price, location) from https://auto.bazos.cz and save it in the
Postgresql (or DB of your choice) database. Implement a simple HTTP server in Python and
show these 100 items on a simple page (title, image URL, price, location) and put everything
to a single docker-compose command so that I can just run "docker-compose up" in the
Github repository and see the scraped ads on http://127.0.0.1:8080 page.

Solution
========================


Pre-requisities
--------------

- git
- python3
- docker 
- docker-compose


Starting the server
------------------------------------

  - Clone project git clone ....
  - Run `docker-compose up`
  - Project is now available on 127.0.0.1:8080 in the browser
  - You can stop docker by CRTL+C 
