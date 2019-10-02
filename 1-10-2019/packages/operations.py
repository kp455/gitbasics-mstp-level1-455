def add(n,m): 
    c=n+m
    print(c)
    

def prime(n):
    fact=0  
    for i in range(1,n+1):
        if n%i==0:
            fact=fact+1
    if(fact==2):
        return True     
    else:
        return False
        
def primefactors(n):
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")        