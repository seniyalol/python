# -*- coding: utf-8 -*-
import re
import sys

def  per( centerX, centerY, centerZ, r, x1, y1, z1, x2, y2, z2):
    
    
    a = (x2-x1)*2+(y2-y1)*2+(z2-z1)*2
    b = 2*((x2-x1)(x1-centerX)+(centerY-y1)(y1-centerY)+(z2-z1)(z1-centerZ)) 
    c = (x1-centerX)*(x1-centerX)+(y1-centerY)*(y1-centerY)+(z1-centerZ)*(z1-centerZ)-r*r
    
    d0 = b*b-4*a*c
   
    if (d0<0):
       return "Коллизий не найдено"
    elif(d0==0):
       d1 = -b/2*a
       xq = x1 + d1*(x2-x1)
       yq = y1 + d1*(y2-y1)
       zq = z1 + d1*(z2-z1)
       return(xq,yq,zq)
    elif(d0>0):
       d1 = (-b-sqrt(d0))/(2*a) 
       d2 = (-b+sqrt(d0))/(2*a)  
       xa = x1 + d1*(x2-x1)
       ya = y1 + d1*(y2-y1)
       za = z1 + d1*(z2-z1)
       xb = x1 + d2*(x2-x1)
       yb = y1 + d2*(y2-y1)
       zb = z1 + d2*(z2-z1)
       return(xa,ya,za,xb,yb,zb)
    
        
    
def main():
    if len(sys.argv) != 11:
        print("Usage:\npython3 task2.py centerX, centerY, centerZ, r, x1, y1, z1, x2, y2, z2")
        exit(1)
    centerX, centerY, centerZ, r, x1, y1, z1, x2, y2, z2 =   sys.argv[1:11]
    print(per (float(centerX), float(centerY), float(centerZ), float(r), float(x1), float(y1), float(z1), float(x2), float(y2), float(z2)))
    
main()
