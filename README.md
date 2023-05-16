# st0263-Proyecto2
## info de la materia: st0263 Topicos Especiales en Telematica
#
## Estudiante(s): Julian Andres Ramirez Jimenez jaramirezj@eafit.edu.co; Samuel David Villegas Bedoya sdvillegab@eafit.edu.co; Julian Giraldo Perez jgiraldop@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Proyecto 2, AutoScaling
#
# 1. breve descripción de la actividad
#
En esta actividad se implemento un servicio de autoScaling el cual opera sobre instancias EC2 de AWS de amazon.
Este grupo de autoScaling funcionara a traves de la simulacion del uso de cpu de las diferentes instancias que esten corriendo en el grupo.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Entre los aspectos propuestos para la actividad se logro:
- Implementacion del Monitor C, el cual correra en cada instancia EC2 que este corriendo.
- Implementacion del Monitor S, el cual se encargara de recibir las metricas del monitor C de cada instancia.
- Implementacion del controladorASG, el cual a partir de la informacion que obtenga el monitor S decidira si montar o bajar instancias a traves del API SDK.
- Implementacion de comunicacion grpc entre el monitor S y los monitores C ubicados en cada instancia. (Hearbeat y getMetrics)
- Implementacion de memoria compartida para la comunicacion entre el monitor S y el controladorASG
- Implementacion de la simulacion del uso de cpu de cada instancia (la simulacion se desarrollo dentro del monitor C)

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- En general todo lo propuesto se desarrollo satisfactoriamente

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

En general el diseño de esta aplicacion va de acuerdo a lo propuesto en clase
![proyecto2 drawio](https://github.com/JulianRamirezJ/st0263-Proyecto2/assets/110442546/296ac5e7-ea1c-4e8c-8ed8-ec386cce8b70)



# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.
Para compilar y ejecutar el programa debe asegurarse que tenga instalado python, y las librerias proto, boto3.
Ademas debe tener AWS CLI instalado, es a travez de este que debe realizar la configuracion de seguridad y autenticacion de su cuenta de AWS (donde se crearan las instancias).
## detalles del desarrollo.

Este proyecto esta pensado para correr en una maquina manager y varias maquinas que sean parte del grupo de autoScaling. 

## detalles técnicos

El proyecto fue desarrollado en:
- python 3.10.6.
Para la comunicacion grpc entre monitor C y monitor S se utilizaron las librerias
- grpcio 1.51.3
- grpc-tools 1.51.3
Para la comunicaicon con AWS SDK
- boto3 1.26.133

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En general se tiene un archivo de configuracion para definir en que puerto correran los Monitores C

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
En general el proyecto esta pensado para ser clonado en la direccion /home/ubuntu/ y a partir de alli se ejecutara el programa dependiendo del ron que tenga la maquina en la que se este realizando la operacion. 
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 
### Estructura
![image](https://github.com/JulianRamirezJ/st0263-Proyecto2/assets/110442546/a234c4d1-33c8-4de3-867f-824684d4588f)

## Instancia AWS
Todo lo descrito aqui ya esta aplicado en diversas instancias de AWS

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.
18.210.179.173 POR DEFINIR
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En el numeral anterior ya se describieron todos los parametros y configuraciones que se deben aplicar.

## como se lanza el servidor.
- Inicie su instancia manager
- Asegurarse de tener el puerto 8080 abierto para comunicacion TCP desde cualquier ip
- git clone de este repositorio
- Correr el setup ssh
- aqui correra el main.py para inicar el programa

## una mini guia de como un usuario utilizaría el software o la aplicación
Una vez el usuario haya lanzado el servidor este podra observar como el nodo manager se encargara de aplicar el scaling up o scaling down segun el uso de cpu (simulado) que se tenga a traves de las diferentes instancias que esten activas.


## opcionalmente - si quiere mostrar resultados o pantallazos 
Por desarrollar


# 5. otra información que considere relevante para esta actividad.
Todo lo relevante para esta actividad ya esta contenido en los otros numerales

# referencias:

## https://docs.python.org/3/library/asyncio.html
## https://grpc.io/docs/languages/python/quickstart/
## https://docs.python.org/3/library/multiprocessing.html

#### versión README.md -> 1.0 (2022-agosto)
