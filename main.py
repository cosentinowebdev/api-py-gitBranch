from fastapi import FastAPI
app = FastAPI()

@app.get("/hola")
def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

@app.get("/hola-mundo")
def hello():
  return {"Hello world!"}