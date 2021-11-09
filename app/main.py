from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}')
def hello_world(name: str):
    return f'hello {name}'
