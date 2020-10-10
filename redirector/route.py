from flask import redirect
from .redirector import redirectapp

@redirectapp.route("/")
def index():
    return redirect("http://cendek.com")

@redirectapp.route("/<string:urlid>")
def redirector(urlid):
    pass


    

