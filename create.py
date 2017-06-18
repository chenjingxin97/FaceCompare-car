#coding=utf8  
import requests  
url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'  
payload = {'api_key': 'the key',   #Write your key,the same below  
               'api_secret': 'the serect',  #Secret
               'display_name':'the name',   #Design the name of the target yourself   
               'outer_id':'the id',   #Design the name of the target yourself  
               'face_tokens':'the foken' #The foken from "detect.py"
               }  
r = requests.post(url,data=payload)  
print r.text  
