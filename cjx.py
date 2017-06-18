# -*- coding: utf-8 -*-
#coding=utf8  
import urllib2
import urllib
import time
import json
import cv2  
import cv2.cv as cv
import requests
import json

def capture(key_value):
    capture = cv.CaptureFromCAM(0)
    key = key_value
    while True:
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera",img)
        if key == 'capture':
            filename = "face.jpg"    
            cv.SaveImage(filename,img)  
            print "图片截取成功"
            break
    del(capture)   
    cv.DestroyWindow("camera")

def detect():
    http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
    key = "QcAkT7ULfQ9TcSUnKKfMYRhDAtnuDHqD"
    secret = "QFquTx_My3G-uDvTgfFS20D-di9016i2"
    filepath = r"/home/pi/arduino_car/face.jpg"
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr=open(filepath,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)

    http_body='\r\n'.join(data)
#buld http request
    req=urllib2.Request(http_url)
#header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
    #req.add_header('Referer','http://remotserver.com/')
    #post data to server
        resp = urllib2.urlopen(req, timeout=5)
    #get response
        qrcont=resp.read()
        print qrcont
        dict = json.loads(qrcont)
        print type(dict)
        list = dict['faces']
        face_r_dir = list[0]
        face_token = face_r_dir['face_token']
        print face_token

    
    except urllib2.HTTPError as e:
        print e.read()
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    payload={'api_key':'QcAkT7ULfQ9TcSUnKKfMYRhDAtnuDHqD',
            'api_secret':'QFquTx_My3G-uDvTgfFS20D-di9016i2',
            'face_token':face_token ,
            'outer_id':'cjx'}


    r=requests.post(url,data=payload)
    print r.text
    data_2 =json.loads(r.text)
    result = data_2['results']
    confi_dir = result[0]
    confidence = confi_dir['confidence']
    print confidence
    f=open("/home/pi/arduino_car/data.html","w")
    f.write(str(confidence))
    f.close()
    return confidence


