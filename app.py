from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/HumanResource")
def HumanResource():
    return render_template('HR.html')

@app.route("/Marketing")
def Marketing():
    return render_template('Marketing.html')

@app.route("/Operations")
def Operations():
    return render_template('Operations.html')

@app.route("/Sales")
def Sales():
    return render_template('Sales.html')

@app.route("/PublicRelations")
def PublicRelations():
    return render_template('Public_relations.html')

@app.route("/Data_science_more")
def Data_science_more():
    return render_template('Data_science_more.html')

@app.route("/Maintainance")
def Maintainance():
    return render_template('Maintainance.html')

if __name__ == "__main__": 
    app.run(debug=True)