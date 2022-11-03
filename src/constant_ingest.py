import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
import time
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS

'''
List of buckets
aerosol
gamma
radiation
surface
swipe
'''

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


def insert_gama_data(location):
    data = round(random.uniform(1,5), 3)
    point = Point("gama").tag("location", location).field("doseRate", data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("gamma", point)


location='NearDrive1A'
try:
  while True:
    print("Ingesting data")
    insert_gama_data(location)

except KeyboardInterrupt:
  print("Detected Ctrl+c... Exiting Now!")
