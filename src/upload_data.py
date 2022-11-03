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

def insert_surface_data(location):
    data = round(random.uniform(1,5), 3)
    point = Point("surface").tag("location", location).field("doseRate", data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("surface", point)

def insert_aerosol_data(location):
    data = round(random.uniform(1,5), 3)
    data2 = round(random.uniform(1,5), 3)
    point = Point("aerosol").tag("location", location).field("alpha", data).field("beta",data2).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("aerosol", point)

def insert_swipe_data(location):
    data = round(random.uniform(1,5), 3)
    data2 = round(random.uniform(1,5), 3)
    point = Point("swipe").tag("location", location).field("alpha", data).field("beta",data2).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("swipe", point)

def insert_radiation_data(location):
    data = round(random.uniform(1,5), 3)
    point = Point("radiation").tag("location", location).field("value", data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("radiation", point)

counter=0
location="entrance1"
while counter < 20:
    insert_gama_data(location)
    insert_surface_data(location)
    insert_aerosol_data(location)
    insert_swipe_data(location)
    insert_radiation_data(location)
    print("Datapoint: "+str(counter)+" added")
    counter += 1
