from pathlib import Path
import tensorflow as tf
import pandas as pd 
import numpy as np 


labels_food =  {
 'apple': 0,
 'banana': 1,
 'beetroot': 2,
 'bell pepper': 3,
 'cabbage': 4,
 'capsicum': 5,
 'carrot': 6,
 'cauliflower': 7,
 'chilli pepper': 8,
 'corn': 9,
 'cucumber': 10,
 'eggplant': 11,
 'garlic': 12,
 'ginger': 13,
 'grapes': 14,
 'jalepeno': 15,
 'kiwi': 16,
 'lemon': 17,
 'lettuce': 18,
 'mango': 19,
 'onion': 20,
 'orange': 21,
 'paprika': 22,
 'pear': 23,
 'peas': 24,
 'pineapple': 25,
 'pomegranate': 26,
 'potato': 27,
 'raddish': 28,
 'soy beans': 29,
 'spinach': 30,
 'sweetcorn': 31,
 'sweetpotato': 32,
 'tomato': 33,
 'turnip': 34,
 'watermelon': 35
 }


def process_food(): 
    user_input = Path('./user_input/inputs/')
    # print(user_input)
    user_input_filepaths = list(user_input.glob(r'**/*.jpg'))
    user_input_df = process_img(user_input_filepaths)

    data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
        preprocessing_function = tf.keras.applications.mobilenet_v2.preprocess_input
        )

    random_images = data_gen.flow_from_dataframe(
        dataframe=user_input_df,
        x_col='FilePath',
        y_col='Label',
        target_size=(224, 224),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=32,
        shuffle=True,
    )

    loaded_model = tf.keras.models.load_model('./model.h5')
    pred = loaded_model.predict(random_images) #its predicting time , our model will try to predict the prob of the particular class 
    pred = np.argmax(pred, axis=1) 
    # predicted_label = list(labels_food.keys())[pred[0]]
    # return the predicted labels as a list
    predicted_labels = [list(labels_food.keys())[pred[i]] for i in range(len(pred))]
    predicted_labels
    return predicted_labels





def process_img(filepath): # passing the filepaths of datasets
    
    labels = [str(filepath[i]).split("\\")[-1   ] #here we are trying to extract the labels for the fruits and veggies by using .split method and
              for i in range(len(filepath))] #since names are secound last word we used [-2] to get that particular name
    filepath = pd.Series(filepath, name='FilePath').astype(str)
    labels = pd.Series(labels, name='Label') 
    
    df = pd.concat([filepath, labels], axis=1) 
    df = df.sample(frac=1).reset_index(drop = True)
    
    return df

