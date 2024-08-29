import math
p=2
q=7
n=p*q
e=8
phi=(p-1)*(q-1)
while (e<phi):
    if (math.gcd(e,phi)==1):
        break
    else:
        e=e+1
k=2
msg=12.0
d=(1+(k*phi))/e
print("message data=",msg)
c=pow(msg,e)c)
m=pow(c,d)
m=math.fmod(m,n)
print("original message set=",m)
