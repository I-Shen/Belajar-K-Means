# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:09:30 2021

@author: NUGI
"""

import math

class proses:
    def jarak(self, data1, data2):
        n=len(data1)
        total=0
        for i in range (n):
            total=total+math.pow(data1[i]-data2[i],2)
        return math.sqrt(total)

obj=proses()
jarak=obj.jarak([1,2], [3,3])
print("jarak", jarak)