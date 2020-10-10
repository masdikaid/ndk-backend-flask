from flask import redirect, render_template
from .redirector import redirectapp, Url

@redirectapp.route("/")
def index():
    return "<h1>Hello</h1>"

@redirectapp.route("/favicon.ico")
def favicon():
    return "https://www.google.com/favicon.ico"

@redirectapp.route("/<string:urlid>")
def redirector(urlid):
    # try :
    urldata = Url.get(urlid)
    if len(urldata.target_url) > 1:
        return urldata.target_url
    else :
        return redirect(urldata.target_url[0])
    # except ValueError:
    #     return redirect("404")



    

