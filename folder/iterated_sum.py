# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:47:40 2018

@author: Vaibhav
"""
sum=0
b=list(map(int,input().split()))
for i in range(b[0],b[1]+1):
    sum=sum+pow(i,2)
print(sum)    
    