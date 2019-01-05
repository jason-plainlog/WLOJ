import subprocess
import pymongo
import psutil
import time

mongo = pymongo.MongoClient(host = 'mongo')

def mongoConnected():
    try:
        mongo.server_info()
    except:
        return False
    return True

while not mongoConnected():
    print("Can't connect to MongoDB, retry in 1 sec!")
    time.sleep(1)
print("Connected to MongoDB!")

db = mongo['WLOJ']
queue = db['queue']

while not queue.count():
    print("No submission pending in queue, retry in 10 sec!")
    time.sleep(10)