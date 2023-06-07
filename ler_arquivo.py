import use_odbc
import tokeniza as tk


def read_file_txt(path) -> list:
    '''
    Função responsável por ler arquivo e validar as frases inseridas
    
     Args:
        path(str): caminho do arquivo

    Returns:
        Lista com palavras
    '''
    words = []
    with open(str(path), "r", encoding="utf-8", newline="\n") as fp:
        line = fp.readline()
        while line:
            list_tokens = tk.tokenize(line.lower())
            for token in list_tokens:
                item, typeWord = token
                typeVar = "INDEFINIDO"

                if typeWord in [tk.OPERADOR, tk.PARENTESES]:
                    continue
                elif typeWord == tk.VARIAVEL:
                    if(len(item) >= 4):
                        words.append(item)
                    description = "%s" %item
                    typeVar = "VARIAVEL"
                elif typeWord == tk.NUMERO:
                    description = "%f" %item
                    typeVar = "FLOAT"
                elif typeWord == tk.SEPARADOR:
                    description = "%s" %item
                    typeVar = "SEPARADOR"
                else:
                    description = "%s" %item
                    typeVar = "DESCONHECIDA"

                if((typeWord != "DESCONHECIDA" and typeWord != 'SEPARADOR') and (len(description) >= 4)):
                    use_odbc.insert_word_table_odbc(str(description),typeVar)

            phrase = tk.tokenize_phrase(line.lower())
            formated_phrase = phrase[0]
            use_odbc.insert_phrase_table_odbc(str(formated_phrase[0]),formated_phrase[1])
            line = fp.readline()
    return words

#-------------------------------------------
# início da execução do programa manualmente
read_file_txt("data/tweets-tt.txt")
