# keywords arguments 
# una manera de poder empaquetar todos los parametros en un solo parametro

def get_product(**datos):  # estamos diciendo que trabajamos con keywords
    print(datos["id"], datos["name"])
    
get_product(id="40",
            name = "Samsung",
            description = "Mi marca favorita de moviles")    # el resultado es un diccionario y es necesario colocar el nombre del parametro a cual queremos que acceda

