from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculadora_energia')
def calculadora_energia():
    return render_template('calculadora_energia.html')

@app.route('/calculadora_agua')
def calculadora_agua():
    return render_template('calculadora_agua.html')

@app.route('/comparador_energia')
def comparador_energia():
    return render_template('comparador_energia.html')

@app.route('/test_ambiental')
def test_ambiental():
    return render_template('test_ambiental.html')

if __name__ == '__main__':
    app.run(debug=True)
