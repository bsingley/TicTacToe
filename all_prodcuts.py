#!/usr/bin/env python
# title: all_products.py
# description: Exploring pp api-this one prints details of products in pp.
# author: snanda
# usage : python copy_templateData.py
# notes : N/A
# python_version: 2.7.5



import requests
import datetime
import json

# this script will get all the products

url = "https://pp.engineering.redhat.com//pp/api/latest/products/"

response = requests.get(url,headers=dict(Accept='application/json'), verify=False)
json_obj=  response.json()

#print json_obj # list of dictionaries

print "####################################################"
print "####################################################"
#print len(json_obj) #lenght of list

for obj in json_obj:
    print obj['name'], " - ", obj['id']," - ", obj['shortname'], "-", obj["platforms"]
    print "*******************"

print "####################################################"
print "####################################################"
