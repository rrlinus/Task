import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Insert pending data into
# pending database
def Insert(databaseName,table, id):
    mydb = myclient[databaseName]
    mycol = mydb[table]
    mycol.insert({"_id": id})


# If current _id is in pending state
def QueryForPending(databaseName, table, id):
    mydb = myclient[databaseName]
    mycol = mydb[table]
    myquery = {"_id": id}
    try:
        mydoc = mycol.find(myquery)[0]
    except:
        params = {
            "status": 404,
            "Message": "NOT FOUND"
        }
        return params
    params = {
        "status": 200,
        "Message": "Please Wait..."
    }
    return params


# If current processed id is in success state
def QueryForSuccess(databaseName, table, id):
    mydb = myclient[databaseName]
    mycol = mydb[table]
    myquery = {"_id": id}
    mydoc = mycol.find(myquery)[0]

    params = {
        "result": mydoc['result'],
        "status":mydoc['status']
    }

    return params


