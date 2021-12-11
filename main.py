import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

myConnection = "mongodb+srv://loan:loan123456@cluster0.cqrpj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(myConnection)
db = client.myFirstDatabase
people = db.student


def findAll():
    return people.find()


def testConnectDB():
    try:
        return client.server_info()
    except Exception:
        return "Unable connect to server"


@app.get("/")
async def root():
    return {"messenger": "Hello wold"}


@app.get("/test")
async def test():
    result = list()
    for x in people.find({}, {"_id": 0, "MSV": 1, "Name": 1}):
        result.append(str(x))
    return {"result": result}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)


