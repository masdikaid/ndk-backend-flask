from flask import Blueprint
from datetime import datetime

from .firebase import getUrlData, setVisitorData

redirectapp = Blueprint("redirector", __name__)

class Url:

    def __init__(self, urlid, target_url, deleted_at, expiration):
        self.urlid = urlid
        self.target_url = self.convertTargetUrl(target_url)
        self.deleted_at = deleted_at
        self.expiration = self.convertExpiration(expiration)
    
    def hit(self, request):
        visitor = {
            "timestamp" : datetime.now(),
            "ipaddress" : request.remote_addr,
            "device" : request.user_agent.platform,
            "browser" : request.user_agent.browser
        }
        setVisitorData(self.urlid, visitor)

    @staticmethod
    def get(urlid):
        urldata = getUrlData(urlid)
        return Url(urlid, 
                urldata["target_url"], 
                urldata["delete_at"], 
                urldata["expiration"]
            )

    @classmethod
    def convertTargetUrl(self, target_url):
        if not len(target_url) == 0 :
            return [{"title":url["title"] if "title" in url else None, 
                    "url":url["url"], "desc":url["desc"] if "desc" in url else None, 
                    "thumb":url["thumb"] if "thumb" in url else None} for url in target_url ]
        else :
            raise ValueError("Target Url Not Found !")

    @classmethod
    def convertExpiration(self, expirationdata):
        if type(expirationdata) == dict :
            return {
                "expiration_at" : expirationdata["expiration_at"],
                "expiration_messege" : expirationdata["expiration_messege"] 
            }
        else :
            return None

