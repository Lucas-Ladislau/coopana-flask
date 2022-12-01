from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras
import os

# User e pass definidos no postgree 
DB_HOST = 'localhost'
DB_NAME = 'coopana' #nome do BD
DB_USER = 'postgres'  #nome user do seu BD      
DB_PASS = '31081995'   #senha do seu BD   

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

@app.route("/licitacoes")
def licitacoes():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM coopana.licitacao"       # Nome da tabela do bd que vai ser utilizada
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('licitacoes.html', list_users = list_users)
        
@app.route("/funcionario")
def funcionario():
    return render_template('funcionarios.html')

@app.route("/cooperados")
def cooperados():
    return render_template('cooperados.html')


#---------------------veiculos-----------------------------------
@app.route("/veiculos")
def veiculos():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    v = "SELECT * FROM coopana.veiculos"       # Nome da tabela do bd que vai ser utililorzada
    cur.execute(v)
    list_veiculos = cur.fetchall()
    return render_template('veiculos.html',list_veiculos = list_veiculos)

#a implementação de situação é feita na regra de negócio em transporte
@app.route('/add_veiculos', methods=['POST'])         
def add_veiculos():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        #Colunas da respectiva tabela
        tipo = request.form['tipo']           
        placa = request.form['placa']
        marca = request.form['marca']
        situacao = False
        ano = request.form['ano']
        cur.execute(
            "INSERT INTO coopana.veiculos (tipo,placa,marca,situacao,ano) VALUES (%s,%s,%s, %s,%s)", 
            (tipo,placa,marca,situacao,ano))
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
        placa = request.form['placa']
        marca = request.form['marca']
        ano = request.form['ano']
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE coopana.veiculos
            SET tipo = %s,placa = %s, marca = %s,ano = %s
            WHERE id = %s 
        """, (tipo,placa,marca,ano, id))
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


#----------------------PROJETO------------------------------

@app.route("/projeto")
def projeto():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    v = "SELECT * FROM coopana.projeto"       # Nome da tabela do bd que vai ser utililorzada
    cur.execute(v)
    list_projetos = cur.fetchall()
    return render_template('projetos.html',list_projetos = list_projetos)

@app.route('/add_projetos', methods=['POST'])         
def add_projetos():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        #Colunas da respectiva tabela
        nome = request.form['nome']           
        sigla = request.form['sigla']
        cur.execute(
            "INSERT INTO coopana.projeto (nome,sigla) VALUES (%s,%s)", 
            (nome, sigla))
        conn.commit()
        flash('Projeto adicionado com Sucesso!')
        return redirect(url_for('projeto'))

@app.route('/editp/<id>', methods = ['POST', 'GET'])  
def get_projetoID(id):    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('SELECT * FROM coopana.projeto WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editp.html', projeto = data[0])

@app.route('/updatep/<id>', methods = ['POST'])
def update_projeto(id):
    if request.method == 'POST':
        #Colunas da respectiva tabela
        nome = request.form['nome']           
        sigla = request.form['sigla']
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE coopana.projeto
            SET nome = %s,sigla = %s WHERE id = %s 
        """, (nome,sigla,  id))
        flash('Projeto Atualizado com sucesso !')
        conn.commit()
        return redirect(url_for('projeto'))

@app.route('/deletep/<string:id>', methods = ['POST','GET'])
def delete_projeto(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM coopana.projeto WHERE id = {0}'.format(id))
    conn.commit()
    flash('Projeto Removido com sucesso!')
    return redirect(url_for('projeto'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
