from mysql.connector import connect,Error
class Conexao:
    def __init__(self,host='localhost', user='root', pwd='', db='db_cadastro'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        # self.conexao = conexao
        # self.cursor = cursor
    def conecta(self):
        try:
            self.conexao = connect(host=self.host,user=self.user,
                              password=self.pwd,database=self.db)
            self.cursor = self.conexao.cursor()
        except Error as erro:
            print('Erro no conecta', erro)
    def executar(self, sql):
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            return registros
        except Error as erro:
            print('Erro no execute', erro)
from sql import Conexao
if __name__ == '__main__':
    o_conexao = Conexao()
    o_conexao.conecta()
    print(o_conexao)
    sql = "select * from td_cargo"
    lista = o_conexao.executar(sql)
    print("Dados na horizontal")
    print(lista)
    print("Dados na vertical")
    for reg in lista:
        print(f'idt {reg[0]}, {reg[1]}')
    insert = "insert into td_cargo "
    insert += f"values ('desenvolvedor')"
    o_conexao.executar(insert)