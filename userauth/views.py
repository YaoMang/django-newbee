from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader

from .models import userBaseInfo, userTokenInfo, serverUniversalKey

import uuid

# Create your views here.


# Token functions
def token_check(token: str):
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    import base64

    encryptInfo = serverUniversalKey.objects.get(keyname = 'tokenEnc')

    ciper = AES.new(base64.b64decode(encryptInfo.key_value), AES.MODE_CBC)
    token_data = ciper.decrypt(token)
    token_dict = dict(token_data)

    hash_val = token_dict['hash']
    del token_dict['hash']

    if hash_val == hash(token_dict):
        return True
    else:
        return False

def token_generate(userInfo: userBaseInfo):
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from datetime import datetime
    import base64

    encryptInfo: serverUniversalKey
    # create encrypt key (if not exist)
    try:
        encryptInfo = serverUniversalKey.objects.get(keyname = 'tokenEnc')
    except KeyError(serverUniversalKey.DoesNotExist):
        encryptInfo = serverUniversalKey(
            keyname = 'tokenEnc',
            keyType = 'AES256-CBC',
            key_value = base64.b64encode(get_random_bytes(16))
        )
        
    # create token
    userId = userInfo.pk
    token_key = get_random_bytes(16)
    timestamp = datetime.utcnow()
    
    data_token = {
        'uid' : userId,
        'psk' : token_key,
        'tsp' : timestamp
    }

    value_hash = hash(data_token)

    data_token['hash'] = value_hash

    token_db = userTokenInfo(
        userInfo = userInfo, 
        encryptInfo = encryptInfo,
        token_key = base64.b64encode(token_key)
        )
    
    token_db.save()

    ciper = AES.new(base64.b64decode(encryptInfo.key_value), AES.MODE_CBC)
    token = ciper.encrypt(data_token)
    
    return  base64.urlsafe_b64encode(token)




# Simply just view
# Should be moduled and do not take specific functions

def VIEW_index(request: HttpRequest):
    # Render page and response
    template = loader.get_template('userauth/userauth_embed.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def VIEW_signin(request: HttpRequest):
    try:
        userinfo = userBaseInfo.objects.get(username=request.POST['username'])

    except (KeyError, userBaseInfo.DoesNotExist):
        return HttpResponse("User doesn't exist")

    if userinfo.password == request.POST['password']:
        return HttpResponse("Sign in")
        
    else:
        return HttpResponse("Username or password error")

def VIEW_signup(request: HttpRequest):
    userinfo = userBaseInfo(username=request.POST['username'], password=request.POST['password'])
    userinfo.save()
    return HttpResponse("Sign up")

# Functional functions

def login(request: HttpRequest):
    # Check request method
    # If not POST, decline request
    if request.method != "POST":
        res = HttpResponse("bad request")
        res.status_code = 403
        return res

    # Check cookies, token could also be send through this
    # If matches stored content, pop tips
    if 'token' in request.COOKIES:
        token = request.COOKIES['token']

    # Check username and password
    # Password should be encrypted
    

    # Response with a new token

def logout(request: HttpRequest):
    # Delete tokens on userdevice


    # Delete tokens on server


    # Redirect user to mainpage
    return

def register(request: HttpRequest):
    return