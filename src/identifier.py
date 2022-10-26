import re


# O método isidentifier é usado para verificar se uma string é um identificador ou não
# letras maiúsculas, minúsculas e dígitos, desde que não seja o primeiro caractere. 
def identifier(id):
    if id.isidentifier() and len(id) >= 1 and len(id) <= 6:
        return "Valido"
    else:
        return "Invalido"