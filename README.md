# SQL_command_recognizer
Implementação de um Parser Descendente Recursivo que reconhece os principais comandos SQL.
<hr>
<h1>Comandos SQL reconhecidos</h1>
<h4>CREATE DATABASE 'id';</h4>
<h4>USE 'id';</h4>
<h4>CREATE TABLE 'id' ('id' 'tipo' [, 'id' 'tipo']*);</h4>
<h4>INSERT INTO 'id' ('id' [, 'id']*) VALUES ('valor' [, 'valor']*) [, ('valor' [, 'valor']*)]*;</h4>
<h4>SELECT * FROM 'id';</h4>
<h4>SELECT 'id' [, 'id']* FROM 'id';</h4>
<h4>SELECT * FROM 'id' ORDER BY 'id';</h4>
<h4>SELECT * FROM 'id' WHERE 'id' = 'valor';</h4>
<h4>UPDATE 'id' SET 'id' = 'valor' WHERE 'id' = 'valor';</h4>
<h4>DELETE FROM 'id' WHERE 'id' = 'valor';</h4>
<h4>TRUNCATE TABLE 'id;</h4>
<hr>
<h5>OBS: Exemplos de entradas presentes no arquivo "exemplos.txt"</h5>
