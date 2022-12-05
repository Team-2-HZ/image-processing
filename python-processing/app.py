from flask import Flask
from waitress import serve  
from processImg import process_food

# import the welcome function from welcome.py
app = Flask(__name__)

@app.route('/')
def hello( ):
    # display values from process_food function as a string
    return str(process_food())

if __name__ == '__main__':
    # run the app.
    serve(app, host='0.0.0.0', port=5000)