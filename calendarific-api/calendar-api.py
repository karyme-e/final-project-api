from flask import Flask, render_template
import requests

app = Flask('__name__')

@app.route("/")
def get_holidays():
    url = 'https://calendarific.com/api/v2/holidays?api_key=lyaHHqfd1ixEesSTLhGnBA5R6ix1gDr1&receiveParameters'

    response = requests.get(url,
    params = {
     # Required
        'country': 'US',
         'year':  2023,
        'type': 'national'
    }

    )

    print(response.status_code)

    #holidays = response.json()["response"]["holidays"]
     #holidays_names = [h["name"] for h in holidays]

    holidays = response.json()["response"]["holidays"]
    holidays_info = [
            {
                'name': h["name"],
                'description': h.get("description", "No description available"),
                'date': h["date"]["iso"]
            }
            for h in holidays
        ]
    
    #return holidays_names

    #return render_template ("calendar-api.jinja", holidays_names = holidays_names)
    return render_template ("holidays_info.jinja" , holidays_info=holidays_info)

    