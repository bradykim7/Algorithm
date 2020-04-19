import sys;

if __name__=='__main__':
    
    t = int(input());
    
    for i in range(t):
        
        nd = input().split();
        n=int(nd[0]); d=int(nd[1]);
        ans =d;
        x= list(map(int,input().rstrip().split()));
        for j in x:
            ans -= d % j
        
        print('Case #%d: %d'%(i+1,ans))
        
        

