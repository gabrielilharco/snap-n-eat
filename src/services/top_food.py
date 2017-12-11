from utils import nice_json
from flask import Flask, request
import pandas as pd
import numpy as np
from scipy.spatial import distance

from sklearn.neighbors import NearestNeighbors

NUT_DAILY_VALUES = {
    "calories": 2000,
    "carbohydrates": 300,
    #"cholesterol": 0.003,
    "fat" : 65,
    #"fiber": 25,
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

MODELS_PATH = "../../data/food-101/models/"
data_file = "../../data/nutrition_values.csv"

nutrition_df = pd.read_csv(MODELS_PATH + "../../nutrition_values.csv", header=0)

#print (nutrition_df.head())
nutrition_values_df = nutrition_df.drop(["product_name", "sugars_100g", "fiber_100g", "cholesterol_100g"], axis=1)

# normalize df
for key, val in NUT_DAILY_VALUES.items():
    column = NUT_NAMES_MAP[key]
    nutrition_values_df[column] /= val
    nutrition_values_df[column] *= 2

print(nutrition_values_df.head())

#knn = joblib.load(MODELS_PATH + "knn.pkl")


app = Flask(__name__)

w = [1, 1, 1, 1]# 0.1, 0]

def weightedL2(a,b):
    q = a-b
    return np.sqrt((w*q*q).sum())

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
    
    print (nutrition_values_df.head())
    knn = NearestNeighbors(n_neighbors=5,
                           algorithm='ball_tree',
                           metric="euclidean").fit(nutrition_values_df)
    
    distances, indices = knn.kneighbors([[(NUT_DAILY_VALUES["calories"] - calories) / NUT_DAILY_VALUES["calories"] ,
                                          (NUT_DAILY_VALUES["carbohydrates"] - carbohydrates) / NUT_DAILY_VALUES["carbohydrates"] ,
                                          (NUT_DAILY_VALUES["proteins"] - proteins) / NUT_DAILY_VALUES["proteins"] ,
                                          (NUT_DAILY_VALUES["fat"] - fat) / NUT_DAILY_VALUES["fat"]]],
                                          #NUT_DAILY_VALUES["fiber"] - fiber,
                                          #NUT_DAILY_VALUES["cholesterol"] - cholesterol]],
                                        n_neighbors=3)
    
    recommended_products = [nutrition_df.loc[i]['product_name'] for i in indices[0]]

    response_dict = {
        "recommended": recommended_products
    }
    return nice_json(response_dict)

if __name__=="__main__":
    app.run(port=5002, debug=True)
