# A short script to get local ip, use that to find the user's state, and create a webpage summarizing all active weather alerts in the state.

import requests

ip_address = requests.get('http://api.ipify.org').text

print(f'IP Address: {ip_address}')

geo_data = requests.get(f'http://ip-api.com/json/{ip_address}').json()

print(geo_data)

lat = geo_data['lat']
lon = geo_data['lon']

print('Latitude: {lat}')
print('Longitude: {lon}')

response = requests.get(f'https://api.weather.gov/alerts/active?point={lat},{lon}').json()

print(f"Active alerts in {geo_data['region']}: {len(response['features'])}")

file = open('./alert.html', 'w')
file.write(f"<h1>Active Weather Alerts for {geo_data['region']}:<h1>")
for x in response['features']:
    file.write(f"<h1>{x['properties']['headline']}<h1>")
    file.write(f"<h3>{x['properties']['headline']}<h3>")
    file.write(f"<p>{x['properties']['headline']}<p>")