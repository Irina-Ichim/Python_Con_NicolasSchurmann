### ¿Qué es el decorador `property`?

En Python, `property` es un **decorador** que permite convertir métodos de una clase en **propiedades**. Proporciona una forma elegante de implementar los métodos getter y setter, permitiendo el acceso y la modificación de atributos de una clase de manera similar a la de acceder y modificar atributos directamente.

### ¿Cómo se usa?

1. **Getter (Método de Obtención):**
   - Utiliza el decorador `@property` justo encima del método que actuará como getter.
   - Este método se ejecuta cuando intentas acceder al atributo asociado.

2. **Setter (Método de Establecimiento):**
   - Utiliza el decorador `@<nombre_del_getter>.setter` justo encima del método que actuará como setter.
   - Este método se ejecuta cuando intentas asignar un valor al atributo asociado.

### ¿Cuándo y por qué usarlo?

Usa el decorador `property` cuando desees:
- **Encapsular la lógica** de obtención y establecimiento de un atributo.
- Realizar acciones específicas cuando se **accede o modifica** un atributo.
- Proporcionar un **acceso controlado** a los atributos.

### Ejemplo Práctico:

```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio  # Atributo privado

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor > 0:
            self._radio = valor
        else:
            print("Error: El radio debe ser mayor que 0.")

# Uso de la clase
mi_circulo = Circulo(5)
print(mi_circulo.radio)  # Accede al método getter

mi_circulo.radio = 7  # Utiliza el método setter
print(mi_circulo.radio)
```

En este ejemplo, `radio` se ha convertido en una propiedad. El método `@property` permite acceder al radio, y el método `@radio.setter` permite modificarlo. La lógica dentro del setter controla que el radio sea mayor que 0.

Recuerda usar el decorador `property` cuando quieras proporcionar una interfaz más controlada y lógica al acceder y modificar atributos de una clase.