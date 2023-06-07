from better_profanity import profanity
from googletrans import Translator

# Constantes
TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."
PONTO_E_VIRGULA = ";"

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáãàâçéèêóòôõíìîóòõôúùû"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')
SEPARADOR = 5
NAO_ENCONTRADO = 6

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"

# palavras negativas
PALAVRAS_NEGATIVAS = False
PALAVRAS_POSITIVAS = True


#------------------------------------------------------------
def tokenize(exp : str) -> list:
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    result = []
    var_sep = []
    complete_number = []
    # exp = ''.join(exp.split(" "))
    for index, i in enumerate(exp):
        if i in COMENTARIO:
            break
        if i in LETRAS:
            var_sep.append(i)
            if index+1 == len(exp):
                var_com = ''.join(var_sep)
                result.append([var_com, VARIAVEL])
                var_sep = []
                continue
            if exp[index+1] in DIGITOS:
                var_sep.append(exp[index+1])
            if exp[index+1] not in LETRAS:
                var_com = ''.join(var_sep)
                result.append([var_com, VARIAVEL])
                var_sep = []
        elif i in OPERADORES:
            result.append([i, OPERADOR])
        elif i in ABRE_FECHA_PARENTESES:
            result.append([i, PARENTESES])
        elif i in PONTO_E_VIRGULA:
            result.append([i, SEPARADOR])
        elif i in BRANCOS:
            result.append([i,SEPARADOR])
        elif i in DIGITOS:
            if exp[index-1] not in LETRAS:
                if index == len(exp) - 1:
                    complete_number.append(i)
                    result.append([float("".join(complete_number)), NUMERO])
                    complete_number = []
                elif exp[index+1] in DIGITOS:
                    complete_number.append(i)
                else:
                    complete_number.append(i)
                    result.append([float("".join(complete_number)), NUMERO])
                    complete_number = []
        else:
            result.append([i, NAO_ENCONTRADO])
    return result
    
def tokenize_phrase(phrase):
    """
    (str) -> list

    Recebe uma string frase, e a função irá validar se a frase tem uma palavra profana

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    translator = Translator()

    if COMENTARIO in phrase:
        phrase = phrase.split(COMENTARIO, 1)[0]

    tokens = []
    text_en = translator.translate(phrase, src="pt", dest="en")
    print(text_en.text)
    if profanity.contains_profanity(text_en.text) == False:
        tokens.append([phrase, PALAVRAS_NEGATIVAS])
    else:
        tokens.append([phrase, PALAVRAS_POSITIVAS])

    return tokens