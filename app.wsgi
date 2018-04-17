#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging

import os
os.chdir(os.path.dirname(__file__))
import bottle
import bcrypt
import time
from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64decode
from base64 import b64encode
import hmac
import hashlib
import urllib.parse
import json
from bottle import route, run, template, response, redirect
from bottle.ext import beaker
from bottle import static_file
import random

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
#application = bottle.default_app()
# use beaker middleware for session handling
application = beaker.middleware.SessionMiddleware(bottle.default_app(), session_opts)

# do not cache tempaltes
bottle.debug(True)

@route('/')
def index():
    response.content_type = 'text/html; charset=utf-8'
    session = bottle.request.environ.get('beaker.session')
    return template('albums')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/var/www/htmlcssjs/static')

@route('/getImages', method='POST')
def login():
    session = bottle.request.environ.get('beaker.session')
    
    # TODO ensure user is loged in
    # if not, call 
    # bottle.abort(401, "Access denied")
    
    folder = bottle.request.params.get('folder',False)
    
    # TODO make request to directory service to retrieve the images of this user for given folder
    

    dummyImages = []
    dummyImages.append({'fileName': 'static/imgs/01.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/02.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/03.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/04.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/05.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/06.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/07.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/08.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/09.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/10.jpg', 'commentCount': random.randint(1, 100)})
    dummyImages.append({'fileName': 'static/imgs/11.jpg', 'commentCount': random.randint(1, 100)})

    result = []
    imagesToReturn = random.randint(1, len(dummyImages))
    for x in range(0, imagesToReturn):
        result.append(dummyImages[x])		

    jsonImageData = json.JSONEncoder().encode(result)

    response.content_type = 'application/json; charset=utf-8'
    return [jsonImageData]



    
