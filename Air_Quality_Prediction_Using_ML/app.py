from flask import Flask,request, render_template
import numpy as np
import pickle
import sklearn
print(sklearn.__version__)
#loading models
dtr = pickle.load(open('dtr.pkl','rb'))

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_air_quality_category(pm25):
    if pm25 <= 12:
        return "Good"
    elif 12 < pm25 <= 35.4:
        return "Moderate"
    elif 35.5 < pm25 <= 55.4:
        return "Unhealthy for Sensitive Groups"
    elif 55.5 < pm25 <= 150.4:
        return "Unhealthy"
    elif 150.5 < pm25 <= 250.4:
        return "Very Unhealthy"
    else:
        return "Hazardous"
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = request.form['Year']
        Month = request.form['Month']
        Day = request.form['Day']
        Hour = request.form['Hour']
        Day_of_Week = request.form['Day_of_Week']
        Season = request.form['Season']

        
    
        features = np.array([[Year, Month, Day, Hour, Day_of_Week, Season]])
        
        
        prediction = dtr.predict(features)
        air_quality_category = get_air_quality_category(prediction)

        return render_template('index.html',prediction = prediction,air_quality_category=air_quality_category)

if __name__=="__main__":
    app.run(debug=True)