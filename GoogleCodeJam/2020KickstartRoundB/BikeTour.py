import sys;

if __name__=='__main__':
    t= int(input());
    
    for i in range(t):
        n = int(input());
        h = list(map(int,input().rstrip.split());
        
        ans =0;
        
        for j in range(len(h)):
            if j==0 or j ==len(h) -1:
                continue;
            if h[j]>h[j-1] and h[j]>h[j+1]:
                ans+=1;
        print('Case #$d: %d'%(i+1, ans));        
