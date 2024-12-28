from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#URL
url = "mongodb+srv://Username:<Password>@phishing.hbsdoeq.mongodb.net/?retryWrites=true&w=majority&appName=phishing"

#create a new client and connect to server
client = MongoClient(url)

DATABASE_NAME = "pwskills"

COLLECTION_NAME = "waferfault"

df = pd.read_csv("/content/wafer_fault.csv")
df = df.drop("Unnamed: 0",axis = 1)

json_record = list(json.loads(df.T.to_json()).values())

# uploading json data to mongodp

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)