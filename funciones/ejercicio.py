# Palindromo
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto  
      
def reverse(texto):
    texto_al_revers = ""
    for char in texto:
        texto_al_revers = char + texto_al_revers
    return(texto_al_revers)    

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_revers = reverse(texto)
    return texto.lower() == texto_al_revers.lower()
    
print(es_palindromo("amo la paloma"))  
print(es_palindromo("hola mundo"))
print(es_palindromo("reconocer"))
print(es_palindromo("Somos o no somos"))  