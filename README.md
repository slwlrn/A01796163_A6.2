Aquí tienes la documentación del proyecto en español siguiendo la estructura que mencionaste:

---

# 📌 Sistema de Reservaciones con Trazabilidad

Este proyecto implementa un sistema de reservaciones en **Python** para administrar **hoteles, clientes y reservaciones**. Los datos se almacenan en archivos **JSON**, y se generan copias de seguridad **(.bak)** para garantizar trazabilidad y recuperación de datos en caso de errores.

---

## 📂 Estructura del Proyecto

```
📂 reservationsystem
 ├── 📂 test_cases  # Datos de prueba
 │   ├── test_hotels.json
 │   ├── test_customers.json
 │   ├── test_reservations.json
 ├── hotels.json  # Almacenamiento de hoteles
 ├── customers.json  # Almacenamiento de clientes
 ├── reservations.json  # Almacenamiento de reservaciones
 ├── main.py  # Código principal del sistema
 ├── README.md  # Documentación del proyecto
```

---

## 🔹 Requisitos Previos

Para ejecutar este proyecto, necesitas:

- **Python 3.8 o superior**
- Instalar herramientas de análisis de código:

```sh
pip install flake8 pylint coverage
```

---

## 🚀 Cómo Ejecutar el Programa

### 📍 Ejecución del Sistema de Reservaciones

Ejecuta el programa con:

```sh
python main.py
```

Este script administra **hoteles, clientes y reservaciones**, asegurando que los datos sean persistentes y trazables.

---

## 📊 Ejecución de Pruebas Unitarias

Para verificar el correcto funcionamiento del sistema, ejecuta:

```sh
python -m unittest main.py
```

La salida esperada confirmará que **las 5 pruebas se ejecutan correctamente**:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.134s

OK
```

---

## 📤 Generar Reporte de Cobertura

Para comprobar que el código tiene una cobertura superior al **85%**, ejecuta:

```sh
coverage run -m unittest main.py
coverage report -m
```

Salida esperada:

```
Name         Stmts   Miss  Cover
--------------------------------
main.py      XXX     XX    90% 
```

---

## ✅ Validación de Estilo con `flake8` y `pylint`

Para asegurar que el código sigue los estándares **PEP 8**, ejecuta:

```sh
flake8 main.py --max-line-length=79
pylint main.py
```

Un puntaje **10/10 en pylint** indica que el código está correctamente estructurado.

---

## 📌 Características del Sistema

✅ **Gestión de Hoteles** - Agregar, listar y eliminar hoteles.

✅ **Gestión de Clientes** - Registrar, listar y eliminar clientes.

✅ **Gestión de Reservaciones** - Crear, listar y cancelar reservaciones.

✅ **Copia de Seguridad (.bak)** - Se generan archivos de respaldo con timestamps.

✅ **Pruebas Unitarias** - 5 pruebas automatizadas validan el sistema.

✅ **Trazabilidad Completa** - Se mantiene un historial de reservaciones.

---

## ⚠ Notas Importantes

- Los archivos `.bak` permiten recuperar versiones previas en caso de fallos.
- Las pruebas **NO eliminan los datos JSON**, permitiendo trazabilidad de datos.
- Las reservaciones **persisten** entre ejecuciones, a menos que sean canceladas.

---
