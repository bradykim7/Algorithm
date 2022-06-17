import re

def solution(dartResult):
    answer = 0
    l = re.findall("[0-9]{1,2}[SDT][*#]?", dartResult)
    
    for i in l :
        if re.search('[*#]', i) :
            print("KMS")
        
    return answer

kms = solution("10S2D*3T")