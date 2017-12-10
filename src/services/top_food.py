from utils import nice_json
from flask import Flask, request
import pandas as pd

from sklearn.externals import joblib

NUT_DAILY_VALUES = {
    "calories": 2000,
    "carbohydrates": 300,
    "cholesterol": 0.003,
    "fat" : 65,
    "fiber": 25,
    "proteins": 50
}

NUT_NAMES_MAP = {
    "calories" : "energy_100g",
    "carbohydrates": "carbohydrates_100g",
    "cholesterol": "cholesterol_100g",
    "fat" : "fat_100g",
    "fiber": "fiber_100g",
    "proteins": "proteins_100g"
}

MODELS_PATH = "/home/ubuntu/dl_hackathon/data/food-101/models/"

nutrition_df = pd.read_csv(MODELS_PATH + "../../nutrition_values.csv", header=0)

knn = joblib.load(MODELS_PATH + "knn.pkl")


app = Flask(__name__)

@app.route("/",  methods=['POST'])
def similar_foods():
    # product_name = request.form.get('product_name')
    calories = float(request.form.get('calories'))
    cholesterol = float(request.form.get('cholesterol'))
    carbohydrates = float(request.form.get('carbohydrates'))
    fat = float(request.form.get('fat'))
    fiber = float(request.form.get('fiber'))
    proteins = float(request.form.get('proteins'))
    
    # TODO Check if any parameter is None
    print(calories);
    print(carbohydrates);
    
    distances, indices = knn.kneighbors([[NUT_DAILY_VALUES["calories"] - calories,
                                          NUT_DAILY_VALUES["carbohydrates"] - carbohydrates,
                                          NUT_DAILY_VALUES["proteins"] - proteins,
                                          NUT_DAILY_VALUES["fat"] - fat,
                                          NUT_DAILY_VALUES["fiber"] - fiber,
                                          NUT_DAILY_VALUES["cholesterol"] - cholesterol]],
                                        n_neighbors=3)
    
    recommended_products = [nutrition_df.loc[i]['product_name'] for i in indices[0]]

    response_dict = {
        "recommended": recommended_products
    }
    return nice_json(response_dict)

if __name__=="__main__":
    app.run(port=5002, debug=True)
