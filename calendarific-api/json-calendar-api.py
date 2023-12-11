import requests

url = 'https://calendarific.com/api/v2/holidays?api_key=lyaHHqfd1ixEesSTLhGnBA5R6ix1gDr1'

response = requests.get(url+'&receiveParameters',
params = {
    # Required
    'country': 'US',
    'year':  2005,
    'type': 'national'
    }

)
#print(response.json())

#data = response.text

#json.loads(data)                

print(response.status_code)

holidays = response.json()["response"]["holidays"]

for h in holidays:
    print(h["name"])
    
#holidays_names = []

#for h in holdiays:
  #  holdiays_names.append(h["name"])
    

holidays_names = [h["name"] for h in holidays]