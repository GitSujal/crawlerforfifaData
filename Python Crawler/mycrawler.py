# Initial imports
import numpy as np
import pandas as pd 
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#matplotlib inline

import random
import urllib.request
import requests
from bs4 import BeautifulSoup
import warnings
import sys
warnings.filterwarnings('ignore')


offset = 0
columns = ['ID', 'Name', 'Age', 'Photo', 'Nationality', 'Flag', 'Overall', 'Potential', 'Club', 
           'Club Logo', 'Value', 'Wage', 'Special']
data = DataFrame(columns=columns)

year =19 #default value
if len(sys.argv) == 2 :
	year=sys.argv[1]


base_url = "https://sofifa.com/players/?v="+str(year)+"&offset="
outfile = "./Data/"+str(year)+"player_data.csv"

for offset in range(170):
    url = base_url + str(offset*60)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    table_body = soup.find('tbody')
    for row in table_body.findAll('tr'):
        td = row.findAll('td')
        picture = td[0].find('img').get('data-src')
        pid = td[0].find('img').get('id')
        nationality = td[1].find('a').get('title')
        flag_img = td[1].find('img').get('data-src')
        name = td[1].findAll('a')[1].text
        age = td[2].find('div').text.strip()
        overall = td[3].text.strip()
        potential = td[4].text.strip()
        club = td[5].find('a').text
        club_logo = td[5].find('img').get('data-src')
        value = td[6].text.strip()
        wage = td[7].text.strip()
        special = td[8].text.strip()
        player_data = DataFrame([[pid, name, age, picture, nationality, flag_img, overall, 
                                  potential, club, club_logo, value, wage, special]])
        player_data.columns = columns
        data = data.append(player_data, ignore_index=True)
    offset+=1
    data.to_csv(outfile, encoding='utf-8')

    if (offset % 20 == 0):
        print(offset)