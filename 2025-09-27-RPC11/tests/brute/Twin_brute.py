import random,subprocess,sys
def tw(x):
    x=str(x);return len(x)%2==0 and all(x[i]==x[i+1] for i in range(0,len(x),2))
for _ in range(300):
    a=random.randint(10,10**random.randint(2,7));b=random.randint(a,a+random.randint(0,10**random.randint(1,7)))
    exp=sum(tw(x) for x in range(a,b+1))%10007
    out=subprocess.run([sys.executable,"Twin.py"],input=f"{a}\n{b}\n",capture_output=True,text=True).stdout.strip()
    if int(out)!=exp: print("BAD",a,b,exp,out);break
else: print("ok")
