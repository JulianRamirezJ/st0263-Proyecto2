# st0263-Proyecto2
## info de la materia: st0263 Topicos Especiales en Telematica
#
## Estudiante(s): Julian Andres Ramirez Jimenez jaramirezj@eafit.edu.co; Samuel David Villegas Bedoya sdvillegab@eafit.edu.co; Julian Giraldo Perez jgiraldop@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Proyecto 2, AutoScaling
#
## 1. Breve descripción de la actividad
En esta actividad, se implementó un servicio de autoescalado utilizando instancias EC2 de AWS de Amazon. El sistema consta de tres componentes distintos: un monitor C, un monitor S y un controlador de autoescalado.

El monitor C se encarga de tomar las métricas de CPU de las instancias. Para esta actividad, se simuló el funcionamiento de este componente. El monitor S se comunica con el monitor C a través de gRPC y obtiene las métricas generadas. A su vez, mantiene actualizada una memoria compartida. El controlador de autoescalado monitorea constantemente esta memoria y realiza el escalado hacia arriba o hacia abajo según sea necesario.

Para este proyecto, se estableció un número mínimo de dos instancias y un máximo de cinco. La métrica utilizada para determinar el escalado hacia arriba es que el uso promedio de CPU de las instancias alcance el 70%. En caso contrario, para el escalado hacia abajo, la métrica es que el uso promedio de CPU esté por debajo del 30%.

Toda la implementación se realizó en Python, haciendo uso de características como gRPC, multiprocessing y el SDK de Amazon. El grupo de autoescalado funciona mediante la simulación del uso de CPU de las diferentes instancias en el grupo.

En conclusión, se desarrolló un sistema de autoescalado utilizando instancias EC2 de AWS, compuesto por un monitor C, un monitor S y un controlador de autoescalado. El sistema utiliza métricas de CPU y se implementó en Python, aprovechando las funcionalidades de gRPC, multiprocessing y el SDK de Amazon.

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Durante la actividad se lograron los siguientes aspectos:

- Se implementó el Monitor C, el cual se ejecuta en cada instancia EC2 en funcionamiento.
 - Se implementó el Monitor S, encargado de recibir las métricas del Monitor C de cada instancia.
- Se implementó el Controlador ASG, que utiliza la información proporcionada por el Monitor S para tomar decisiones sobre la creación o eliminación de instancias utilizando el SDK de la API.
- Se estableció la comunicación gRPC entre el Monitor S y los Monitores C ubicados en cada instancia, utilizando los mensajes Heartbeat y GetMetrics.
- Se implementó una memoria compartida para la comunicación entre el Monitor S y el Controlador ASG.
- Se desarrolló la simulación del uso de la CPU de cada instancia, la cual se encuentra dentro del Monitor C.

### 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- En general todo lo propuesto se desarrollo satisfactoriamente

## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

En general el diseño de esta aplicacion va de acuerdo a lo propuesto en clase
![proyecto2 drawio (1)](https://github.com/JulianRamirezJ/st0263-Proyecto2/assets/110442546/b477b348-ce1f-40b4-9b08-0ca965b352b2)

Como podemos ver en la imagen la arquitectura se compone de 3 componentes, que son Monitor S, Monitor C y Controller ASG.
El Monitor C desempeña la función crucial de recolectar las métricas de uso de la CPU de las instancias. Si bien en esta implementación se simuló su funcionamiento, es importante destacar que normalmente estaría en ejecución en cada instancia EC2 de Amazon. 
Por otro lado, el Monitor S establece una comunicación bidireccional mediante gRPC con el Monitor C, permitiéndole obtener las métricas generadas por este último. Además, el Monitor S es responsable de mantener actualizada una memoria compartida, la cual actúa como un medio de comunicación entre los diferentes componentes. 

El Controlador de Autoescalado, por su parte, monitorea constantemente esta memoria compartida y toma decisiones de escalado hacia arriba o hacia abajo en función de las métricas recibidas. Es importante mencionar que tanto el Monitor S como el Controlador ASG son lanzados como procesos separados en el mismo programa y utilizan un diccionario en memoria compartida para su intercambio de información. Todo el sistema ha sido implementado en Python, haciendo uso de características como gRPC, el lenguaje de programación Python y el SDK de Amazon.



## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Para el desarrollo del proyecto se utilizaron los siguientes elementos y tecnologías:

1. Python 3: Se eligió Python como lenguaje de programación principal debido a su versatilidad, facilidad de uso y amplia disponibilidad de bibliotecas y que facilitan el desarrollo de programas para realizar operaciones sobre la infraestructura.

2. gRPC: Se utilizó gRPC como el framework de comunicación entre los diferentes componentes del sistema, permitiendo una comunicación eficiente y de alto rendimiento basada en el protocolo de buffers de Google.

3. Multiprocessing: Se hizo uso del módulo de multiprocessing de Python para gestionar la ejecución concurrente de los diferentes componentes del sistema, como el Monitor C, el Monitor S y el Controlador ASG. Esto permitió aprovechar al máximo los recursos del sistema y mejorar la eficiencia del procesamiento.

4. Memoria compartida: Se implementó una memoria compartida utilizando el módulo de multiprocessing de Python, que permitió a los componentes del sistema compartir información de manera segura y eficiente. El uso de memoria compartida fue fundamental para mantener actualizadas las métricas y decisiones de escalado.

5. Compilador del protocol buffer: Se utilizó el compilador del protocol buffer para generar el código fuente de los mensajes y servicios definidos en los archivos .proto. Esto permitió establecer la comunicación entre los componentes del sistema de manera sencilla y eficiente.

6. Random y Time: Se utilizaron los módulos de Random y Time de Python para simular el uso de CPU de las diferentes instancias. Estos módulos permitieron generar valores aleatorios de métricas y controlar el tiempo de espera entre mediciones, lo que contribuyó a la simulación realista del sistema.

7. SDK de Amazon para Python: Se empleó el SDK de Amazon para Python para interactuar con los servicios de AWS, específicamente para realizar las operaciones de escalado hacia arriba o hacia abajo en función de las métricas obtenidas. El uso del SDK facilitó la integración con los servicios de AWS y brindó un enfoque práctico para la gestión de instancias EC2.

Estas elecciones tecnológicas y herramientas fueron seleccionadas en base a su capacidad para cumplir con los requisitos del proyecto, proporcionar una implementación eficiente y facilitar la integración con los servicios de AWS.
### 3.1. Como se compila y ejecuta.
Para compilar y ejecutar el programa debe asegurarse que tenga instalado python, y las librerias proto, boto3.
Ademas debe tener AWS CLI instalado, es a travez de este que debe realizar la configuracion de seguridad y autenticacion de su cuenta de AWS (donde se crearan las instancias).

### 3.2. Detalles del desarrollo.

Este proyecto esta pensado para correr en una maquina manager y varias maquinas que sean parte del grupo de autoScaling. 

## 4. Detalles técnicos

El proyecto fue desarrollado en:
- python 3.10.6.
Para la comunicacion grpc entre monitor C y monitor S se utilizaron las librerias
- grpcio 1.51.3
- grpc-tools 1.51.3
Para la comunicaicon con AWS SDK
- boto3 1.26.133

## 5. descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En general se tiene un archivo de configuracion para definir en que puerto correran los Monitores C

## 6. Detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
En general el proyecto esta pensado para ser clonado en la direccion /home/ubuntu/ y a partir de alli se ejecutara el programa dependiendo del rol que tenga la maquina en la que se este realizando la operacion. 
## 
### Estructura
![image](https://github.com/JulianRamirezJ/st0263-Proyecto2/assets/110442546/a234c4d1-33c8-4de3-867f-824684d4588f)

## Instancia AWS
Todo lo descrito aqui ya esta aplicado en diversas instancias de AWS

# 7. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## 8. IP o nombres de dominio en nube o en la máquina servidor.
18.210.179.173 POR DEFINIR

## 9. Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En el numeral anterior ya se describieron todos los parametros y configuraciones que se deben aplicar.

## 10. como se lanza el servidor.
- Inicie su instancia manager
- Asegurarse de tener el puerto 8080 abierto para comunicacion TCP desde cualquier ip
- git clone de este repositorio
- Correr el setup ssh
- aqui correra el main.py para inicar el programa

## 11. Guia de como un usuario utilizaría el software o la aplicación
Una vez el usuario haya lanzado el servidor este podra observar como el nodo manager se encargara de aplicar el scaling up o scaling down segun el uso de cpu (simulado) que se tenga a traves de las diferentes instancias que esten activas.


## 12. opcionalmente - si quiere mostrar resultados o pantallazos 
Por desarrollar


## 13. otra información que considere relevante para esta actividad.
Todo lo relevante para esta actividad ya esta contenido en los otros numerales

## Referencias:

- https://docs.python.org/3/library/asyncio.html
- https://grpc.io/docs/languages/python/quickstart/
- https://docs.python.org/3/library/multiprocessing.html

#### versión README.md -> 1.0 (2022-agosto)
