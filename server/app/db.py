import pymongo

class DB():
    client = None
    database = None

    def connect(self):
        self.client = pymongo.MongoClient(host = 'mongo')
        return self.client
    
    def state(self):
        try:
            self.client.server_info()
        except:
            return False
        return True
    
    def getDB(self, name):
        self.database = self.client.get_database(name = name)
        return self.database
    
    def close(self):
        if self.client !=  None:
            self.client.close()