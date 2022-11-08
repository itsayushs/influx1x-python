
import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
import time
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS


username = 'admin'
password = 'password'
retention_policy = 'autogen'
org='-'

def ingest_data(database, point):
    with InfluxDBClient(url='http://localhost:8086', token=f'{username}:{password}', org='-') as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
    bucket = f'{database}/{retention_policy}'
    write_api.write(bucket, org, point)
    time.sleep(2)



def insert_geo_radiation_data(sensorName, lat, long):
    data = round(random.uniform(1,5), 3)
    point = Point("geodata").tag("sensor", sensorName).field("lat", lat).field("long",long).field("value",data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("geodata", point)

'''

sensorName = 'aerosol'

# Delhi
lat = 28.644800
long = 77.216721
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# LKO
lat = 26.850000
long = 80.949997
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# Udaipur
lat = 24.794500
long = 73.055000
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# Jaipur
lat = 26.922070
long = 75.778885
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# Mumbai
lat = 19.076090
long = 72.877426
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# Hyd
lat = 17.387140
long = 78.491684
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# daman
lat = 20.397373
long = 72.832802
insert_geo_radiation_data(sensorName, lat, long)
print('Added')

'''

sensorName = 'radiation'

# Delhi
lat = 28.654800
long = 77.233721
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# LKO
lat = 26.895000
long = 80.955997
insert_geo_radiation_data(sensorName, lat, long)
print('Added')
# Udaipur
lat = 24.798500
long = 73.035000
insert_geo_radiation_data(sensorName, lat, long)
print('Added')


# counter=0

# while counter < 4:
#     insert_geo_radiation_data(sensorName, lat, long)
#     print("Datapoint: "+str(counter)+" added")
#     counter += 1