from firebase_admin import initialize_app, firestore, credentials
from os import environ

cred = credentials.Certificate({
    "type": environ["TYPE"],
    "project_id": environ["PROJECT_ID"],
    "private_key_id": environ["PRIVATE_KEY_ID"],
    "private_key": environ["PRIVATE_KEY"].replace('\\n', '\n'),
    "client_email": environ["CLIENT_EMAIL"],
    "client_id": environ["CLIENT_ID"],
    "auth_uri": environ["AUTH_URI"],
    "token_uri": environ["TOKEN_URI"],
    "auth_provider_x509_cert_url": environ["AUTH_PROVIDER_X509_CERT_URL"],
    "client_x509_cert_url": environ["CLIENT_X509_CERT_URL"]
})

initialize_app(cred)
db = firestore.client()

def getUrlData(urlid):
    urldata = db.collection(u"shortenurl").document(urlid).get()
    if urldata.exists :
        return urldata.to_dict()
    elif not urldata.exists :
        raise ValueError("data not found")

def setVisitorData(urlid, visitordata):
    urldata = db.collection(u"shortenurl").document(urlid)
    if urldata.get().exists :
        urldata = urldata.update({u"visitor" : firestore.ArrayUnion([visitordata])})
    else :
        raise ValueError("data not found")

