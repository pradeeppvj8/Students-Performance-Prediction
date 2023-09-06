from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline
from src.pipeline.train_pipeline import TrainPipeline

application = Flask(__name__)

app = application

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if request.form.get("option") == 'train_model':
            train_pipeline = TrainPipeline()
            train_pipeline_successful = train_pipeline.initiate_train_pipeline()

            if train_pipeline_successful :
                return render_template('home.html')
            else :
                return render_template('index.html')
        else :
            return render_template('home.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender = request.form.get("gender"),
            race_ethnicity = request.form.get("ethnicity"),
            parental_level_of_education = request.form.get("parental_level_of_education"),
            lunch = request.form.get("lunch"),
            test_preparation_course = request.form.get("test_preparation_course"),
            reading_score = float(request.form.get("reading_score")),
            writing_score = float(request.form.get("writing_score"))
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results = results[0])
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port=8080)
