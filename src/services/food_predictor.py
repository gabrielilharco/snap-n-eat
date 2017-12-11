import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from fastai.imports import *
from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *
import glob
import imghdr

UPLOAD_FOLDER = '../../data/food-101/test/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Model stuff
PATH = "../../data/food-101/"
sz=224
arch=resnext101

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/path", methods=["POST"])
def predict():
    filepath = request.data.decode("utf-8").split("=")[1]

    # cleaning test dir
    files = glob.glob(UPLOAD_FOLDER+'*')
    for f in files:
        os.remove(f)
    
    ext = imghdr.what(filepath)
    os.rename(filepath, os.path.join(app.config['UPLOAD_FOLDER'], "batata." + ext))

    data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz), test_name='test')
    learn = ConvLearner.pretrained(arch, data, precompute=True, xtra_fc=[512, 512], ps=0.5)
    learn.load('better_model')
    learn.precompute=False # We'll pass in a raw image, not activations
    preds = learn.predict(is_test=True)
    top_preds = preds[0].argsort()[-5:][::-1] # get top 5 predictions
    top_pred_names = [data.classes[i] for i in top_preds]

    return jsonify(predictions=top_pred_names)
    
@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print(request)
            print(request.files)
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # cleaning test dir
            files = glob.glob(UPLOAD_FOLDER+'*')
            for f in files:
                os.remove(f)
            
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            
            data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz), test_name='test')
            learn = ConvLearner.pretrained(arch, data, precompute=True, xtra_fc=[512, 512], ps=0.5)
            learn.load('better_model')
            learn.precompute=False # We'll pass in a raw image, not activations
            preds = learn.predict(is_test=True)
            top_preds = preds[0].argsort()[-5:][::-1] # get top 5 predictions
            top_pred_names = [data.classes[i] for i in top_preds]
            
            return jsonify(predictions=top_pred_names)

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
