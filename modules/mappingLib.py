import urllib.request
from urllib.parse import urlencode
from math import ceil
import json

def distance_calculator(origin, dest):
    ## 1 mile = 1609.34 meters
    query_args = {'origins': origin, 'destinations': dest, 'units': 'imperial', 'key': 'AIzaSyA3tRoRrMbrlYye-TRxBl7Lwev6HVx5ZSI'}
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    requestUrl = base_url + urlencode(query_args, doseq=True)
    output = {}
    try:
        data = urllib.request.urlopen(requestUrl)
        response = json.load(data)
    except:
        raise ValueError('Could not open URL')
    try:
        distance = response['rows'][0]['elements'][0]['distance']['value']
    except KeyError:
        raise ValueError("Location Not Found or other error; GMaps API message:", response['status'])

    if type(distance) != int or distance <= 0:
        raise ValueError('There must be a separation of more than 1 mile between origin and destination')
    else:
        distance = round(distance/1609.34, 2)
        output = {'dest': response['destination_addresses'][0], 'origin': response['origin_addresses'][0], 'distance': distance}
        return output

def cost_calculator(d, weight=None, length=None, width=None, height=None):
    if weight:
        weight += 0.00000001
        weight = ceil(weight)
    else:
        weight = 1
    cost = 18 + d + weight
    return cost
"""
d = distance_calculator('willis tower', 'brookfield zoo')['distance']
print(d)
print(cost_calculator(d))
"""