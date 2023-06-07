import use_odbc
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def list_word_cloud() -> list:
    """
    Função responsável por retornar a lista de palavras da tabela de palavras

    Args:
        None

    Returns:
        Lista com palavras

    Errors:
        pyodbc.ProgrammingError: Erro com a conexão com o banco de dados
    """
    return [i[0] for i in use_odbc.get_words_table_odbc("Word")]


def remove_conectors(list_string : list) ->  list:
    """
    Função responsável remover conectores e palavras enviesadas

    Args:
        Lista de palavras
        
    Returns:
        Lista com palavras sem os conectores e dados enviesados
    """
        
    # Palavras que são utilizadas como conectoresw nas frases 
    # list_conectores = ['de','o','da','ter','um','em','que','é','por','ser','vai','e','a','u','i','para','tem','até','lá','os']
    list_conectors = ['pode','mais','isso','pela','para','estão','quem','quer','pelo','onde','muito','essa']

    # Utilizei no web-scrapping #rodovia, #carros e #estradas então retirei esses valores para o word cloud ser mais preciso 
    list_conectors.append('carro')
    list_conectors.append('rodovia')
    list_conectors.append('rodovias')
    list_conectors.append('estrada')
    list_conectors.append('estradas')

    for word in list_conectors:
        for i in list_string:
            if word == i:
                list_string.remove(word)
    return list_string

def generate_word_cloud() -> None:
    """
    Função responsável por gerar o WordCloud

    Args:
        None
        
    Returns:
        None

    """
    list_word = list_word_cloud()            
    list_word = remove_conectors(list_word)

    unique_string=(" ").join(word for word in list_word)
    word_cloud = WordCloud(collocations = False, background_color = 'white').generate(unique_string)
    plt.figure(figsize=(15,8))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    plt.close()

generate_word_cloud()