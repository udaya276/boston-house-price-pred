from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__)


@app.route("/")
def loadPage():
	return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    query1 = float(request.form['query1'])
    query2 = float(request.form['query2'])
    query3 = float(request.form['query3'])
    query4 = float(request.form['query4'])
    query5 = float(request.form['query5'])
    query6 = float(request.form['query6'])
    query7 = float(request.form['query7'])
    query8 = float(request.form['query8'])
    query9 = float(request.form['query9'])
    query10 = float(request.form['query10'])
    query11 = float(request.form['query11'])
    query12 = float(request.form['query12'])
    query13 = float(request.form['query13'])

    data  = [[query6,query13]]
    new_df = pd.DataFrame(data)
    model = pickle.load(open("model1.sav", "rb"))
    price = float(model.predict(new_df))
    
    output="Prediction price is: {}".format(price)


    return render_template('home.html', output1=output, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'], query7 = request.form['query7'],query8 = request.form['query8'],query9 = request.form['query9'],query10 = request.form['query10'],query11 = request.form['query11'], query12 = request.form['query12'],query13 = request.form['query13'])
    #return render_template('home.html', output1=price)

"""
@app.route("/via_postman", methods=["post"])
def boston_price_prediction():
    if (request.method=='POST'):
        CRIM = float(request.json["CRIM"])
        ZN = float(request.json["ZN"])
        INDUS = float(request.json["INDUS"])
        CHAS = float(request.json["CHAS"])
        NOX = float(request.json["NOX"])
        RM = float(request.json["RM"])
        AGE = float(request.json["AGE"])
        DIS = float(request.json["DIS"])
        RAD = float(request.json["RAD"])
        TAX = float(request.json["TAX"])
        PTRATIO = float(request.json["PTRATIO"])
        B = float(request.json["B"])
        LSTAT = float(request.json["LSTAT"])

        data  = [[LSTAT,RM]]
        new_df = pd.DataFrame(data)
        model = pickle.load(open("model1.sav", "rb"))
        price = model.predict(new_df)
        return(jsonify(float(price)))
"""

if __name__ == "__main__":
    app.run(debug=True)
