# API endpoints

---

### /post/image

#### Method: POST

- Sends the image that needs to be processed to the, along with the weight of the product, to the image processing model.
- Request example:

  ```json
  {
    "files": {
      "imgFile": {
        "file": "path_to_image_file"
      }
    },
    "data": { "weight": "500" }
  }
  ```

#### Response example

```json
{
  "foodName": "Mango",
  "foodId": "food_an1dqoib8xj3tyb3pr7c0abi4rbw",
  "foodMeasures": {
    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
    "label": "Gram",
    "weight": 1
  },
  "quantity": 200,
  "ENERC_KCAL": {
    "calories": 120,
    "unit": "kcal"
  },
  "FAT": {
    "fat": 0.76,
    "unit": "g"
  },
  "PROTEIN": {
    "protein": 1.64,
    "unit": "g"
  },
  "SUGAR": {
    "sugar": 27.32,
    "unit": "g"
  },
  "CARBS": {
    "carbs": 29.96,
    "unit": "g"
  },
  "cautions": ["SULFITES"]
}
```
