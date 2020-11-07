from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index(x=0):
    if x == 0:
        return render_template('index_bmi.html')
    else: 
        return render_template('index_bmi.html', BMI=x)

@app.route("/calc", methods=['POST'])
def calc():
    m = request.form['height']
    kg = request.form['weight']
    if m == '' or kg == '' : 
        return index()
    else:
        bmi = str(int(kg)/((int(m)/100)**2))
        return index(bmi)

if __name__ == "__main__":
    app.run(port=5000, debug=True)