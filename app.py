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
collection= db['flask_test']

app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')

    return render_template('index.html', day=day_of_week, time=current_time)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            # Collect user input
            username = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm-password')

            # Check if any required field is empty
            if not username or not email or not password or not confirm_password:
                raise ValueError("Please fill in all fields.")  # Raise custom error if any field is missing

            # Check if password and confirm password match
            if password != confirm_password:
                raise ValueError("Passwords do not match.")
            
            # Create user dictionary
            user = {
                "username": username,
                "email": email,
                "password": password,
                "confirm_password": confirm_password
            }

            # Insert user data into MongoDB
            collection.insert_one(user)
        
        except ValueError as e:
            # Handle custom validation errors (missing fields or password mismatch)
            return f"Error: {e}"
        except ConnectionError:
            # Handle MongoDB connection issues
            return "Error: Unable to connect to the database."
        except Exception as e:
            # Handle any other unexpected errors
            return f"An unexpected error occurred: {e}"

        # If everything goes fine, redirect to success page
        return redirect(url_for('success'))

    return render_template('signup.html')

@app.route('/success')
def success():

    return ("Signup successful!")

if __name__ == '__main__':
    app.run(debug=True)