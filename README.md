# pytest_freecodecamp
- [1.- Install Pytest y crear conjunto de carpetas](#schema1)
- [2.- Primera prueba](#schema2)
- [3.- Class-based Test](#schema3)



<a name="schema1"></a>

# 1. Install Pytest y crear conjunto de carpetas
``` 
pip install pytest 
``` 
- Crear carpeta source, donde van a ir el archivo con las fuciones a testear
  - Creamos un archivo my_functiones, donde añadimos dos funciones de prueba
  
    ```
    def add(number_one, number_two):
    return number_one + number_two

    def divide(number_one, number_two):
    return number_one/number_two
    ``` 
- Crear carpeta test, donde ve a ir el archivo para testear.
  - Dentro de esta carpeta creamos el archivo test_my_functions.py
  ```
  import pytest
  import source.my_functions as my_functions

  def test_add():
    pass
  ```
  - Y lo ejecutamos: 
    ```
    pytest test/test_my_functions.py
    ``` 
    Y comprobamos la salida, en este caso es una prueba y pasa correctamente.


<a name="schema2"></a>

# 2. Primera prueba.

Cambiamos el archivo `test_my_functions.py
```
  def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5

```
Haciendo esto vemos que la función suma funciona correctamente.
Si cambiamos el valor que afirmamos que debaría de dar a 6, quedando así la función:
```
  def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 6

```
En este caso si que da un error
![error](./img/test1.png)

En caso de la division tenemos que tener en cuenta la division por 0, que aunque nosotros forcemos a que pase el codigo 
nos da error.
```
  def test_divide_by_zero():
    result = my_functions.divide(number_one=10, number_two=0)
    assert True
```

![error](./img/test2.png)

Pero si esperamos un division por zero
```
 def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one=10, number_two=0)
```
Y ahora si que pasan los 3 test correctament
![error](./img/test3.png)

<a name="schema3"></a>

# 3. Class-based Test
- 1 Creamos el archivo `shapes.py` en la carpeta source. Con una clase shape y creamos una clase círculo
```
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2

        def perimeter(self):
            return 2*math.pi *self.radius
```
- 2 Creamos el archivo de test `test_circle.py`, es bueno que el archivo de test tenga un nombre con el que podamos
saber a que archivo le va hacer test.
```
import pytest
import source.shapes as shapes

class TestCircle:
    def test_one(self):
        assert True
```
![test](./img/test4.png)

- 3 Creamos dos funciones nuevas, `setup_method` y `teardown_method`.
  - La primera se ejecuta antes de que comience la prueba y se usa para realizar configuraciones o preparaciones antes 
de una prueba
  - La segunda se ejecuta una después que se ejecute la prueba y se utiliza por lo general para realizar limpieza o 
liberar recursos después de que las pruebas se hayan ejecutado.
  ```
    import source.shapes as shapes
    import math


  class TestCircle:

    def setup_method(self,method):
        print(f'Setting up {method}')
        self.circle = shapes.Circle(10)

    def teardown_method(self,method):
        print(f'Tearing down {method}')
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
  ```
- 4 Para ver la ejecución de estas dos útlimas funciones usamos 
  ```
    pytest test/test_circle.py -s
  ```
  ![error](./img/test5.png)

