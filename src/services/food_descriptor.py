from utils import nice_json
from flask import Flask, request
import pandas

csv_path = '/home/ubuntu/dl_hackathon/data/nutrition_values.csv'
df = pandas.read_csv(csv_path)

products = df['product_name'].unique()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def describe():
    product_name = request.args.get('product_name')
    if product_name not in products:
        return nice_json({})
    dic = df.loc[df['product_name'] == product_name].to_dict()
    for key, val in dic.items():
        dic[key] = val[next(iter(val))]
    return nice_json(dic)

if __name__=="__main__":
    app.run(port=5001, debug=False)
