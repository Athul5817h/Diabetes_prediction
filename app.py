
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def brain():
    try:
        # Extract form data
        age = float(request.form["age"])
        pregnancies = float(request.form["pregnancies"])
        bmi = float(request.form["bmi"])
        glucose = float(request.form["glucose"])
        blood_pressure = float(request.form["bloodpressure"])
        hba1c = float(request.form["hba1c"])
        ldl = float(request.form["ldl"])
        hdl = float(request.form["hdl"])
        triglycerides = float(request.form["triglycerides"])
        waist_circumference = float(request.form["waistcircumference"])
        hip_circumference = float(request.form["hipcircumference"])
        whr = float(request.form["whr"])
        family_history = float(request.form["familyhistory"])
        diet_type = float(request.form["diettype"])
        hypertension = float(request.form["hypertension"])
        medication_use = float(request.form["medicationuse"])

        # Prepare data for the model
        values = [
            age, pregnancies, bmi, glucose, blood_pressure, hba1c, ldl, hdl,
            triglycerides, waist_circumference, hip_circumference, whr,
            family_history, diet_type, hypertension, medication_use
        ]
        arr = [values]  # Data prepared for model prediction

        model = joblib.load("DBModel.joblib")

        # Make prediction
        prediction = model.predict(arr)

        # Return prediction result
        for i in prediction:
            if i == 1:
                return render_template("prediction.html",result_message="Person suffer from Diabetes")
            else:
                return render_template("prediction.html",result_message="Did not suffer from Diabetes")
            
        
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
 