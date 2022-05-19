import requests
from bs4 import BeautifulSoup
from datetime import datetime


# setting current time
now = datetime.now()
time = now.strftime('%A, %B, %d, %I:%M%p')


# W. Hartford NOAA weather forecast
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.75967070000007&lon=-72.72651189999993')

# creating soup
soup = BeautifulSoup(page.content, 'html.parser')

# current conditions


# Extended (Short) Forecast for W Hartford CT
seven_day = soup.find(id='seven-day-forecast')

# 5 day forecast block
forecast_items = seven_day.find_all(class_='forecast-tombstone')

# retrieving the most upcoming forecast block
one_block = forecast_items[0]

# name of the first block
period = one_block.find(class_='period-name').get_text()
#print(period)

# short forecast description of first block
short_desc = one_block.find(class_='short-desc').get_text(' ')
#print(short_desc)

'''# temp of the first block
temp = one_block.find(class_='temp temp-low').get_text()
#print(temp)'''

# detailed forecast description of the first block
img = one_block.find('img')
tonight = img['title']
#print(tonight)

'''---------------------------------------------------'''
# looking into current conditions block
current_conditions = soup.find(id='current-conditions')

# current condition first block
location_body = current_conditions.find_all(class_='panel-title')
location_sub = location_body[0]
location_title = location_sub.get_text()

# current temp
current_conditions_temp = current_conditions.find_all(class_='myforecast-current-lrg')
current_conditions_weather = current_conditions_temp[0]
current_temp = current_conditions_weather.get_text()

# current weather
current_weather_class = current_conditions.find_all(class_='myforecast-current')
current_weather_text = current_weather_class[0]
current_weather = current_weather_text.get_text()

# retrieving latitude and longitude
lat_long_body = current_conditions.find_all(class_='smallTxt')
lat_long_sub = lat_long_body[0]
lat_long_title = lat_long_sub.get_text(' ')


# compiled print block
print(
	' -------------------------------------------------\n'
	'| {} Weather Forecast |'.format(time),
	'| --------------------------------------------------------',
	'| Weather for: {} |'.format(location_title),
	'| -------------------------------------------------------- \n'
	'| {} |'.format(lat_long_title), 
	'| -----------------------------------------------',
	'| Current Temp: {} |'.format(current_temp) + ' Current Weather: {} |'.format(current_weather),
	'| --------------------------------------------------------------------- ',
	'| {} |'.format(tonight),
	'| ---------------------------------------------------------------------',
	sep='\n'
)










