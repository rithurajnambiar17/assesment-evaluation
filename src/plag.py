import requests
import json
import random
import string


def plag(file):
    headers = {
    'Content-type': 'application/json'
    
    }

    myobj = json.dumps({'email':'rithurajnambiar17@gmail.com','key':'34eb707b-681d-4788-a80e-d2dc3aed904d'})
    response = requests.post('https://id.copyleaks.com/v3/account/login/api', headers=headers, data=myobj)

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + str(response.json()['access_token'])
    }

    myobj = json.dumps({'base64':'SGVsbG8gd29ybGQh','filename':file, 'properties':{'webhooks':{'status':'https://rithurajnambiar17.github.io/{STATUS}'}}})

    hash1 = ''.join(random.choices(string.ascii_lowercase, k=5))

    response = requests.put(f'https://api.copyleaks.com/v3/education/submit/file/{hash1}/', headers=headers, data=myobj)
    if response.status_code == 201:
        return response
    elif response.status_code == 400:
        return response.json()