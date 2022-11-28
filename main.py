from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras

# User e pass definidos no postgree 
DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'        
DB_PASS = '1234567890'      

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

app = Flask(__name__)
app.secret_key = "coopana"

@app.route("/")
def main():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM coopana.licitação"       # Nome da tabela do bd que vai ser utilizada
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

@app.route('/add_licitação', methods=['POST'])
def add_licitação():    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        #Colunas da respectiva tabela
        financiador = request.form['financiador']           
        licitacao_destino = request.form['licitacao_destino']
        cur.execute("INSERT INTO coopana.licitação (financiador, licitacao_destino) VALUES (%s,%s)", (financiador, licitacao_destino))
        conn.commit()
        flash('Licitação adicionada com Sucesso!')
        return redirect(url_for('main'))        #retorna pra main onde vai monstrar a tabela depois de dar INSERT 
        
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('SELECT * FROM coopana.licitação WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', licitação = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_licitação(id):
    if request.method == 'POST':
        #Colunas da respectiva tabela
        financiador = request.form['financiador']           
        licitacao_destino = request.form['licitacao_destino']
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE coopana.licitação
            SET financiador = %s,
                licitacao_destino = %s
            WHERE id = %s           
        """, (financiador, licitacao_destino, id))
        flash('Licitação Atualizada com sucesso !')
        conn.commit()
        return redirect(url_for('main'))   
        
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_licitação(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM coopana.licitação WHERE id = {0}'.format(id))
    conn.commit()
    flash('Licitação Removida com sucesso!')
    return redirect(url_for('main'))
        
@app.route("/funcionario")
def funcionario():
    return render_template('funcionarios.html')

@app.route("/projeto")
def projeto():
    return render_template('projetos.html')

@app.route("/licitacao")
def licitacao():
    return render_template('licitacoes.html')

@app.route("/veiculos")
def veiculos():
    return render_template('veiculos.html')

@app.route("/cooperados")
def cooperados():
    return render_template('cooperados.html')

app.run()
