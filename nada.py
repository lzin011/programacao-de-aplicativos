import sqlite3
Importa a biblioteca sqlite3, usada para trabalhar com bancos de dados SQLite.
Tratamento de erros
try:
Inicia um bloco de código que será monitorado. Se ocorrer algum erro, o programa irá para o except.
Conectando ao banco
conexao = sqlite3.connect("cinema.db")
Cria o banco cinema.db se ele não existir.
Se já existir, apenas abre o banco.
cursor = conexao.cursor()
Cria um cursor, que é o objeto responsável por executar comandos SQL.
Ativando chave estrangeira
cursor.execute("PRAGMA foreign_keys = ON")
Faz com que o SQLite respeite as Foreign Keys (FK).
Criando a tabela de cinemas
cursor.execute("""
CREATE TABLE IF NOT EXISTS cinemas(
Cria a tabela cinemas caso ela ainda não exista.
id INTEGER PRIMARY KEY AUTOINCREMENT,
id é o identificador do cinema.
PRIMARY KEY significa chave primária.
AUTOINCREMENT faz o ID aumentar automaticamente.
nome_cinema TEXT,
Campo para armazenar o nome do cinema.
shopping TEXT
Campo para armazenar o nome do shopping.
)
""")
Finaliza a criação da tabela.
Criando a tabela de salas
cursor.execute("""
CREATE TABLE IF NOT EXISTS salas(
Cria a tabela salas.
id INTEGER PRIMARY KEY AUTOINCREMENT,
ID da sala.
numero_sala INTEGER,
Número da sala.
capacidade INTEGER,
Quantidade de pessoas que cabem na sala.
id_cinema INTEGER,
Guarda o ID do cinema ao qual a sala pertence.
FOREIGN KEY(id_cinema) REFERENCES cinemas(id)
Diz que id_cinema deve existir na tabela cinemas.
)
""")
Finaliza a criação da tabela.
Salvando as tabelas
conexao.commit()
Salva as alterações feitas no banco.
Cadastro do cinema
nome = input("Nome do cinema: ")
Pede o nome do cinema.
shopping = input("Shopping: ")
Pede o shopping onde o cinema está.
cursor.execute(
    "INSERT INTO cinemas(nome_cinema, shopping) VALUES (?, ?)",
    (nome, shopping)
)
Insere o cinema no banco.
Os ? recebem os valores das variáveis nome e shopping.
conexao.commit()
Salva o cadastro do cinema.
Cadastro da sala
try:
Inicia outro tratamento de erro.
Aqui ele serve para capturar erros caso o usuário digite texto em vez de números.
numero = int(input("Número da sala: "))
Pede o número da sala.
int() transforma a entrada em número inteiro.
capacidade = int(input("Capacidade: "))
Pede a capacidade da sala.
id_cinema = int(input("ID do cinema: "))
Pede o ID do cinema ao qual a sala pertence.
cursor.execute("SELECT * FROM cinemas WHERE id = ?", (id_cinema,))
Procura um cinema com o ID informado.
if cursor.fetchone():
fetchone() pega a primeira linha encontrada.
Se encontrou um cinema, retorna um valor verdadeiro (True).
Se não encontrou, retorna None.
cursor.execute("""
INSERT INTO salas(numero_sala, capacidade, id_cinema)
VALUES (?, ?, ?)
""", (numero, capacidade, id_cinema))
Cadastra a sala no banco.
conexao.commit()
Salva a nova sala.
print("Sala cadastrada!")
Exibe uma mensagem de sucesso.
else:
    print("Cinema não encontrado.")
Se o ID informado não existir, a sala não é cadastrada.
except ValueError:
Captura o erro quando o usuário digita texto em um campo que deveria ser numérico.

Exemplo:

Número da sala: A

Isso gera um ValueError.

print("Digite apenas números nos campos numéricos.")
Exibe uma mensagem informando o erro.
Listando as salas
print("\nSalas cadastradas:")
Mostra um título antes da listagem.
cursor.execute("SELECT * FROM salas")
Busca todas as salas cadastradas.
salas = cursor.fetchall()
fetchall() pega todos os registros encontrados e guarda na variável salas.
for sala in salas:
Percorre cada sala encontrada.
print(sala)
Exibe uma sala por vez.

Exemplo de saída:

(1, 5, 120, 1)
(2, 6, 90, 1)
Tratando erros do banco
except sqlite3.Error as erro:
Captura qualquer erro relacionado ao SQLite.
print("Erro:", erro)
Mostra a mensagem do erro.
Encerrando a conexão
finally:
Esse bloco sempre será executado, com erro ou sem erro.
conexao.close()
Fecha a conexão com o banco de dados.