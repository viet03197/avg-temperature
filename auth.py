import getpass
import json
import requests
import base64

base_url = 'https://api.netatmo.com/oauth2/token'
grant_type = 'password'
scope = 'read_station'
token_properties = ['access_token', 'expires_in', 'refresh_token']

def get_input(file=None):
    credentials = ['', '', '', '']
    if file is None:
        credentials[0] = getpass.getpass(prompt='Your client id:')
        credentials[1] = getpass.getpass(prompt='Your client secret:')
        credentials[2] = getpass.getpass(prompt='Your username:')
        credentials[3] = getpass.getpass(prompt='Your password:')
    else:
        count = 0
        with open(file) as f:
            try:
                for line in f:
                    credentials[count] = line.rstrip()
                    count +=1                    
            except:
                print('Invalid input file!')
    return credentials

def authentication(credentials):
    if len(credentials) != 4:
        return
    data = {
        'grant_type'    : grant_type,
        'client_id'     : credentials[0],
        'client_secret' : credentials[1],
        'username'      : credentials[2],
        'password'      : credentials[3],
        'scope'         : scope
    }
    token = requests.post(base_url, data=data).json()
    if 'error' in token:
        print(token)
        return
    else:
        print('Authentication Successful!')
        return token[token_properties[0]], token[token_properties[1]], token[token_properties[2]]
