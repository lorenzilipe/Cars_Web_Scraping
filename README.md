# Cars - Web Scraping

Web scraping a few pages of Cars.com every day to keep track of trends in prices.

## Files
- `add_to_car_history.py` File to be run every night. Calls web scraping function and adds to main database.
- `scrape_cars.py` Contains function which scrapes a single Cars.com page
- `analysis.ipynb` Jupyter notebook containing analysis made so far.

## Description

Used car prices have gone through the roof with the pandemic and the war in Ukraine, which has made getting a decent replacement for my recently-totaled (by someone else) '06 Prius quite challenging.

I've spent a lot of time in the last couple of months on Cars.com looking for a deal that would neither break my bank nor have a high probability of becoming a headache in a year - to no avail. I did some research and it looks like prices might begin to decline sometime soon, although no one can tell for certain.

So I asked myself: How long should I wait? Should I buy a car that recently got listed or should I wait a bit before getting in touch, see if the price changes? Are certain models getting cheaper than others? To answer those questions I decided to build a Python script that runs every night while I'm asleep. It scrapes Cars.com for the filters I selected and adds the details of the cars it found onto a table in a csv file. From there, I can read the file in Jupyter Notebooks whenever I want and use Python to see what the prices of the cars I'm after are doing.

I don't have much data yet, but I expect this tool to become more powerful as time goes by. So far I have found that only around 10% of cars change price in a week, and cars with higher mileages tend to drop in price faster than those with lower mileages.
