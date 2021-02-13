import requests
import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import auth
"""
    Retrieve the temperature data from a Netatmo Weather Station and find the value
    Request Arguments:
        - Headers: Authorization
        - Parameters: device_id, module_id, scale=max, type=temperature, date_begin, date_end, optimize, real_time
"""

token_properties = ['access_token', 'expires_in', 'refresh_token']
req_properties = ['device_id', 'module_id', 'scale', 'type', 'date_begin', 'date_end', 'optimize', 'real_time']
current_time = round(int(datetime.datetime.now().timestamp()))
date_begin = str(current_time - 24*7*3600)
date_end = str(current_time)
req_value = ['70:ee:50:3f:13:36', '02:00:00:3f:0a:54', 'max', 'temperature', date_begin, date_end, 'false', 'false']
base_url = 'https://api.netatmo.com/api/getmeasure'
# List of parameters for GET request
parameters = dict()
headers = dict()

def set_API(token):
    """ Set the necessary parameters and headers
    """
    for i in range(len(req_properties)):
        parameters[req_properties[i]] = req_value[i]
    #access_token = token['access_token']
    access_token = token
    headers['Authorization'] = f'Bearer {access_token}'
    return

def temp_plot(temp):
    """ Draw a temperature plot for the last 7 days
    """
    x = list(temp.keys())
    y = list(temp.values())
    y2 = [np.mean(y)]*len(y)
    y = np.round(y)
    plt.plot(x, y, 'bo-', label='Temperature')
    plt.plot(x, y2, 'r--', label='Average', alpha=0.3)
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.ylim([min(y)-5, max(y)+5])
    plt.legend()
    plt.show()
    return

def calculate(data):
    items = data['body'].items()
    temp_by_date = dict()
    avg_temp_by_date = dict()
    for k, v in items:
        tmp = int(k)
        d = str(datetime.datetime.fromtimestamp(tmp)).split(' ')[0]
        if d not in temp_by_date:
            temp_by_date[d] = v
        else:
            temp_by_date[d].append(v[0])
    for k in temp_by_date.keys():
        avg_temp_by_date[k] = np.mean(temp_by_date[k])
    avg_temp = np.mean(list(avg_temp_by_date.values()))

    print(f'Average temperature last 7 days: {np.round(avg_temp, 0):.0f} degree(s) C')
    temp_plot(avg_temp_by_date)
    return avg_temp

print(f'Getting data from {datetime.datetime.fromtimestamp(int(date_begin))} to {datetime.datetime.fromtimestamp(int(date_end))}')
credentials = None
token = dict()
if len(sys.argv) == 1:
    credentials = auth.get_input()
else:
    credentials = auth.get_input(sys.argv[1])

err = 0
try:
    token[token_properties[0]], token[token_properties[1]], token[token_properties[2]] = auth.authentication(credentials)
    err = 1
    set_API(token[token_properties[0]])
    data_req = requests.get(base_url, headers=headers, params=parameters).json()
    calculate(data_req)
except:
    if err == 0:
        print('Failed to get access token!')
    else:
        print('Failed to retrieve the data!')



