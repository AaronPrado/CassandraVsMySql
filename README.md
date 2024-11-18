# Comparativa entre Cassandra y MySQL

## Autores: **Celia** y **Aarón**

---


## Introducción

Este proyecto compara el rendimiento entre las bases de datos Cassandra y MySQL. Ofrece scripts para medir el rendimiento de ambas bases de datos en cuanto a inserción y consulta de datos.

## Contenido del Repositorio

- **cassandra/**: Scripts y configuración de Docker para ejecutar Cassandra.
  - **cassandraTest.ipynb**: Carga de datos, consultas y mediciones en Cassandra.
  - **docker-compose-cassandra.yml**:  Archivo Docker Compose para Cassandra.
  - **envCassandra.yaml**:  Conda Enviroment para Cassandra.


- **docker-compose.yml**: Archivo Docker Compose para MySQL.
- **envmysqltask.yaml**: Conda Enviroment para MySQL.
- **generador_dataset.py**: Script para generar los datos de prueba.
- **dataset_falso.csv**: Datos de prueba generados.
- **medidor.py**: Consultas en MySQL .

## Configuración y Ejecución

### Requisitos Previos

Asegúrate de tener instalados los siguientes programas:
- **Docker**: Para ejecutar ambos servicios de base de datos.
- **Python 3**: Requerido para ejecutar los scripts de generación y carga de datos.

### Configuración de Docker y entornos

1. **Iniciar Cassandra**:
   ```bash
   docker-compose -f docker-compose_Cassandra.yml up

2. **Iniciar MySQL**:
   ```bash
   docker-compose -f docker-compose.yml up

3. **Importar el entorno de Cassandra**:
   ```bash
   conda env create -f cassandra/envCassandra.yaml

4. **Importar el entorno de MySQL**:
   ```bash
   conda env create -f mysql/envmysqltask.yaml

### Ejecución de scripts

1. **Para generar un conjunto de datos de prueba, ejecuta el script generador_dataset.py (puedes modificar el número de registros de prueba**

2. **Ejecutar el script `cassandraTest.ipynb` para Cassandra**
   Este script está diseñado para cargar los datos en Cassandra, realizar consultas y medir el rendimiento. Para ejecutarlo:

      Asegúrate de haber activado el entorno de Conda para Cassandra:
   ```bash
   conda activate envmysqltask
   ```

     Inicia Jupyter Notebook

      Abre el archivo cassandraTest.ipynb y ejecuta las celdas en orden.

4. **Ejecutar el script medidor.py para MySQL**
Este script realiza las consultas en la base de datos MySQL y mide el rendimiento.

    Asegúrate de haber activado el entorno de Conda para MySQL:

    ```bash
    conda activate envmysqltask
Ejecuta el script python medidor.py

    
Este script realizará las consultas y mostrará el tiempo de ejecución de las operaciones.






