from flask import Flask

app = Flask("meu app")

@app.route('/')  #decorators
def hello():
    return "Hello world"

@app.route('/novo')  #decorators
def novo():
    return "<h1> Nova Pagina <h1>"