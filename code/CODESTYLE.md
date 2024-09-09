## Commit Standard

### Formato del Mensaje de Commit

Un buen mensaje de commit debe seguir el siguiente formato:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)])
```

### Tipos de Commit

- **feat**: Una nueva característica.
- **fix**: Una corrección de errores.
- **docs**: Cambios en la documentación.
- **style**: Cambios que no afectan el significado del código (espacios en blanco, formato, etc.).
- **refactor**: Cambios en el código que no corrigen errores ni añaden características.
- **test**: Añadir o corregir tests.
- **chore**: Cambios en el proceso de construcción o herramientas auxiliares y librerías.

## Coding Style

### Nombres de Variables y Funciones

- Usa nombres descriptivos y significativos.
- Usa camelCase para variables y funciones.
- Usa PascalCase para nombres de clases.

### Formato del Código

- Indentación de 4 espacios.
- Líneas de máximo 80 caracteres.

### Comentarios

- Usa comentarios para explicar el "por qué" detrás de una decisión de código.
- Evita comentarios obvios que no añaden valor.

### Ejemplo de Código

```python
class MiClaseEjemplo:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial

    def incrementar_valor(self, incremento):
        """
        Incrementa el valor por la cantidad especificada.

        :param incremento: La cantidad a incrementar.
        """
        self.valor += incremento
```
