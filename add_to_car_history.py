import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from datetime import datetime
from scrape_cars import scrape_cars

# Define queries
civic_query = '?_utf8=%E2%9C%93&home_delivery=&list_price_max=14000&list_price_min=&makes[]=honda&maximum_distance=100&mileage_max=140000&models[]=honda-civic&page=1&page_size=200&sort=best_deal&stock_type=used&virtual_appointments=&year_max=&year_min=2012&zip=92037'
prius_query = '?_utf8=%E2%9C%93&home_delivery=&list_price_max=15000&list_price_min=&makes[]=toyota&makes[]=toyota&makes[]=toyota&makes[]=toyota&makes[]=toyota&maximum_distance=100&mileage_max=&models[]=toyota-prius_v&models[]=toyota-prius_c&models[]=toyota-prius_prime&models[]=toyota-prius_plug_in&models[]=toyota-prius&page_size=200&sort=best_deal&stock_type=used&virtual_appointments=&year_max=&year_min=2015&zip=92037'
camry_query = '?_utf8=%E2%9C%93&home_delivery=&list_price_max=14000&list_price_min=&makes[]=toyota&maximum_distance=100&mileage_max=&models[]=toyota-camry&page=1&page_size=200&sort=best_deal&stock_type=used&virtual_appointments=&year_max=&year_min=2013&zip=92037'
mazda_query = '?_utf8=%E2%9C%93&body_style_slugs[]=hatchback&home_delivery=&list_price_max=15000&list_price_min=2000&makes[]=mazda&maximum_distance=150&mileage_max=&models[]=mazda-mazda3&stock_type=used&virtual_appointments=&year_max=&year_min=2014&zip=92037'

queries = [civic_query, prius_query, camry_query, mazda_query]

# Read in current cars histories
cars_history = pd.read_csv('/Users/felipelorenzi/Documents/GitHub/Cars_Web_Scraping/cars_history.csv')

# Scrape for new info and append to cars history
for query_url in queries:
    current_cars = scrape_cars(query_url)
    cars_history = pd.concat([cars_history, current_cars]).drop_duplicates()

# Save new cars history
cars_history.to_csv('/Users/felipelorenzi/Documents/GitHub/Cars_Web_Scraping/cars_history.csv', index = False)