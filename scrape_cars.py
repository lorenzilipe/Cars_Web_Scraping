import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from datetime import datetime

def scrape_cars(query_url):
    cars_base = 'https://www.cars.com/shopping/results/'
    
    # Get HTML and make soup
    model_url = cars_base + query_url
    model_html = requests.get(model_url).text
    model_soup = BeautifulSoup(model_html, 'html.parser')
    
    # Find and store vehicle cards
    vehicle_cards = model_soup.find_all("div", class_ = "vehicle-card")
    
    # Create outer car list
    vehicles = []

    # Extract data from vehicle cards
    for vehicle_card in vehicle_cards:
        
        # Get title, mileage, price, and distance
        title = vehicle_card.find('h2', class_ = 'title').text
        
        mileage = vehicle_card.find('div', class_ = 'mileage').text
        mileage = int(re.sub(pattern = r'\D*', repl = '', string = mileage))
        
        price = vehicle_card.find('span', class_ = 'primary-price').text
        price = int(re.sub(pattern = r'\D*', repl = '', string = price))
        
        try:
            distance = vehicle_card.find('div', class_ = 'miles-from').text.strip()
            distance = int(re.sub(pattern = r'\D+.*', repl = '', string = distance))
        except:
            distance = np.NaN
        
        # Get date accessed
        date_accessed = datetime.now().strftime("%Y-%m-%d %H hrs")

        # Ignore if mileage == 0
        if mileage == 0:
            continue

        # Append vehicle data to dataframe
        vehicles.append([title, mileage, price, distance, date_accessed])
        
    return pd.DataFrame(vehicles, columns = ['title', 'mileage', 'price', 'distance', 'date_accessed'])