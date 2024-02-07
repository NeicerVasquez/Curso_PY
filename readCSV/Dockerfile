FROM python:3.10

# el nombre que le pasemos puede ser cualquiera
WORKDIR /readCSV

# Como buena práctica es copiar los archivos de la carpeta
# en donde estamos ubicamos
# Copy <archivos_locales> <archivos_copias_en_contenedor>
COPY requirements.txt /readCSV/requirements.txt

# Instalar las dependencias y que esten disponibles
# cuando se crea el contenedor
RUN pip install --no-cache-dir --upgrade -r /readCSV/requirements.txt

COPY . /readCSV

CMD bash -c "while true; do sleep 1; done"



