# Complete the braces function below.
def braces(values):
    # (), { }, [ ]
    ans=[];
    for i in values:
        flag = 0;
        c=[];
        for j in i:
            if j ==']':
                if not c:
                    flag =1;
                    break;
                if c[-1]=='[':
                    c.pop();
            elif j == '}':
                if not c:
                    flag =1;
                    break;
                if c[-1]=='{':
                    c.pop();
            elif j == ')':
                if not c:
                    flag=1;
                    break;
                if c[-1]=='(':
                    c.pop();
            else:
                c.append(j);
        if not c and flag != 1:
            ans.append('YES');
        else:
            ans.append('NO');

    return ans;


