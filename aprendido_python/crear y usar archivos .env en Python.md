Cómo crear y usar archivos .env en Python
Última actualización: 23 de julio de 2025

En Python, un archivo .env se usa comúnmente para almacenar ajustes de
configuración, claves de API y otra información confidencial. Es un archivo de texto
plano con pares clave-valor, y la biblioteca python-dotenv se usa a menudo para
cargar estas variables en el entorno. En este artículo, exploraremos el proceso
detallado de creación y uso de archivos .env en Python.

¿Qué son los archivos .Env en Python?
Un archivo .env en Python es un archivo de texto simple que se utiliza para
almacenar ajustes de configuración, variables de entorno y otros pares clave-valor
relacionados con un proyecto Python. Estos archivos suelen contener información
confidencial, como claves de API, credenciales de base de datos o ajustes de
configuración. El contenido de un archivo .env no está diseñado para codificarse en
el código fuente, sino que se carga en el entorno del proyecto durante la ejecución.
La biblioteca python-dotenv se utiliza habitualmente para leer el contenido del
archivo .env y configurar las variables de entorno, lo que la convierte en una forma
práctica de gestionar las configuraciones del proyecto de forma segura.

¿Cómo crear y utilizar archivos .Env en Python?
A continuación se muestra el procedimiento completo 
para crear y utilizar archivos .Env en Python:
Paso 1: Crea el archivo .env
En el directorio de su proyecto, cree un archivo llamado ".env" en el nivel raíz
para almacenar configuraciones e información confidencial.

Paso 2: Instalar el módulo
Instale la biblioteca python-dotenv ejecutando el siguiente comando en su terminal
o terminal integrada dentro de su IDE de Python (por ejemplo, PyCharm ):
pip instalar python-dotenv

Paso 3: Almacenar datos confidenciales en un archivo .env
En el archivo .env, defina los pares clave-valor para la configuración. Por ejemplo:
MI_CLAVE = "kishankaushik12353"
Este archivo almacenará información confidencial y configuraciones.Paso 4: Acceda al archivo .env
En su código Python, importe el módulo dotenv y use load_dotenv() para cargar
variables desde el archivo .env. Acceda a los valores
usando os.getenv("KEY") para cada par clave-valor definido en el archivo .env .
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()
# accessing and printing value
print(os.getenv("MY_KEY"))Paso 5: Compilar y ejecutar el código
Compila y ejecuta el código Python. El programa utilizará las variables de entorno
cargadas desde el archivo .env y la salida mostrará el valor asociado a la clave
especificada, como " MY_KEY ", lo que demuestra una integración correcta con el
archivo .env.Conclusión
En conclusión, el uso de archivos .env en Python proporciona una forma segura y
organizada de gestionar información confidencial y opciones de configuración.
Mediante la biblioteca python-dotenv, los desarrolladores pueden cargar variables
fácilmente en el entorno del proyecto, lo que mejora la flexibilidad en diferentes
entornos. Esta práctica garantiza la separación de los datos confidenciales del
código base y permite un enfoque sistemático para gestionar las configuraciones
en desarrollo, pruebas y producción. Incorporar archivos .env es una buena
práctica para mantener la seguridad y la escalabilidad en proyectos Python.
