from __future__ import print_function
import json
import urllib2 
import os
import sys
from sys import argv

key = sys.argv[1]
busline = sys.argv[2]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key,busline)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

dataDict = json.loads(data)


busdata = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
max_ = len(busdata)

print ('Bus Line: ', busline)
print ('Number of Active Buses: ', max_)
for i in range(0,max_):
    locatinfro = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    latitude = locatinfro.get('Latitude', 'N/A')  
    longitude = locatinfro.get('Longitude', 'N/A')
    print ('Bus',i, 'is at latitude', latitude, 'and longitude', longitude)
