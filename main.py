import zipfile
import os
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuración del navegador
options = Options()
# options.add_argument('--headless')  # Comentado para que sea visible durante la ejecución (opcional)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Ruta al driver de Chrome
chrome_path = "/ruta/al/driver/chromedriver"  # Cambia esto a la ruta correcta en tu sistema

# Ruta de descarga
download_path = "C:\\Users\\caray\\Downloads"

# Inicializar el navegador
driver = webdriver.Chrome(options=options)

# URL de la página
url = "https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads"

# Configurar las opciones de descarga
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False,
}

options.add_experimental_option("prefs", prefs)



# Abrir la página en el navegador
driver.get(url)

try:
    # Esperar hasta 180 segundos para que el elemento con ID 'dwnnibrs-card' esté presente
    WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.ID, 'dwnnibrs-card')))

    # ... (código para seleccionar año, ubicación, tipo de datos, y hacer clic en "Download")
    # Seleccionar el año 
    year_dropdown = driver.find_element(By.ID, 'dwnnibrscol-year-select')
    year_dropdown.click()
    year_option = driver.find_element(By.XPATH, "//nb-option[contains(text(), '2022')]")
    year_option.click()

    # Seleccionar la ubicación 
    location_dropdown = driver.find_element(By.ID, 'dwnnibrsloc-select')
    location_dropdown.click()
    location_option = driver.find_element(By.XPATH, "//nb-option[contains(text(), 'Florida')]")
    location_option.click()

    download_dir = "C:\\Users\\caray\\Downloads"

    #Seleccionar "Victims"
    data_type_dropdown = driver.find_element(By.ID, 'dwnnibrs-download-select')
    data_type_dropdown.click()
    victims_option = driver.find_element(By.XPATH, "//nb-option[contains(text(), 'Victims')]")
    
    # Obtener el nombre dinámicamente (en minúsculas)
    zip_file_name = victims_option.text.lower()
    
    victims_option.click()

    # Hacer clic en el botón "Download"
    download_button = driver.find_element(By.ID, 'nibrs-download-button')
    download_button.click()

    # Esperar a que el archivo se descargue completamente
    time.sleep(10)  # Puedes ajustar este tiempo según la velocidad de descarga

    # Ruta completa del archivo ZIP
    zip_file_path = os.path.join(download_dir, zip_file_name + ".zip")

    # Directorio donde se extraerán los archivos
    extract_path = os.path.join(download_dir, "extracted")

    # Crear directorio de extracción si no existe
    os.makedirs(extract_path, exist_ok=True)

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    print(f"Archivos extraídos en: {extract_path}")

except Exception as e:
    print(f"Error esperando al elemento: {e}")


##### LIMPIEZA PARA GENERAR EL CSV
    
import os
import pandas as pd

# Rutas en formato consistente usando barras diagonales
download_dir = "C:/Users/caray/Downloads"
extract_path = os.path.join(download_dir, "extracted")
download_path = "C:/Users/caray/Downloads"



# Ruta completa del archivo Excel descargado
excel_file_path = os.path.join(extract_path, "Victims_Age_by_Offense_Category_2022.xlsx")

# Verificar y crear el directorio 'extracted' si no existe
if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Verificar la existencia del archivo y el contenido del directorio 'extracted'
print(f'Ruta del archivo Excel: {excel_file_path}')
print(f'Contenido del directorio extracted: {os.listdir(extract_path)}')


df = pd.read_excel(excel_file_path)

# Mostrar las primeras filas del DataFrame
df.head()

# Visualizar los valores de la fila 4
fila_5 = df.iloc[3].tolist()

# Quedarse con los valores a partir del índice 2
nueva_lista = fila_5[2:]

# Mostrar la lista resultante
print(nueva_lista)

fila_5 = df.iloc[3].tolist()

# Agregar "Crimes Against Property" como primer elemento
nueva_lista_f = ["Crimes Against Property"] + fila_5[2:]

# Mostrar la lista resultante
print(nueva_lista_f)

# Encontrar el índice de la fila donde está "Crimes Against Property"
indice_crimes_against_property = df[df['Victims'] == 'Crimes Against Property'].index[0]

# Seleccionar las filas debajo de "Crimes Against Property"
df_crimes_against_property = df.iloc[indice_crimes_against_property + 1:]

# Mostrar el DataFrame resultante
print(df_crimes_against_property)

# Encontrar el índice de la última fila
indice_ultima_fila = df_crimes_against_property.index[-1]

# Eliminar la última fila
df_sin_footer = df_crimes_against_property.drop(indice_ultima_fila)

# Mostrar el DataFrame resultante
print(df_sin_footer)

# Obtener los nombres de las columnas del DataFrame df_sin_footer
nombres_columnas = df_sin_footer.columns

# Mostrar los nombres de las columnas
print(nombres_columnas)

# Eliminar la columna "Unnamed: 1" ya que alli se encuentran los totales
df_sin_footer = df_sin_footer.drop(columns=['Unnamed: 1'])

# Obtener los nombres de las columnas del DataFrame actual
nombres_columnas_actuales = df_sin_footer.columns

# Obtener la lista de nuevos nombres de columnas (nueva_lista_f tiene que tener la misma longitud que nombres_columnas_actuales)
nueva_lista_f #definido mas arriba

# Renombrar las columnas
diccionario_renombres = dict(zip(nombres_columnas_actuales, nueva_lista_f))
df_final = df_sin_footer.rename(columns=diccionario_renombres)

# Mostrar el DataFrame resultante
print(df_final)

# Guardar DataFrame como CSV en la misma ubicación que el archivo Excel
csv_file_path = os.path.splitext(excel_file_path)[0] + '.csv'
df_final.to_csv(csv_file_path, index=False)

# Verificar la existencia del archivo CSV y el contenido del directorio 'extracted'
print(f'Ruta del archivo CSV: {csv_file_path}')
print(f'Contenido del directorio extracted: {os.listdir(extract_path)}')


# Bucle infinito para mantener el script en ejecución
while True:
    pass




