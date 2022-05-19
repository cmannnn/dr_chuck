import requests
from bs4 import BeautifulSoup
import pandas as pd

# Premier League Stats
html_text = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats').text
soup = BeautifulSoup(html_text, 'lxml')

# players stats - most goals
player_goals = soup.find('div', id='wrap')
player_goals2 = player_goals.find('div', id='info')
player_goals3 = player_goals2.find('div', id='meta')
player_goals4 = player_goals3.find_all('div')[1]
player_goals5 = player_goals4.find_all('p')[3].text

# players stats - most assists
player_assists = player_goals4.find_all('p')[4].text

# player stats - most clean sheets
player_clean_sheets = player_goals4.find_all('p')[5].text

#print(f'{player_goals5}')
#print(f'{player_assists}')
#print(f'{player_clean_sheets}')

# current league table
current_league_table = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats')[0]
current_league_table = current_league_table.reset_index(drop=True)
current_league_table = current_league_table.set_index('Rk')
current_league_table = current_league_table.drop(columns=['Notes', 'Attendance'])

#print(current_league_table.info())


squad_stats_table = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats')


# cleaning column names
#squad_stats_table = squad_stats_table.rename(columns={'Rk': 'Rank', 'MP': 'Matches Played'})

# squad stats NOT PULLING SECOND TABLE IN CORRECTLY
def get_tables(input):
	tables = BeautifulSoup(input, 'lxml').find_all(['table', 'h1'])
	formatted = pd.DataFrame(pd.read_html(str(tables))).prettify()
	return formatted

print(get_tables(html_text))




