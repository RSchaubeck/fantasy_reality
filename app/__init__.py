from flask import Flask
from app.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def index():
    return '<h1>Foobar</h1>'
