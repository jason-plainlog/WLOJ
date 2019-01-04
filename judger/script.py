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
    print("Can't connect to mongo, retry in 1 sec!")
    time.sleep(1)

db = mongo['wloj']
queue = db['queue']

while not queue.count():
    print("No submission in queue now, recheck in 1 sec!")
    time.sleep(1)