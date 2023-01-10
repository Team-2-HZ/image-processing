from flask import request, jsonify
from processImg import process_food_from_image
from PIL import Image
import requests

bearerTkn = 'miTQ1NwbocCI?A2uyop1?VN=l3wh?kebR6WuepYJCOFfzWqGImXfiO/Ksed5pAxQBP8km8qU!6RmhehCPlF5D7TZm?R8w4bH8JpQXxrgABVDfAHyC9yBp3M2zxCQN13-oSf-fJhqjY-X9HlyMyq6y3Rm486eOx5VGWt!upDx-Y3CorzLs747otpnGEcfOQozNoSzJqlC!PZGypR22j/2DD1jzuCml!eHjfkX=sT8lQYqabuOnAJ/fhI6HKdo1p0X'
apiUrl = 'https://nutrition-calculation-app.onrender.com/api/v1/nutrition'


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
    data = {'food': img[0], 'grams': int(weight)}

    # make a post to the API
    response = requests.post(
        apiUrl,
        json={"data": data},
        headers={"Authorization": f"Bearer {bearerTkn}"})

    return response.json()
