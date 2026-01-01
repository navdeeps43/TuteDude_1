from flask import Flask, redirect, request, render_template, url_for
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri= os.getenv("uri")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db= client.test
collection= db['to_do_items']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submittodoitems', methods=['POST'])
def submittodoitems():
    if request.method == 'POST':
            
            # Collect user input
            itemname = request.form.get('itemname')
            itemdescription = request.form.get('itemdescription')


            item = {
                "itemname": itemname,
                "itemdescription": itemdescription
            }

            # Insert user data into MongoDB
            collection.insert_one(item)


    return "item inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)