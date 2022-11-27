from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/funcionario")
def funcionario():
    return render_template('funcionarios.html')

@app.route("/projeto")
def projeto():
    return render_template('funcionarios.html')

@app.route("/licitacao")
def licitacao():
    return render_template('funcionarios.html')

@app.route("/veiculos")
def veiculos():
    return render_template('funcionarios.html')

@app.route("/cooperados")
def cooperados():
    return render_template('cooperados.html')

app.run()