from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras
import os

# User e pass definidos no postgree 
DB_HOST = 'localhost'
DB_NAME = 'coopana' #nome do BD
DB_USER = 'postgres'  #nome user do seu BD      
DB_PASS = '123456789'   #senha do seu BD   

#Versão de conexão docker  
#DB_HOST = os.environ['DB_HOST']
#DB_NAME = os.environ['DB_DBNAME']
#DB_USER = os.environ['DB_USER']
#DB_PASS = os.environ['DB_PASS']

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
#---------------------veiculos-----------------------------------
@app.route("/veiculos")
def veiculos():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    v = "SELECT * FROM coopana.veiculos"       # Nome da tabela do bd que vai ser utilizada
    cur.execute(v)
    list_veiculos = cur.fetchall()
    return render_template('veiculos.html',list_veiculos = list_veiculos)

@app.route('/add_veiculos', methods=['POST'])         
def add_veiculos():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        #Colunas da respectiva tabela
        tipo = request.form['tipo']           
        nome = request.form['nome']
        placa = request.form['placa']
        marca = request.form['marca']
        situacao = request.form['situacao']
        ano = request.form['ano']
        valor = request.form['valor']
        cur.execute(
            "INSERT INTO coopana.veiculos (tipo,nome,placa,marca,situação,ano,valor) VALUES (%s,%s,%s,%s,%s,%s,%s)", 
            (tipo,nome,placa,marca,situacao,ano,valor))
        conn.commit()
        flash('Veiculo adicionado com Sucesso!')
        return redirect(url_for('veiculos')) 

@app.route('/editv/<id>', methods = ['POST', 'GET'])  
def get_employe(id):    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('SELECT * FROM coopana.veiculos WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editv.html', veiculos = data[0])

@app.route('/updatev/<id>', methods = ['POST'])
def update_veiculos(id):
    if request.method == 'POST':
        #Colunas da respectiva tabela
        tipo = request.form['tipo']           
        nome = request.form['nome']
        placa = request.form['placa']
        marca = request.form['marca']
        situacao = request.form['situacao']
        ano = request.form['ano']
        valor = request.form['valor']
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE coopana.veiculos
            SET tipo = %s,nome = %s,placa = %s, marca = %s,situação = %s,ano = %s,valor = %s
            WHERE id = %s 
        """, (tipo,nome,placa,marca,situacao,ano,valor, id))
        flash('Veiculo Atualizado com sucesso !')
        conn.commit()
        return redirect(url_for('veiculos'))   

@app.route('/deletev/<string:id>', methods = ['POST','GET'])
def delete_veiculos(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM coopana.veiculos WHERE id = {0}'.format(id))
    conn.commit()
    flash('Veiculo Removido com sucesso!')
    return redirect(url_for('veiculos'))
#------------------------------------------------------------------
@app.route("/cooperados")
def cooperados():
    return render_template('cooperados.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
