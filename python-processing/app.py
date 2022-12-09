from flask import Flask
from waitress import serve
from receiveImg import process_image_from_url

# import the welcome function from welcome.py
app = Flask(__name__)


@app.route('/')
def hello():
    # display values from process_food function as a string
    return ('Hello World')


@app.route('/post/image', methods=['POST'])
# receive the image from the raspberry pi POST request
def receiveImg():
    # return the recognized food from the image
    return process_image_from_url()


if __name__ == '__main__':
    # run the app.
    serve(app, host='0.0.0.0', port=5000)
