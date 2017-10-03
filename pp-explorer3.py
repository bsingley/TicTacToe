import requests
import datetime
import json

#this script would be used to print out the eng status detail

url="https://pp.engineering.redhat.com/pp/api/latest/releases-eng-statuses/"
response = requests.get(url,headers=dict(Accept='application/json'), verify=False)
json_obj=  response.json()

print json_obj


print "####################################################"
print "####################################################"
print "####################################################"
print "####################################################"

a=1
for obj in json_obj:

    print obj['id'], " : ",#  obj['name']," : ", obj['ga_date'], " : ",
    print obj['eng_status_color'], " : ", obj["eng_status_text"]
    print "*******************"
