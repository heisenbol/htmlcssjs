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
    
    albums = getAlbums()
    
    return template('albums', albums=albums)

@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='/var/www/htmlcssjs/static')

@route('/getImages', method='POST')
def getImages():
    session = bottle.request.environ.get('beaker.session')
    
    # TODO ensure user is loged in
    # if not, call 
    # bottle.abort(401, "Access denied")
    
    albumId = bottle.request.params.get('albumId',0)
    
    # TODO make request to directory service to retrieve the images of this user for given albumId
    
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
    if albumId != '0':
        imagesToReturn = random.randint(1, len(dummyImages))
        for x in range(0, imagesToReturn):
            result.append(dummyImages[x])		

    jsonImageData = json.JSONEncoder().encode(result)

    response.content_type = 'application/json; charset=utf-8'
    return [jsonImageData]

def getAlbums():
    dummyAlbums = []	
    dummyAlbums.append({'title': 'Album1 & ', 'id': 100})
    dummyAlbums.append({'title': 'Alb<b>um2</b>', 'id': 101})
    dummyAlbums.append({'title': 'Album3', 'id': 102})
    dummyAlbums.append({'title': 'Album4', 'id': 103})
    dummyAlbums.append({'title': 'Album5', 'id': 104})
    
    return dummyAlbums
    
