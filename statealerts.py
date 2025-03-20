import requests
import json

state = "UT"
response = requests.get(f'https://api.weather.gov/alerts/active?area={state}').json()

# print(response)
print("\nRaw json data:")
response_pretty =  json.dumps(response, indent=2)

print(response_pretty)
print("\n*****************************\n")

print(f'Weather Alerts for {state}:')
if not response['features']:
    print(f'No current weather advisories for {state}')
for x in response['features']:
    print("\nArea Description:")
    print(x['properties']['areaDesc'])

    print("\nHeadline:")
    print(x['properties']['headline'])

    print("\nDescription:")
    print(x['properties']['description'])
    print("\n*********************\n")