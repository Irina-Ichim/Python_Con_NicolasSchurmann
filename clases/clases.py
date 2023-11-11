class MiPerro:      # la primera letra debe ser mayuscula
    def  habla(self):    # ojo con la identacion, estas funciones en una clase dejan de ser funciones, son metodos. Siempre el primer parametro de una class es self
         print("Guau!") 
       
mi_perro = MiPerro()    # mi_perro es una instancia(=objeto)
# print(type(mi_perro))
mi_perro.habla()        # invocamos el metodo
print(isinstance(mi_perro, MiPerro))   #isistence se usa para verificar si es una instancia, puede devolver true o false
print(isinstance(mi_perro, str))

#"self" es simplemente una convención para referirse al objeto actual y permite que los métodos dentro de la clase interactúen con los datos de esa instancia específica.
        