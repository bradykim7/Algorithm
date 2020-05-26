# Enter your code here. Read input from STDIN. Print output to STDOUT
# This Explanation is really bad. So, don't waste your time and just read input output and deduce it
if __name__ == "__main__":

    n = int(input());

    ans = [0]*100;
    count =0;
    for i in range(n):
        x, arr= input().split();
        x = int(x);
        ans[x] += 1;

    for i in ans:
        count+= i;
        print(count, end=" ")
