from flask import Flask, Blueprint
from .route import redirectapp

def redirector():
    app = Flask(__name__)
    app.register_blueprint(redirectapp)
    return app