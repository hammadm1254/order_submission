import urllib.request
from urllib.parse import urlencode
import json

def cost_calculator(origin, dest):
    ## 1 mile = 1609.34 meters
    query_args = {'origins': origin, 'destinations': dest, 'units': 'imperial', 'key': 'AIzaSyA3tRoRrMbrlYye-TRxBl7Lwev6HVx5ZSI'}
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    requestUrl = base_url + urlencode(query_args, doseq=True)
    output = {}
    try:
        data = urllib.request.urlopen(requestUrl)
        response = json.load(data)
    except:
        raise ValueError('Could not open URL, Check API key')
    try:
        distance = response['rows'][0]['elements'][0]['distance']['value']
    except KeyError:
        raise ValueError("Location Not found")

    if type(distance) != int or distance <= 0:
        raise ValueError('There must be a separation of more than 1 mile between origin and destination')
    else:
        distance = round(distance/1609.34, 2)
        output = {'dest': response['destination_addresses'][0], 'origin': response['origin_addresses'][0], 'distance': distance}
        return output

#print(cost_calculator('fuckthis', 'cyyz'))