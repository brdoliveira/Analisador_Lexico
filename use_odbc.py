import pyodbc
from credentials import *

def insert_word_table_odbc(word: str, type: str) -> None:
    """
    Função responsável por adicionar palavra para o wordcloud.

    Args:
        word (str): Palavra que será a adicionada no banco de dados.
        type (str): Tipo da palavra, exemplo: Variável, Separador, etc...

    Returns:
        none

    Errors:
        pyodbc.ProgrammingError: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conn_string)
    try:
        cursor = conn.cursor()
        sql_query = "INSERT INTO WordClients (Word,TypeWord,CaptureDate) VALUES ('{0}','{1}',getdate())".format(word, type)

        cursor.execute(sql_query)
        cursor.commit()
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()

def insert_phrase_table_odbc(phrase: str, type: str) -> None:
    """
    Função responsável por adicionar frase para a análise de dados.

    Args:
        phrase (str): Frase que será inserida no banco.
        type (str): Tipo da frase, exemplo: Positivo ou Negativo.

    Returns:
        none

    Errors:
        pyodbc.ProgrammingError: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conn_string)
    try:
        cursor = conn.cursor()
        sql_query = "INSERT INTO Feedbacks(Phrase,TypeFeedback,CaptureDate) values('{0}','{1}',getdate())".format(phrase,type)

        cursor.execute(sql_query)
        cursor.commit()
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()

def get_words_table_odbc(parameters : str = '*') -> list:
    """
    Função responsável por buscar os valores da tabela de palavras

    Args:
        parameters (str): Paramamtros escolhidos para ser buscado.

    Returns:
        Responsável por retornar uma lista com os registros da WordClients

    Errors:
        pyodbc.ProgrammingError: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conn_string)
    try:
        cursor = conn.cursor()
        sql_query = f'SELECT {parameters} FROM WordClients'

        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.commit()

        return result
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()

def get_phrase_table_odbc(parameters : str = '*') -> list:
    """
    Função responsável por buscar os valores da tabela de feedback

    Args:
        parameters (str): Parametros escolhidos para ser buscado.

    Returns:
        Lista com os parametros selecionados

    Errors:
        pyodbc.ProgrammingError: Erro com a conexão com o banco de dados
    """
    conn = pyodbc.connect(conn_string)
    try:
        cursor = conn.cursor()
        sql_query = f'SELECT {parameters} FROM Feedbacks' 

        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.commit()

        return result
    except pyodbc.ProgrammingError as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        cursor.close()

