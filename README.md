# Web Scraping con Selenium en Python:

![Web Scraping](webscraping.jpg)


## Definición:
El web scraping con Selenium en Python es la técnica de automatizar la extracción de datos de sitios web. Utilizando Selenium, una biblioteca para la automatización de navegadores, se pueden realizar acciones interactivas como hacer clic en botones y completar formularios para extraer información de manera programática.

## Importancia:

Recopilación de Datos Estructurados: Permite extraer información específica de páginas web, incluyendo tablas y listas.
Manejo de Contenido Dinámico: Puede interactuar con páginas web que utilizan JavaScript para cargar datos dinámicamente.
Automatización de Tareas Web: Facilita la automatización de acciones en sitios web, como iniciar sesión y realizar búsquedas.
Análisis Competitivo: Permite el monitoreo de competidores al recopilar datos sobre productos y precios.
Actualización de Datos: Se utiliza para rastrear cambios en la información y mantener bases de datos actualizadas.
Pruebas Automatizadas: Es útil en el desarrollo de software para realizar pruebas automatizadas en aplicaciones web.

## Desafio

- Deben ser desarrollados los siguientes puntos completamente en python

1. Ir a:

https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home

2. Sección "Documents & Downloads"

3. En la sección "National Incident-Based Reporting System (NIBRS) Tables" elegir table: Victims, año: 2022, location: Florida

4. Descargar archivo

5. Con pandas leer zip y elegir el archivo: Victims_Age_by_Offense_Category_2022.xlsx

6. Elegir categoria Crimes Against Property y generar csv sin totales, footer, ni index

- Se requiere un código que ejecute todas las partes, desde el webscraping hasta la generación del archivo csv, debe entregar el código completo y el archivo resultado.

## Solucion y Consideraciones:
La solucion esta en el main.py: el cual baja el archivo requerido para luego realizar su posterior limpieza, dando como resultado un archivo.csv con los requerimientos solicitados.
Se debe configurar la ruta de Descarga de los archivos si se prefiere otra (Yo configure la ruta por defecto)

Link del video de la solucion:

https://youtu.be/fBbCjY0b4v4


Contacto o sugerencias:
email : rodribogado50@gmail.com