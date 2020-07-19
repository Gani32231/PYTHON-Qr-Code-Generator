# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:29:01 2020

@author: wwwds
"""


import pyqrcode
import pypng
from pyqrcode import QRCode
s = "www.google.com"
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png("myqrcode.png",scale=6)