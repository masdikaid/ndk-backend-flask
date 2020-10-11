from os import environ
from flask import redirect, render_template, abort
from .redirector import redirectapp, Url

@redirectapp.route("/")
def index():
    return redirect(environ["CENDEK_APP_URL"])

@redirectapp.route("/favicon.ico")
def favicon():
    return "https://www.google.com/favicon.ico"

@redirectapp.route("/<string:urlid>")
def redirector(urlid):
    try :
        urldata = Url.get(urlid)
        if len(urldata.target_url) > 1:
            return render_template("collection/url_collection.html", url=urldata)
        else :
            return redirect(urldata.target_url[0]["url"])
    except ValueError:
        abort(404)

@redirectapp.errorhandler(404)
def pageNotFound(error):
    return render_template("error/404.html", messege=error.description)



    

