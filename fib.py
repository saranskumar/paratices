a,b,i=0,1,0
limit=int(input("enter your limit:"))
while i<limit:
    print(a,end=",")
    c=a+b
    a=b
    b=c
    i+=1