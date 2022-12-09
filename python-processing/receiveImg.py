from flask import request, jsonify
from processImg import process_food_from_image
from PIL import Image


def process_image_from_url():
    file = request.files['file']
    # get weight from request
    weight = request.form['weight']
    # Read the image via file.stream
    img = Image.open(file.stream)
    # save image to disk
    img.save('./user_input/inputs/image_1.jpg')
    # process the image with the pre-trained model
    img = process_food_from_image()
    # return the processed image
    data = {'food': img[0], 'grams': weight}
    return data
