from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'OK'

@app.route('/callback', methods=['POST'])
def callback():
    # curl -X POST -d "name=John&age=30" http://localhost:5000/callback
    name = request.form['name']
    age = request.form['age']
    # do something with name and age...
    return f'Name is {name} and age is {age}'

if __name__ == '__main__':
    app.run()
