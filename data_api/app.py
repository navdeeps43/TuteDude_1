from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/api')

def api():
    name = request.values.get('name')
    age = request.values.get('age')

    result = {
        'name': name,
        'age': age,
        'message': f'Hello, {name}! You are {age} years old.'
    }
    with open('data.txt', 'w') as f:
        f.truncate(0)
        f.write(str(result) + '\n')
        f.close
    data = open('data.txt', 'r')
    f.close
    return data.read()

if __name__ == '__main__':
    app.run(debug=True)