from flask import Flask, request, render_template, jsonify
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application
predict_pipeline=PredictPipeline()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Age=int(request.form.get('age')),
            Gender=request.form.get('gender'),
            Weight=float(request.form.get('weight')),
            Height=float(request.form.get('height')),
            Max_BPM=int(request.form.get('max_bpm')),
            Avg_BPM=int(request.form.get('avg_bpm')),
            Resting_BPM=int(request.form.get('resting_bpm')),
            Session_Duration=float(request.form.get('session_duration')),
            Workout_type=request.form.get('workout_type'),
            Fat_Percentage=float(request.form.get('fat_percentage')),
            Water_Intake=float(request.form.get('water_intake')),
            Workout_Frequency=int(request.form.get('workout_frequency')),
            Experience_Level=int(request.form.get('experience_level')),
            BMI=float(request.form.get('bmi'))
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return jsonify({
            "prediction": round(float(results[0]), 2)
        })
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        


    
