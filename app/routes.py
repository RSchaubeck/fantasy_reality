from flask import Blueprint
import psycopg2
import os

bp = Blueprint("main", __name__, url_prefix="")
CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}
