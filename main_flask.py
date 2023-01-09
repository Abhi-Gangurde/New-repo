from flask import render_template, Flask, request
app = Flask(__name__)
import pickle
import numpy as np

with open("main.pkl","rb") as file:
    main = pickle.load(file)

@app.route("/")
def cursor():
    return render_template("Loan_Status.html")

@app.route("/Entry", methods = ["POST"])
def predict():
    Gender= eval(request.form["Gender"])
    Married = eval(request.form["Married_Status"])
    Dependents = eval(request.form["Dependents"])
    Education = eval(request.form["Education"])
    Self_Employed = eval(request.form["Self_Emp"])
    ApplicantIncome = eval(request.form["Applicant Income"])
    CoapplicantIncome = eval(request.form["CoApplicant_Income"])
    LoanAmount = eval(request.form["Loan_Amount"])
    Loan_Amount_Term = eval(request.form["Loan_Amount_Term"])
    Credit_History = eval(request.form["Credit_history"])
    Property_Area = eval(request.form["Property_Area"])
    data = np.array([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area], ndmin=2)
    result = main.predict(data)
    print(result)
    if result[0] == 0:
        pred = "No, this person does not have any type of credit history"
    if result[0] == 1:
        pred = "Yes, this person having a loan"
    return render_template("Loan_Status.html", prediction = pred)

# @app.route("/login")
# def login():
if __name__ == "__main__":
    app.run(debug=True)