from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras

# User e pass definidos no postgree 
DB_HOST = 'localhost'
DB_NAME = 'coopana' #nome do BD
DB_USER = 'postgres'  #nome user do seu BD      
DB_PASS = '31081995'   #senha do seu BD     

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

app = Flask(__name__)
app.secret_key = "coopana"

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/add_licitacao', methods=['POST'])
def add_licitacao():    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        #Colunas da respectiva tabela
        financiador = request.form['financiador']           
        licitacao_destino = request.form['licitacao_destino']
        cur.execute("INSERT INTO coopana.licitacao (financiador, licitacao_destino) VALUES (%s,%s)", (financiador, licitacao_destino))
        conn.commit()
        flash('Licitação adicionada com Sucesso!')
        return redirect(url_for('licitacoes'))        #retorna pra main onde vai monstrar a tabela depois de dar INSERT 
        
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('SELECT * FROM coopana.licitacao WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', licitacao = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_licitacao(id):
    if request.method == 'POST':
        #Colunas da respectiva tabela
        financiador = request.form['financiador']           
        licitacao_destino = request.form['licitacao_destino']
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE coopana.licitacao
            SET financiador = %s,
                licitacao_destino = %s
            WHERE id = %s           
        """, (financiador, licitacao_destino, id))
        flash('Licitação Atualizada com sucesso !')
        conn.commit()
        return redirect(url_for('licitacoes'))   
        
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_licitacao(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM coopana.licitacao WHERE id = {0}'.format(id))
    conn.commit()
    flash('Licitação Removida com sucesso!')
    return redirect(url_for('licitacoes'))
        
@app.route("/funcionario")
def funcionario():
    return render_template('funcionarios.html')

@app.route("/projeto")
def projeto():
    return render_template('projetos.html')

@app.route("/licitacoes")
def licitacoes():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM coopana.licitacao"       # Nome da tabela do bd que vai ser utilizada
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('licitacoes.html', list_users = list_users)

@app.route("/veiculos")
def veiculos():
    return render_template('veiculos.html')

@app.route("/cooperados")
def cooperados():
    return render_template('cooperados.html')

app.run()
