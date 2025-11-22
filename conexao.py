import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'senai_crud'
}

def get_conexao():
    return mysql.connector.connect(**db_config)

def ler_produtos():
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, preco From produtos")
    res = cursor.fetchall()
    return res


def inserir_produto(titulo,preco):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (titulo, preco) VALUES (%s, %s)",(titulo,preco))
    conn.commit()
    conn.close()

def deletar_produtos(id_prod):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos where id = %s", (id_prod,))
    conn.commit()
    conn.close()


def editar_produtos(id_prod, titulo, preco):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = ("UPDATE produtos SET titulo=%s, preco=%s")
    cursor.execute(sql, (titulo, preco, id_prod))
    conn.commit()
    conn.close()