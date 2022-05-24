# api-py-gitBranch
en esta clase vamos a usar la libreria https://fastapi.tiangolo.com/es/ para crear nuestras apis

# crear un endpoint 
para ello vamos a definir con @app.get("/mi-endpoint") que nos permitira acceder al endpoint mediante el Path. "Path" aquí se refiere a la última parte de una URL comenzando desde el primer /.

Entonces, en una URL como:
localhost:8000/items/foo
el path sería:
/items/foo

Cuando construyes una API, el "path" es la manera principal de separar los "intereses" y los "recursos".

app es una instancia del objeto app = FastAPI() que es el que manejara nuestra api

## Operaciones

"Operación" aquí se refiere a uno de los "métodos" de HTTP.

Uno como:
POST: para crear datos.
GET: para leer datos.
PUT: para actualizar datos.
DELETE: para borrar datos.

Así que en OpenAPI, cada uno de estos métodos de HTTP es referido como una "operación".


# ver las apis creadas 
accediendo a esta url podemos acceder a las apis creadas http://127.0.0.1:8000/docs