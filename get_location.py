# -*- coding: utf-8 -*-
'''
Created by VincentLee on 2015/7/22.
'''
import urllib2
import xml.etree.ElementTree as ET
city='武汉'
url='http://api.map.baidu.com/telematics/v3/geocoding?keyWord='+city+'&cityName=131&out_coord_type=gcj02&ak=1557cdbdaf2a1db4229cfb947438a7c5'
response=urllib2.urlopen(url)
html=response.read()
print html
d=ET.fromstring(html)
# lat=d.findtext('./results/result/location/lat')
print d
# print lat