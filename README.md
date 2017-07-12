# Face-_compare-car
The target detection based on machine learning.If you like,you could equip it at everywhere.

## Demo
![](https://github.com/chenjingxin97/Face-_compare-car/blob/master/Screenshot%20from%202017-07-11%2019-15-19.png)

Upload the image that you want to copare to your created Face++_target.

![](https://github.com/chenjingxin97/Face-_compare-car/blob/master/Screenshot%20from%202017-07-11%2019-16-36.png)

You will get the json of picture_foken

![](https://github.com/chenjingxin97/Face-_compare-car/blob/master/Screenshot%20from%202017-07-11%2019-16-46.png)

Display the result through your own ways.

## Requirements
* WebCamera
* Python3.5
* Raspberrypi 3B
* A image of the person that you want to detectc
* Face++ API and KEY
## usage
First, create target with Face++.

    $ python create.py

Second,get the image_foken of the person from detect.py

    $ python detect.py
    
Third, mobify the all souce codes with the image_foken you got just now,and then run camera_compare.py to get the final data.

    $ python camera_conpare.py

## Install

## Author
JINGXIN CHEN
