import statistics
import math

x=[60,61,65,63,98,99,90,95,91,96]

mean=statistics.mean(x)

z=[]
m=[]

#calculating mean
for i in x:
          y=i-mean
          z.append(y)
          print(z)

#calculating the square
for i in z:
          y=i*i
          m.append(y)
          print(y)

#calculating variance
mean2=statistics.mean(m)

#calculating standard deviation
sd=math.sqrt(mean2)

print("standard deviation=",sd)