def ballcollide(x1,y1,r1,x2,y2,r2): 
 d=dist(x1,y1,x2,y2) 
 if d<=r1+r2: 
 print("colliding") 
 else: 
 print("not colliding") 
import math as m 
def dist(x1,y1,x2,y2): 
 return m.sqrt(m.pow((x1-x2),2)+m.pow((y1-y2),2)) 
ballcollide(2,2,1,3,4,2) 
ballcollide(2,3,4,5,6,7) 
'''
output:
colliding
colliding
'''
