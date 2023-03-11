import ply.lex as lex 
import ply.yacc as yacc


# Tokens
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVICION',
    'ID',
    'CONDICIONAL',
    'SI_NO',
    'ENTONCES',
    'DE',
    'ROMPER',
    'GLOBALES',
    'AFIRMAR',
    'IMPORTAR',
    'CLASE',
    'FALSO',
    'Y',
    'FINALIZAR',
    'CICLO_MIENTRAS',
    'CICLO_PARA',
    'CONTINUE',
)

# Palabras reservadas
reserved = {
    'if': 'CONDICIONAL',
    'else': 'SI_NO',
    'then': 'ENTONCES',
    'from': 'DE',
    'break': 'ROMPER',
    'global': 'GLOBALES',
    'assert': 'AFIRMAR',
    'import': 'IMPORTAR',
    'class': 'CLASE',
    'false': 'FALSO',
    'and': 'Y',
    'finally': 'FINALIZAR',
    'while': 'CICLO_MIENTRAS',
    'for': 'CICLO_PARA',
    'continue': 'CONTINUE',
}

# Expresiones regulares de conocimiento
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVICION = r'/'
t_ignore = ' \t' '\n'

# Reglas de expresiones regulares que retornan tokens
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# Manejo de errores
def t_error(t):
    print("Token desconocido: '%s'" % t.value[0] )
    t.lexer.skip(1)

# Analizador léxico
lexer = lex.lex()

# Definición de reglas de gramática
def p_expresion_SUMA(p):
    'expresion : expresion SUMA termino'                     
    p[0] = p[1] + p[3]
    
def p_expresion_RESTA(p):
    'expresion : expresion RESTA termino'
    p[0] = p[1] - p[3]
    
def p_expresion_TERMINO(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]
     
def p_termino_Numero(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_error(p):
    print('Error de sintaxis!')

# Analizador sintáctico
parser = yacc.yacc()

# Lectura de archivo
with open('data.txt', 'r') as archivo:
    data = archivo.read()
    resultado = parser.parse(data)
    print(resultado)
