Administrar multiples versiones de Python con pyenv

Tabla de contenido
Comprender los beneficios de usar pyenv
Instalación de pyenv
Preparación de sistemas Linux para pyenv
Preparación de sistemas macOS para pyenv
Instalación de pyenv en sistemas tipo Unix
Instalación de pyenv-win en Windows
Administrar múltiples versiones de Python con pyenv
Instalación de versiones de Python: instalar
Comprobación de las versiones instaladas: versiones
Comprobación de la ruta ejecutable actual de Python: cuál
Desinstalar versiones de Python: desinstalar
Configuración de la versión de Python a utilizar
Versión de Python de la sesión de Shell actual: shell
La versión local o específica de la aplicación de Python: local
La versión global de Python: global
Gestión de entornos virtuales con pyenv
Creación de entornos virtuales
Listado de entornos virtuales
Uso de entornos virtuales
Eliminación de entornos virtuales
Conclusión
Preguntas frecuentes
----------------------------------------

Comprender los beneficios del usopyenv
La pyenvherramienta está diseñada para gestionar múltiples versiones de Python de forma ordenada. Incluso si ya tiene
Python instalado en su sistema operativo, conviene tenerlo pyenvinstalado para mantener la instalación de Python del
sistema ordenada y, lo que es más importante, contribuir a proyectos que usan una versión diferente de Python.
Surge la pregunta: ¿Por qué debería usarlo pyenvsi ya tengo Python instalado en mi sistema operativo (OS)?La instalación del sistema de Python es el intérprete de Python que se instala directamente en el sistema operativo.
Normalmente, en macOS o Linux, se instala Python por defecto. En Windows, es posible que deba instalar
Python manualmente.
Entonces, ¿por qué no usar la instalación de Python del sistema para tu programación diaria? Una forma de verlo es que
este Python pertenece al sistema operativo. En muchos casos, el sistema operativo depende del Python preinstalado para
funcionar. Esto significa que algunos componentes del sistema operativo pueden depender de una versión específica de
Python para funcionar correctamente. Si cambias la versión de Python del sistema o algunos de los paquetes preinstalados,
podrías dañar el propio sistema operativo.
Además, es posible que no tengas mucho control sobre la versión de Python que puedes instalar en tu sistema operativo. Si
quieres usar las últimas funciones de Python y usas Ubuntu, por ejemplo, podrías tener problemas. Las versiones disponibles
podrían ser demasiado antiguas, lo que significa que tendrás que esperar a que salga una nueva versión del sistema
operativo. Desafortunadamente, puede aparecer otra versión de Python en ese proceso y nunca estarás al día.
Otro problema surge al instalar paquetes de terceros en el sistema Python mediante el pipcomando o una herramienta
similar. En este caso, se instala el paquete de Python globalmente, lo que puede ser un problema si otro usuario (o usted
mismo) desea instalar una versión diferente del paquete para trabajar en otro proyecto. No se pueden tener varias versiones
del mismo paquete instaladas en un entorno de Python determinado.
Por ejemplo, si tiene la versión 1.1.0 de un paquete determinado e instala la versión 1.2.0, reemplazará la primera. Esto
podría parecer inofensivo. Sin embargo, los proyectos que dependen de la versión anterior pueden dejar de funcionar con la
nueva.
Un problema crítico surge cuando tienes varios proyectos que requieren diferentes versiones de Python. La instalación de
Python del sistema suele ser única. Si actualizas Python, algunos proyectos podrían dejar de funcionar. Si no lo actualizas,
es posible que los proyectos más recientes no puedan usar las nuevas funciones de Python.
Finalmente, en la mayoría de los sistemas operativos, se necesitan privilegios administrativos para instalar una versión
diferente de Python o paquetes de terceros. Este requisito puede ser un verdadero obstáculo en entornos empresariales con
estrictas normas de seguridad. En resumen, usar la instalación de Python del sistema conlleva importantes inconvenientes.
Puede:
Romper partes del sistema operativo
Evitar que utilices las últimas versiones de Python
Provocar problemas en proyectos que requieren versiones anteriores de Python
Proyectos de bloques que dependen de nuevas características de Python
Requerir la intervención de una tercera persona cuando se necesita instalar algo
Idealmente, busca mayor flexibilidad y seguridad al usar Python para el desarrollo de software. Por ejemplo, podría necesitar
realizar algunas de las siguientes acciones:
Instale Python en su espacio de usuario para no depender de los administradores del sistema
Instalar, administrar y desinstalar múltiples versiones de Python libremente
Especifique la versión exacta de Python que desea utilizar en cada proyecto
Cambiar entre las versiones instaladas
La buena noticia es que pyenvte permite hacer todo esto. Además, es una excelente manera de instalar versiones
preliminares de Python , para que puedas probar nuevas funciones del lenguaje o comprobar si la versión tiene errores.
Eliminar anuncios
Instalaciónpyenv
Antes de instalar y usar pyenven Linux o macOS, es posible que deba cumplir con algunas dependencias específicas del
sistema operativo. Estas dependencias son principalmente utilidades de desarrollo escritas en C que pyenvcompilan Python
desde el código fuente. Por otro lado, los usuarios de Windows configuran las cosas de forma diferente, como prontodescubrirá.
Para obtener una explicación más detallada de las dependencias de compilación, consulta la Guía del desarrollador de
Python . En este tutorial, aprenderás las formas más comunes de instalar estas dependencias.
Preparación de sistemas Linux parapyenv
En sistemas Linux, las dependencias de compilación varían según la plataforma. Si usa Ubuntu o Debian y desea instalar
las dependencias de compilación, puede ejecutar los siguientes comandos:
$ sudo apt update
$ sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev \
xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
Estos comandos usan Apt para actualizar el índice del repositorio del sistema e instalar todas las dependencias de
compilación. Una vez ejecutados, estará listo para empezar.
Si usa Fedora Linux , puede usar el siguiente comando para instalar sus dependencias de compilación:
$ sudo dnf install make gcc patch zlib-devel bzip2 bzip2-devel \
readline-devel sqlite sqlite-devel openssl-devel tk-devel \
libffi-devel xz-devel libuuid-devel gdbm-libs libnsl2
Si utiliza openSUSE , ejecute lo siguiente:
$ zypper install gcc automake bzip2 libbz2-devel xz xz-devel \
openssl-devel ncurses-devel readline-devel zlib-devel tk-devel \
libffi-devel sqlite3-devel gdbm-devel make findutils patch
Nuevamente, este comando instala todas las dependencias de compilación de Python para su sistema. Si usa otra
distribución de Linux, consulte la pyenv guía del entorno de compilación para encontrar los comandos necesarios para su
sistema operativo.
Preparación de los sistemas macOS parapyenv
Si eres usuario de macOS, puedes usar el siguiente comando para instalar las dependencias de compilación:
$ brew install openssl readline sqlite3 xz zlib tcl-tk@8 libb2 zstd
Si no tiene Homebrew instalado en su sistema, puede visitar su página de inicio para obtener instrucciones de instalación.
Instalación pyenven sistemas tipo Unix
Después de instalar las dependencias de compilación, estará listo para la instalación pyenv. La documentación recomienda
usar el instalador automático . El siguiente comando debería funcionar en Linux y macOS, aunque en macOS podría ser
necesario reemplazarlo bashpor zsh:
$ curl -fsSL https://pyenv.run | bash
Esto se instalará pyenven tu sistema. Sin embargo, la instalación aún no está lista para usar. Necesitas configurar tu
entorno de shell para pyenv.
Nota: Puedes ampliar la funcionalidad principal pyenvinstalando complementos . Algunos de los complementos oficiales
son los siguientes:
pyenv-virtualenv:Plugin para gestionar entornos virtuales conpyenv
pyenv-update:Plugin para actualizaciónpyenv
pyenv-doctor:Complemento para verificar que pyenvlas dependencias de compilación estén instaladas
Si Bash es su shell de sistema predeterminado, puede ejecutar los siguientes comandos:$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
Si tiene archivos ~/.profile, ~/.bash_profile, o ~/.bash_login, ejecute estos comandos también en esos archivos. Si no
tiene ninguno de estos archivos, cree un archivo ~/.profiley ejecute los comandos en él.
Si usas macOS, zsh sería tu shell predeterminado. En este caso, puedes ejecutar los comandos anteriores en los
archivos ~/.zshrcy ~/.zprofile.
Una vez que hayas hecho esto, puedes recargar tu shell con el siguiente comando:
$ exec "$SHELL"
Alternativamente, puedes reiniciar tu terminal. ¡Listo! Ya lo tienes pyenvinstalado y listo para usar.
Eliminar anuncios
Instalación pyenv-winen Windows
La pyenvherramienta en sí no es compatible con Windows . Sin embargo, si lo está, puede usar pyenv-win , que es
una pyenvadaptación para Windows. La forma recomendada de instalar esta herramienta en Windows es ejecutar el siguiente
comando en una terminal de PowerShell :
PS> Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyen
Si recibe un UnauthorizedAccesserror, inicie PowerShell con la opción "Ejecutar como administrador" y ejecute Set-
ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine. Una vez completado este comando, ejecute el
comando de instalación anterior.
Administrar múltiples versiones de Python conpyenv
La pyenvherramienta ofrece varios comandos para instalar y administrar varias versiones de Python. Puede ver una lista
completa ejecutando el siguiente comando:
$ pyenv commands
--version
activate
commands
...
which
Esta salida muestra todos los nombres de comandos disponibles en su pyenvinstalación. Cada comando tiene una --
helpbandera que le proporcionará información más detallada. Por ejemplo, si desea ver más información sobre
el installcomando, puede ejecutar lo siguiente:$ pyenv install --help
Usage: pyenv install [-f] [-kvp] <version>...
pyenv install [-f] [-kvp] <definition-file>
pyenv install -l|--list
pyenv install --version
-l/--list
List all available versions
-f/--force
Install even if the version appears to be installed already
-s/--skip-existing Skip if the version appears to be installed already
...
El mensaje de ayuda describe para qué se usa el comando y las opciones que puede usar junto con él. En las siguientes
secciones, encontrará una descripción general de pyenvlos comandos que le permiten administrar varias versiones de
Python.
Instalación de versiones de Python:install
Ahora que lo has instalado y configurado pyenven tu sistema, el siguiente paso es instalar Python. Tienes varias versiones
para elegir. Si quieres verlas todas, ejecuta este comando:
$ pyenv install --list
Available versions:
2.1.3
2.2.3
2.3.7
2.4.0
...
Obtendrás una lista de casi 1000 versiones distintas de Python, y la cifra sigue aumentando. Incluye otras variantes de
Python, como ActivePython , IronPython y Jython , así como distribuciones como Anaconda .
Nota: Si has estado usando pyenvla herramienta durante un tiempo y no ves la versión que estás buscando, es posible
que tengas que ejecutarla pyenv updatepara actualizarla y asegurarte de tener acceso a las últimas versiones.
Para ver solo las versiones de CPython disponibles a partir de la 3.10, ejecute el siguiente comando:
$ pyenv install --list | grep -E ' 3\.([1-9][0-9]+)'
3.10.0
3.10-dev
3.10.1
...
3.13.5
3.13.5t
3.13.6
3.13.6t
3.13.7
3.13.7t
3.14.0rc2
3.14.0rc2t
3.14-dev
3.14t-dev
3.15-dev
3.15t-dev
Esta salida muestra todas las versiones de Python que coinciden con la expresión regular especificada . En este ejemplo, se
listan todas las versiones de CPython disponibles a partir de la 3.10.0.
También puedes consultar otras implementaciones de Python. Por ejemplo, si quieres ver todas las versiones de PyPy ,
puedes hacer lo siguiente:$ pyenv install --list | grep " pypy"
pypy-c-jit-latest
pypy-dev
pypy-stm-2.3
pypy-stm-2.5.1
pypy-1.5-src
pypy-1.6
...
Una vez que encuentres la versión que deseas, puedes instalarla con un solo comando:
$ pyenv install 3.13.5
Este comando tardará un poco porque pyenvnecesita compilar la versión de Python seleccionada desde el código fuente.
Una vez completada la compilación, la versión que elijas se instalará en tu equipo local.
También puedes enumerar varias versiones en un comando separándolas con espacios:
$ pyenv install 3.13.5 3.14.0rc2
Continúe e instale otra versión usted mismo. Tenga en cuenta que es posible que no pueda seguir los ejemplos del tutorial al
pie de la letra, ya que las versiones candidatas a lanzamiento (RC) , como la 3.14.0rc2, se publican temporalmente durante la
fase de pruebas. Una vez publicada la siguiente versión, el equipo de Python suele eliminar las RC anteriores del servidor de
descarga para evitar confusiones.
Nota: Si tiene algún problema con la compilación, puede consultar la pyenvdocumentación , que contiene excelentes
notas de instalación, preguntas frecuentes útiles y problemas de compilación comunes .
Durante el resto del tutorial, los ejemplos suponen que ha instalado 3.13.5 y 3.14.0rc2, pero puede sustituirlos por cualquier
otra versión de Python que esté utilizando.
Eliminar anuncios
Comprobando las versiones instaladas:versions
Como ya sabes, pyenvPython se compila desde el código fuente. Cada versión que instalas se encuentra en
la versions/carpeta de tu pyenvdirectorio raíz:
$ ls $PYENV_ROOT/versions/
3.13.5
3.14.0rc2
En este punto, solo tendrás las versiones 3.13.5y 3.14.0rc2, como puedes ver en este resultado. Ahora es el momento de
aprender a usar las versiones de Python instaladas.
En lugar de utilizar el lscomando anterior, puede ejecutar pyenv versionspara mostrar todas las versiones de Python
instaladas actualmente:$ pyenv versions
* system (set by /Users/realpython/.pyenv/version)
3.13.5
3.14.0rc2
Esta salida muestra que las versiones 3.13.5y 3.14.0rc2están instaladas. También muestra la instalación de Python del
sistema. Tenga en cuenta que el asterisco ( *) indica que la versión de Python del sistema está activa. Esto significa que aún
se refiere a la versión de Python del sistema al escribir el pythoncomando.
Si solo te interesa la versión activa actual, puedes usar el siguiente comando:
$ pyenv version
system (set by /Users/realpython/.pyenv/version)
Este comando es similar, versionspero solo muestra la versión activa de Python. Esta información es crucial al iniciar un
nuevo proyecto con una versión específica de Python.
Comprobación de la ruta ejecutable actual de Python:which
El whichcomando muestra la ruta completa a un programa ejecutable. Funciona no solo con los ejecutables del pyenventorno,
sino también con los comandos del sistema:
$ pyenv which python3
/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
$ pyenv which ls
/bin/ls
El primer comando muestra la ruta del ejecutable de Python activo en el pyenventorno. El segundo comando muestra que
también se puede obtener la ruta de comandos del sistema como ls.
Dado que pyenvfunciona mediante correcciones de calce (shims ), este comando permite ver la ruta completa del
ejecutable pyenven ejecución. Por ejemplo, si desea ver dónde pipestá instalado, puede ejecutar lo siguiente:
$ pyenv which pip3
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3
La salida muestra la ruta completa del sistema para pip. Esto puede ser útil al instalar aplicaciones de línea de comandos.
Desinstalación de versiones de Python:uninstall
En algún momento, podrías descubrir que ya no necesitas una instalación de Python. En ese caso, puedes desinstalarla con
la siguiente sintaxis de comando:
$ pyenv uninstall <version>
Al presionar Enter , se te preguntará si deseas eliminar la versión de destino. Si respondes "Sí" , se pyenveliminará la
versión por completo.
Eliminar anunciosConfiguración de la versión de Python a utilizar
Una de las partes más confusas de es cómo se resuelve pyenvexactamente el comando y qué comandos se pueden usar.
En , hay tres maneras de elegir qué versión de Python usar:pythonpyenv
1. pyenv shell <version>
2. pyenv local <version>
3. pyenv global <version>
Entonces, ¿cómo interactúan todas estas opciones? El orden de resolución es similar a esto:
En esta pirámide, el pythonorden de resolución de los comandos funciona de arriba a abajo, y los niveles superiores anulan a
los inferiores. Un pyenvcomando gestiona cada parte de esta pirámide. En las siguientes secciones, aprenderá sobre todos
estos comandos.
Versión de Python de la sesión de Shell actual:shell
Puedes usar el shellcomando para activar o desactivar una versión de Python específica del shell. Por ejemplo, si quieres
probar la 3.14.0rc2 versión preliminar , puedes ejecutar el siguiente comando en la ventana de tu terminal:
$ pyenv shell 3.14.0rc2
$ pyenv version
3.14.0rc2 (set by PYENV_VERSION environment variable)
Este comando activa la versión especificada configurando la PYENV_VERSION variable de entorno . Sobrescribe cualquier otra
configuración. Ahora puede probar las nuevas funciones de la versión especificada siempre que permanezca en la misma
sesión de shell.
Para desactivar la versión del shell, puedes utilizar la --unsetbandera:
$ pyenv shell --unset
$ pyenv version
system (set by /Users/realpython/.pyenv/version)Como su nombre indica, esta --unsetbandera anula la versión de shell especificada y regresa a la versión anterior de
Python. Elimina la PYENV_VERSIONvariable de entorno y restaura la última configuración en la pirámide de resolución.
La versión de Python local o específica de la aplicación:local
Puedes usar el localcomando para configurar una versión específica de Python para una aplicación o proyecto. A
continuación, se muestra un ejemplo de cómo localfunciona:
$ mkdir project/
$ cd project/
$ pyenv local 3.13.5
$ pyenv version
3.13.5 (set by /Users/realpython/Code/project/.python-version)
$ cd ../
$ pyenv version
system (set by /Users/realpython/.pyenv/version)
Este comando almacena la versión de Python deseada en un .python-versionarchivo en su directorio actual. Si la
tiene pyenven su entorno, se activará automáticamente (siempre que esté disponible) al acceder al project/directorio.
Es habitual guardar este .python-versionarchivo en la carpeta raíz del proyecto y tenerlo bajo control de versiones, por
ejemplo, con Git . De esta forma, pyenvse puede acceder a él y usar automáticamente el intérprete de Python correcto al
trabajar en esta carpeta.
Nota: Al utilizar local, no es necesario especificar un número de versión completo:
$ pyenv local 3.13
$ python --version
Python 3.13.5
$ pyenv local 3.13.4
$ python --version
Python 3.13.4
$ pyenv local 3.6
pyenv: version '3.6' not installed
Observa cómo pyenvse selecciona automáticamente la última versión disponible que cumple con tus restricciones. Si la
versión de destino no está instalada, recibirás un mensaje informativo.
Esta función es útil para gestionar varios proyectos con diferentes versiones de Python. Evita tener que comprobar
constantemente la versión de Python, lo que garantiza que este proyecto específico usará la versión de Python deseada.
Eliminar anuncios
La versión global de Python:global
Si desea utilizar una versión específica de Python globalmente en su sistema, puede usar el globalcomando:$ pyenv global 3.13.5
$ pyenv version
3.13.5 (set by /Users/realpython/.pyenv/version)
Este globalcomando establece 3.13.5 como la versión de Python que obtendrá cuando ejecute el pythoncomando en
cualquier ventana de terminal.
Si alguna vez desea volver a la versión del sistema de Python, puede ejecutar el siguiente comando:
$ pyenv global system
$ pyenv version
system (set by /Users/realpython/.pyenv/version)
Ahora puedes cambiar rápidamente entre diferentes versiones de Python, lo que constituye otra capacidad importante
cuando necesitas administrar múltiples versiones de Python en tu trabajo diario.
Gestión de entornos virtuales conpyenv
Los entornos virtuales son una parte importante de la gestión de proyectos de Python y se combinan bien con pyenv.
Nota: Si no tienes experiencia en entornos virtuales, consulta el tutorial Entornos virtuales de Python: una introducción .
En pyenv[nombre del complemento], pyenv-virtualenvtrabajar con múltiples versiones de Python y entornos virtuales es muy
sencillo. La buena noticia es que si usaste el script de instalación automática para instalar [nombre del complemento] pyenv,
ya lo tienes pyenv-virtualenvinstalado y listo para usar.
Nota: Si pyenv-virtualenvno está disponible en su pyenvinstalación actual, siga la guía de instalación oficial para
instalarlo.
Si te preguntas la diferencia entre pyenv, pyenv-virtualenv, y herramientas como virtualenvo venv, no eres el único. Esto es
lo que necesitas saber:
pyenvadministra múltiples versiones de Python.
virtualenvy venvadministrar entornos virtuales para una versión específica de Python.
pyenv-virtualenvAdministra entornos virtuales en múltiples versiones de Python.
En la práctica, pyenv-virtualenvfacilita el cambio entre múltiples entornos que requieren diferentes versiones de Python.
Creación de entornos virtuales
Para crear un entorno virtual con pyenvuna versión específica de Python, puede utilizar la siguiente sintaxis de comando:
$ pyenv virtualenv [python_version] <environment_name>
El python_versionargumento es opcional, pero conviene especificarlo para saber exactamente qué versión de Python se está
usando para crear el entorno. Si no se proporciona una versión, se pyenvusará la activa. El environment_nameargumento es
obligatorio y representa el nombre de la carpeta del entorno.
Una buena práctica es nombrar los entornos según el proyecto de destino. Esto es importante porque pyenvcrea entornos
virtuales en el $PYENV_ROOT/versions/<version>/envs/directorio. Si crea dos entornos con el mismo nombre para la misma
versión de Python, puede generar problemas.
Por ejemplo, si estuvieras trabajando en un proyecto llamado coolapp, podrías hacer lo siguiente:
$ pyenv virtualenv 3.13.5 coolapp_venv
$ pyenv versions
* system (set by /Users/realpython/.pyenv/version)
3.13.5
3.13.5/envs/coolapp_venv
3.14.0rc2
coolapp_venv --> /Users/realpython/.pyenv/versions/3.13.5/envs/coolapp_venv¡Listo! Has creado tu primer entorno virtual de Python con pyenvel pyenv-virtualenvcomplemento.
Eliminar anuncios
Listado de entornos virtuales
Para ver todos los entornos virtuales disponibles, ejecute este comando:
$ pyenv virtualenvs
3.13.5/envs/coolapp_venv (created from
/Users/realpython/.pyenv/versions/3.13.5)
coolapp_venv (created from /Users/realpython/.pyenv/versions/3.13.5)
Este comando enumera todos los entornos virtuales que se han creado pyenven su sistema.
Uso de entornos virtuales
Ahora que ha creado su entorno virtual, el siguiente paso es usarlo. Normalmente, debería activar sus entornos ejecutando lo
siguiente:
$ pyenv local coolapp_venv
Ya has visto este pyenv localcomando, pero esta vez especificas un entorno virtual en lugar de una versión de Python. Este
comando crea un .python-versionarchivo en tu directorio actual y activa automáticamente el entorno correspondiente.
Puedes comprobarlo ejecutando lo siguiente:
$ pyenv which python
/Users/realpython/.pyenv/versions/coolapp_venv/bin/python
$ file `pyenv which python`
/Users/realpython/.pyenv/versions/coolapp_venv/bin/python: symbolic link to
⮑ /Users/realpython/.pyenv/versions/3.13.5/bin/python
Puede ver un entorno virtual llamado coolapp_venven la salida. El pythonejecutable de ese entorno es un enlace
simbólico que apunta a la versión del intérprete correspondiente.
Para activar y desactivar manualmente su entorno Python, utilice los siguientes comandos:
$ pyenv activate <environment_name>
$ pyenv deactivate
Estos comandos activarán o desactivarán el entorno virtual de destino de la forma habitual. Verá cómo cambia el mensaje:
$ pyenv activate coolapp_venv
(coolapp_venv) $
En este ejemplo, se activa el coolapp_venventorno. Observe cómo el mensaje cambia de $a (coolapp_venv) $para indicar
visualmente que se encuentra en un entorno virtual de Python activo.Puedes crear tantos entornos virtuales como necesites. Idealmente, deberías crear un entorno dedicado para cada proyecto.
Después, puedes cambiar de proyecto y usar los pyenvcomandos correspondientes para administrar el entorno virtual
asociado.
En cierto sentido, pyenvtrata los entornos virtuales como versiones de Python. Esto significa que también se pueden usar los
comandos local, globaly similares con entornos virtuales. Para eliminar un entorno virtual, se usa el uninstallcomando.
Eliminación de entornos virtuales
Finalmente, puede eliminar un entorno virtual si ya no lo necesita. Para ello, puede usar el siguiente comando:
$ pyenv virtualenv-delete coolapp_venv
pyenv-virtualenv: remove /Users/realpython/.pyenv/versions/coolapp_venv? (y/N)
Si escribe y y presiona Enter , se pyenveliminará el entorno virtual de destino
del $PYENV_ROOT/versions/<version>/envs/directorio.
Como alternativa, puede usar el pyenv uninstall <virtualenv_name>comando para eliminar entornos virtuales. Este
comando funcionará de forma similar al anterior.
Eliminar anuncios
Conclusión
Aprendiste pyenva administrar varias versiones de Python de forma rápida y segura. También viste por qué depender de la
instalación de Python del sistema puede generar conflictos y limitaciones, y cómo pyenvte permite instalar, cambiar y
mantener versiones específicas de Python para diferentes proyectos de programación.
También instalaste pyenvy sus dependencias en sistemas tipo Unix y Windows. Después, practicaste los comandos
esenciales para configurar versiones globales, locales y específicas del shell. Finalmente, exploraste cómo administrar
entornos virtuales con el pyenv-virtualenvcomplemento.
En este tutorial, aprendiste a:
Instalar y configurar pyenven sistemas tipo Unix y Windows
Instale y administre múltiples versiones de Python independientemente de su sistema Python
Administrar versiones globales , locales y específicas de shellpyenv de Python mediante comandos
Cree y administre entornos virtuales en diferentes versiones y proyectos de Python
Ahora que posee estas habilidades, puede administrar con confianza las versiones de Python y los entornos virtuales de
cualquier proyecto. Esta flexibilidad le permitirá contribuir a una gama más amplia de proyectos y garantizar que su entorno
de desarrollo siempre satisfaga sus necesidades.















