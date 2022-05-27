def solution(numbers, hand):
    answer = ""
    L = ["1", "4", "7", "*"]
    R = ["3", "6", "9", "#"]
    O = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
    pre = {"L": "*", "R": "#"}
    for i in numbers:
        i = str(i)
        if i in L:
            answer += "L"
            pre["L"] = i
        elif i in R:
            answer += "R"
            pre["R"] = i
        else:
            for x in O :
                if pre["L"] in x:
                    ll = [O.index(x), x.index(pre["L"])]
                if pre["R"] in x:
                    rl = [O.index(x), x.index(pre["R"])]
                if i in x:
                    ml = [O.index(x), x.index(i)]
            lg = abs(ll[0] - ml[0]) +  abs(ll[1]-ml[1])
            rg = abs(rl[0] - ml[0]) +  abs(rl[1]-ml[1])
            if lg < rg:
                answer += "L"
                pre["L"] = i
            elif lg > rg:
                answer += "R"
                pre["R"] = i
            else:
                el = "R" if hand == "right" else "L" 
                answer += el
                pre[el] = i
    return answer

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"

#실행한 결괏값 "LLRLLRLLRR"이(가) 기댓값 LLRLLRLLRL"LLRLLRLLRL"와(과) 다릅니다.