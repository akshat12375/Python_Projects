import random
le=['a','A','b','b','c','f','G','N','L','p','y','z']
nu=['1','2','3','4','5','6','7','8','9']
sy=['!','@','#','$','%','^','*','(','<','?',',','>']
l=int(input("how many letters do you want\n"))
n=int(input("how many numbers do you want\n"))
s=int(input("how many symbols do you want\n"))
pa=[]
for i in range(l+1):
      ch=random.choice(le)
      pa+=ch
for i in range(n+1):
      ch=random.choice(nu)
      pa+=ch
for i in range(s+1):
      ch=random.choice(sy)
      pa+=ch
random.shuffle(pa)
pas=''
for i in pa:
     pas=pas+i
print(pas) 

      