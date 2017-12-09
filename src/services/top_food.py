from utils import nice_json
from flask import Flask, request
import pandas

import pickle

MODEL_PATH = "/home/ubuntu/dl_hackathon/data/food-101/"
df = pandas.read_csv(csv_path)

products = df['product_name'].unique()

app = Flask(__name__)

@app.route("/",  methods=['POST'])
def similar_foods():
    product_name = request.args.get('product_name')
    calories = request.args.get('calories')
    carbohydrates = request.args.get('cholesterol')
    fat = request.args.get('fat')
    fiber = request.args.get('fiber')
    proteins = request.args.get('proteins')
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    if product_name not in products:
        return nice_json({})
    dic = df.loc[df['product_name'] == product_name].to_dict()
    for key, val in dic.items():
        dic[key] = val[next(iter(val))]
    return nice_json(dic)

if __name__=="__main__":
    app.run(port=5002, debug=True)
