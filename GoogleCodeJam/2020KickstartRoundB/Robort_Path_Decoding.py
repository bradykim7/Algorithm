import sys;
    
    
if __name__=='__main__':
    
    t = int(input());
    
    for i in range(t):       
        move = input();
        w=[0];
        h=[0];
        x=[];
        
        for j in move:
            if j =='N':
                h[-1] -= 1;
            elif j =='S':
                h[-1] += 1;
            elif j =='W':
                w[-1] -= 1;
            elif j =='E':
                w[-1] += 1;
            elif j.isdigit():
                x.append(int(j));
            elif j=='(':
                w.append(0)
                h.append(0)
            elif j == ')':
                ww =w.pop();
                hh =h.pop();
                xx =x.pop();
                w[-1]+=ww*xx;
                h[-1]+=hh*xx;
                
        print("Case #%d: %d %d"%(i+1, w[0]%int(1e9)+1, h[0]%int(1e9)+1))
