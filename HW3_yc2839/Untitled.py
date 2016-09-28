
# coding: utf-8

# In[3]:

from __future__ import print_function
import json
import urllib2 
import os
import sys
from sys import argv

key = '33d4708c-de08-4742-807d-15690491f3d4'
busline = 'B54'


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


# In[13]:

from __future__ import print_function
import json
import urllib2 
import os
import sys

key = '33d4708c-de08-4742-807d-15690491f3d4'
busline = 'B54'

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key,busline)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

dataDict = json.loads(data)


busdata = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
max_ = len(busdata)

#fout = open(sys.argv[3], "w")
for i in range(0, max_):
    
    locatinfro = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    locatinfro_1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
    locatinfro_2 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']
    latitude = locatinfro.get('Latitude', 'N/A')  
    longitude = locatinfro.get('Longitude', 'N/A')
    StopPointName = locatinfro_1.get('StopPointName', 'N/A')
    PresentableDistance = locatinfro_2.get('PresentableDistance','N/A')
    print(latitude, longitude, StopPointName, PresentableDistance)


# In[ ]:



