import store
from fastapi import FastAPI
from typing import Union
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') # <- ruta con la que pueden acceder desde la web
def get_list():
    return list(range(0,10))

@app.get('/contact')
def get_list():
    return {'Name': 'Neicer', 'Phone number': '0961181914'}

@app.get('/miPagina', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Esto es una prueba</h1>
        <p>Estoy muy emocionado de aprender este tipo de cosas en platzi</>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()